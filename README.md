# Awesome Core AI

> Curated resources for Apple's **Core AI** framework (iOS 27 / macOS 27+) — official tooling,
> converted models, conversion pipelines, sample apps, benchmarks, and learning material.

Core AI is Apple's next-generation on-device ML stack (successor to Core ML): models ship as
`.aimodel` bundles and run on Apple silicon GPU / Neural Engine. This list tracks the ecosystem
growing around it.

*PRs welcome — see [Contributing](#contributing).*

---

## Contents

- [Official](#official)
- [Getting started](#getting-started)
- [Running models in your app](#running-models-in-your-app)
- [Models](#models)
- [Conversion](#conversion)
- [Serving](#serving)
- [Benchmarks & engineering notes](#benchmarks--engineering-notes)
- [Learning](#learning)

## Official

- [apple/coreai-models](https://github.com/apple/coreai-models) — The reference repo: model export recipes, Python primitives, and the Swift runtime packages (`CoreAILM`, `CoreAIObjectDetection`, `CoreAISegmentation`, `CoreAISpeech`, `CoreAIDiffusion`).
- [apple/coreai-torch](https://github.com/apple/coreai-torch) — PyTorch → Core AI IR: `torch.export` conversion, composite ops, custom op lowering, inline Metal kernels.
- [apple/coreai-optimization](https://github.com/apple/coreai-optimization) — Quantization, palettization, and compression for Core AI deployment.
- WWDC26 sessions [324](https://developer.apple.com/videos/play/wwdc2026/324/) · [325](https://developer.apple.com/videos/play/wwdc2026/325/) · [326](https://developer.apple.com/videos/play/wwdc2026/326/) · [330](https://developer.apple.com/videos/play/wwdc2026/330/) — Core AI introduction through advanced topics (session 330 covers quantized TensorOps matmul and FlashAttention).

## Getting started

- [coreai-kit ChatDemo](https://github.com/john-rocky/coreai-kit/tree/main/Examples/ChatDemo) — Open the Xcode project, pick a model in the picker, chat fully on-device; the model downloads once and is cached. Also a terminal path: `swift run chat-cli`.
- [timokoethe/CoreAIChat](https://github.com/timokoethe/CoreAIChat) — Minimal SwiftUI chat app for macOS showing the smallest `CoreAILanguageModel` → `LanguageModelSession` wiring.
- [rbniranjan/WWDC2026CoreAI](https://github.com/rbniranjan/WWDC2026CoreAI) — Hands-on examples following the WWDC26 sessions.
- [The Art of Core AI](https://john-rocky.github.io/the-art-of-core-ai/) — Free hands-on book: 13 chapters + labs from first export to custom kernels ([source](https://github.com/john-rocky/the-art-of-core-ai), [Japanese edition on Zenn](https://zenn.dev/mlboydaisuke/books/coreai-textbook)).

## Running models in your app

- [john-rocky/coreai-kit](https://github.com/john-rocky/coreai-kit) — One line of Swift per model (`ChatSession(catalog: "qwen3.5-2b")`) across LLM / VLM / ASR / TTS / diarization / detection and more; 49-model pinned catalog, nightly on-device gate. SPM.
- [rudrankriyam/Core-AI-Framework-Lab](https://github.com/rudrankriyam/Core-AI-Framework-Lab) — Practical lab app: model asset management, specialization states, compute-unit configuration, benchmarking across modalities.
- [Techopolis/AFM-Studio](https://github.com/Techopolis/AFM-Studio) — Chat app spanning Apple Foundation Models, Private Cloud Compute, and Core AI models behind one provider interface.
- [mweinbach/NemotronCoreAI](https://github.com/mweinbach/NemotronCoreAI) — SwiftPM streaming-ASR runtime for NVIDIA Nemotron 3.5 on Core AI.

## Models

- [john-rocky/coreai-model-zoo](https://github.com/john-rocky/coreai-model-zoo) — 49 models converted and device-verified (iPhone 17 Pro / M4 Max): LLM, VLM, OCR, ASR, TTS, diarization, image/video/music generation, forecasting. Each with a downloadable Hugging Face bundle, conversion recipe, and a ready-to-build app.
- [Hugging Face: mlboydaisuke](https://huggingface.co/mlboydaisuke) — The zoo's published `.aimodel` bundles.
- [SAL2-Dev/ComfyUI-CoreAI](https://github.com/SAL2-Dev/ComfyUI-CoreAI) — Core AI vision nodes (depth, detection, VLM, CLIP, on-device LLM) for ComfyUI.
- [kevinqz/coreai-catalog](https://github.com/kevinqz/coreai-catalog) — Source-grounded registry of Core AI models, artifacts, upstreams, and provenance.

## Conversion

- [apple/coreai-torch](https://github.com/apple/coreai-torch) — The official bring-your-own-PyTorch-model path (see [Official](#official)).
- [devin-lai/coreai-onnx](https://github.com/devin-lai/coreai-onnx) — Convert ONNX models directly to `.aimodel`.
- [coreai-model-zoo/conversion](https://github.com/john-rocky/coreai-model-zoo/tree/main/conversion) — Reproducible per-model conversion recipes (pinned base + overlay) behind every zoo bundle, with a `doctor`/`run` CLI.
- [lucasnewman/mlx2coreai](https://github.com/lucasnewman/mlx2coreai) — Convert MLX models to Core AI.
- [weichao1221/coreai-models-gui](https://github.com/weichao1221/coreai-models-gui) — SwiftUI GUI for Core AI model export, with ModelScope source support.
- [NagaYu/silicon-forge](https://github.com/NagaYu/silicon-forge) — Pull, convert, quantize, benchmark, and package open-weight LLMs for Apple silicon (MLX → Core AI).

## Serving

- [RedHillsMediaFL/caix](https://github.com/RedHillsMediaFL/caix) — Native Core AI inference server for Apple silicon: OpenAI/Anthropic-compatible API, dashboard, streaming chat.

## Benchmarks & engineering notes

- [coreai-model-zoo decode-throughput tables](https://github.com/john-rocky/coreai-model-zoo#models) — Device-verified tok/s (greedy, top-1 exact vs the Hugging Face reference) on iPhone 17 Pro GPU/ANE and M4 Max.
- [coreai-model-zoo/knowledge](https://github.com/john-rocky/coreai-model-zoo/tree/main/knowledge) — Port write-ups and engineering notes: ANE vs GPU trade-offs, quantization ladders, chunked prefill, speculative decoding, custom Metal kernels.
- [rwrun/coreAIvsMLLLM](https://github.com/rwrun/coreAIvsMLLLM) — Core AI vs MLX LLM comparison on iOS (Russian).

## Learning

- [The Art of Core AI](https://john-rocky.github.io/the-art-of-core-ai/) — see [Getting started](#getting-started).
- WWDC26 sessions — see [Official](#official).
- [Steven-ZN/Apple-26-ai-skill](https://github.com/Steven-ZN/Apple-26-ai-skill) — Guide coding agents to instrument, trace, compare, and optimize Apple Foundation Models, PCC, Core AI, and multi-session agentic flows using Instruments, str...

## Contributing

PRs welcome. Criteria for inclusion:

- Public repo (or published resource) that is specifically about Apple's Core AI framework / `.aimodel`.
- Has a README that lets a stranger use it: what it is, how to run it, what OS/hardware it needs.
- Model entries should state the license and how correctness was verified (e.g. parity vs the upstream reference).

One line per entry, factual tone, no superlatives. Within each section: official Apple
resources first, then entries ordered by how useful and proven they are for that section's
purpose — never by authorship. New radar finds join at the bottom until they earn a higher spot.

New entries are also scouted and added weekly by an automated [radar](.github/workflows/radar.yml)
(GitHub / Hugging Face search): confident finds — a strong Core AI signal plus some traction —
land in the list automatically, and everything else waits in [RADAR.md](RADAR.md) until it
qualifies. Spotted a bad entry? Open an issue or PR; removals are pinned in
[`.github/radar-ignore.txt`](.github/radar-ignore.txt) so the radar never re-adds them.
