#!/usr/bin/env python3
"""Radar: scout new Apple Core AI ecosystem resources and auto-update the list.

Searches GitHub and Hugging Face. Confident finds (strong Core AI signal, 1+
stars, classifiable section) are inserted into README.md directly; everything
else that plausibly relates to Core AI is regenerated into RADAR.md as a
watchlist. There is no state file: the README itself is the dedup source and
the watchlist is recomputed from scratch each run, so watchlist items promote
to the README automatically once they gain traction. False positives are
blocked permanently via .github/radar-ignore.txt (one repo/model id per line).

Stdlib only. Auth: GITHUB_TOKEN env var.
"""

import argparse
import base64
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

FRAMEWORK_BIRTH = "2026-05-01"  # Core AI announced at WWDC26; older "coreai" repos are name collisions
GITHUB_QUERIES = [
    f"coreai in:name,description created:>{FRAMEWORK_BIRTH}",
    f'"core ai" apple in:name,description created:>{FRAMEWORK_BIRTH}',
    f"aimodel apple in:name,description created:>{FRAMEWORK_BIRTH}",
    "topic:coreai",
]
EXCLUDED_OWNERS = {"john-rocky"}  # maintainer's own repos are curated manually
HF_EXCLUDED_OWNERS = {"mlboydaisuke", "coreai-community"}  # the zoo's own bundles / mirrors
MIN_README_BYTES = 800
STALE_AFTER_DAYS = 365


def http_get(url, token=None, accept="application/vnd.github+json"):
    req = urllib.request.Request(url, headers={
        "Accept": accept,
        "User-Agent": "awesome-core-ai-radar",
        **({"Authorization": f"Bearer {token}"} if token else {}),
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())


def search_github(token):
    items = {}
    for q in GITHUB_QUERIES:
        url = "https://api.github.com/search/repositories?" + urllib.parse.urlencode(
            {"q": q, "sort": "stars", "order": "desc", "per_page": 50})
        try:
            for item in http_get(url, token).get("items", []):
                items[item["full_name"]] = item
        except Exception as e:
            print(f"warn: search failed for {q!r}: {e}", file=sys.stderr)
    return list(items.values())


def fetch_readme_head(full_name, token):
    try:
        data = http_get(f"https://api.github.com/repos/{full_name}/readme", token)
        raw = base64.b64decode(data.get("content", ""))
        return len(raw), raw[:4000].decode("utf-8", errors="ignore")
    except Exception:
        return 0, ""


def core_ai_signal(haystack):
    """'strong' = confidently about Apple's Core AI framework; 'weak' = plausible; None = noise."""
    mentions = bool(re.search(r"core[\s-]?ai|\.aimodel|\baimodel\b", haystack))
    if not mentions or "apple" not in haystack:
        return None
    if ".aimodel" in haystack or re.search(
            r"ios 27|macos 27|xcode 27|neural engine|apple silicon|on-device|foundation models",
            haystack):
        return "strong"
    return "weak"


def classify(haystack):
    if any(k in haystack for k in ["inference server", "openai-compatible", "api server"]):
        return "## Serving"
    if re.search(r"converted to|ported to|port of|model zoo|\.aimodel format", haystack):
        return "## Models"
    if any(k in haystack for k in ["convert", "conversion", "onnx", "exporter", "quantiz"]):
        return "## Conversion"
    if any(k in haystack for k in ["benchmark", "comparison", " vs "]):
        return "## Benchmarks & engineering notes"
    if any(k in haystack for k in ["book", "tutorial", "guide", "course", "hands-on"]):
        return "## Learning"
    if any(k in haystack for k in ["swiftui", "chat app", "sample app", "swift package", "swiftpm", "runtime"]):
        return "## Running models in your app"
    if re.search(r"\bmodels?\b", haystack):
        return "## Models"
    return None


def clean_description(desc):
    desc = re.sub(r"\s+", " ", (desc or "").strip())
    desc = re.sub(r"[\U0001F000-\U0001FAFF☀-➿]", "", desc).strip()
    desc = desc.replace("|", "\\|")
    if len(desc) > 160:
        desc = desc[:157].rstrip() + "..."
    return desc or "(no description)"


def github_candidates(token, ignored, listed):
    out = []
    cutoff = datetime.now(timezone.utc) - timedelta(days=STALE_AFTER_DAYS)
    for item in search_github(token):
        full = item["full_name"]
        if (full.lower() in ignored or full.lower() in listed or item.get("fork")
                or item.get("archived") or item["owner"]["login"] in EXCLUDED_OWNERS):
            continue
        created = datetime.fromisoformat(item["created_at"].replace("Z", "+00:00"))
        pushed = datetime.fromisoformat(item["pushed_at"].replace("Z", "+00:00"))
        if created < datetime.fromisoformat(FRAMEWORK_BIRTH + "T00:00:00+00:00") or pushed < cutoff:
            continue
        readme_size, readme_head = fetch_readme_head(full, token)
        if readme_size < MIN_README_BYTES:
            continue
        haystack = f"{item.get('description') or ''}\n{readme_head}".lower()
        signal = core_ai_signal(haystack)
        if not signal:
            continue
        out.append({
            "full_name": full,
            "url": item["html_url"],
            "stars": item["stargazers_count"],
            "created": item["created_at"][:10],
            "description": clean_description(item.get("description")),
            "section": classify(haystack),
            "signal": signal,
        })
    return out


def huggingface_candidates(ignored, listed):
    out = []
    try:
        models = http_get("https://huggingface.co/api/models?search=coreai&limit=50",
                          accept="application/json")
    except Exception as e:
        print(f"warn: HF search failed: {e}", file=sys.stderr)
        return out
    for m in models:
        mid = m.get("id", "")
        if (not mid or mid.lower() in ignored or mid.lower() in listed
                or mid.split("/")[0] in HF_EXCLUDED_OWNERS):
            continue
        if "coreai" not in mid.lower() and "aimodel" not in mid.lower():
            continue
        if m.get("downloads", 0) < 5 and m.get("likes", 0) < 1:
            continue  # cut the long tail of name-collision spam
        out.append({"id": mid, "url": f"https://huggingface.co/{mid}",
                    "downloads": m.get("downloads", 0), "likes": m.get("likes", 0)})
    return out


def insert_into_section(readme_lines, section, entry_line):
    """Append entry_line after the last non-empty line of the given section."""
    start = next((i for i, l in enumerate(readme_lines) if l.strip() == section), None)
    if start is None:
        return False
    end = next((i for i in range(start + 1, len(readme_lines))
                if readme_lines[i].startswith("## ")), len(readme_lines))
    last = max((i for i in range(start, end) if readme_lines[i].strip()), default=start)
    readme_lines.insert(last + 1, entry_line)
    return True


def build_watchlist(watch, hf):
    lines = [
        "# Radar watchlist",
        "",
        "*Auto-generated by the weekly [radar](.github/workflows/radar.yml) — do not edit by hand.*",
        "",
        "Repos and models that mention Apple Core AI but haven't yet met the bar for the curated",
        "list (strong signal + some traction + a clear section). Watchlist items are promoted to",
        "[README.md](README.md) automatically once they qualify. Known false positives are blocked",
        "in [.github/radar-ignore.txt](.github/radar-ignore.txt).",
        "",
    ]
    if watch:
        lines += ["## GitHub", "",
                  "| Repo | ★ | Created | Signal | Guessed section | Description |",
                  "|---|---|---|---|---|---|"]
        lines += [f"| [{c['full_name']}]({c['url']}) | {c['stars']} | {c['created']} | "
                  f"{c['signal']} | {(c['section'] or '?').lstrip('# ')} | {c['description']} |"
                  for c in sorted(watch, key=lambda c: (-c["stars"], c["full_name"]))]
        lines.append("")
    if hf:
        lines += ["## Hugging Face", "",
                  "| Model | Downloads | Likes |", "|---|---|---|"]
        lines += [f"| [{m['id']}]({m['url']}) | {m['downloads']} | {m['likes']} |"
                  for m in sorted(hf, key=lambda m: (-m["downloads"], m["id"]))]
        lines.append("")
    if not watch and not hf:
        lines += ["Nothing on the radar right now.", ""]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--readme", default="README.md")
    ap.add_argument("--watchlist", default="RADAR.md")
    ap.add_argument("--ignore", default=".github/radar-ignore.txt")
    ap.add_argument("--commit-msg", default="/tmp/radar-commit-msg.txt")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    ignored = set()
    if os.path.exists(args.ignore):
        with open(args.ignore) as f:
            ignored = {l.split("#")[0].strip().lower() for l in f if l.split("#")[0].strip()}

    with open(args.readme) as f:
        readme = f.read()
    listed = {m.lower() for m in re.findall(r"github\.com/([\w.-]+/[\w.-]+)", readme)}
    listed |= {m.lower() for m in re.findall(r"huggingface\.co/([\w.-]+/[\w.-]+)", readme)}

    gh = github_candidates(token, ignored, listed)
    hf = huggingface_candidates(ignored, listed)

    readme_lines = readme.splitlines()
    placed, watch = [], []
    for c in sorted(gh, key=lambda c: -c["stars"]):
        # Auto-add only confident finds with some traction; the rest wait on the watchlist.
        if (c["signal"] == "strong" and c["stars"] >= 1 and c["section"]
                and insert_into_section(
                    readme_lines, c["section"],
                    f"- [{c['full_name']}]({c['url']}) — {c['description']}")):
            placed.append(c)
        else:
            watch.append(c)

    print(f"radar: placed={len(placed)} watchlist={len(watch)} hf={len(hf)}")
    for c in placed:
        print(f"  ADD {c['full_name']} ({c['stars']}★) -> {c['section']}")
    for c in watch:
        print(f"  watch {c['full_name']} ({c['stars']}★, {c['signal']})")
    for m in hf:
        print(f"  watch HF {m['id']}")

    if args.dry_run:
        return

    if placed:
        with open(args.readme, "w") as f:
            f.write("\n".join(readme_lines) + "\n")
    with open(args.watchlist, "w") as f:
        f.write(build_watchlist(watch, hf))

    msg = ["Radar: add " + ", ".join(c["full_name"] for c in placed) if placed
           else "Radar: refresh watchlist", ""]
    msg += [f"Auto-added to {c['section'][3:]}: {c['full_name']} ({c['stars']} stars)"
            for c in placed]
    msg.append(f"Watchlist: {len(watch)} GitHub + {len(hf)} Hugging Face candidates")
    with open(args.commit_msg, "w") as f:
        f.write("\n".join(msg) + "\n")


if __name__ == "__main__":
    main()
