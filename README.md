# Awesome Core AI

> Curated resources for Apple's **Core AI** framework (iOS 27 / macOS 27+) — official tooling,
> converted models, conversion pipelines, sample apps, benchmarks, and learning material.

Need to try a local model, add one to a Swift app, or convert your own? Start with the route below. Core AI uses `.aimodel` bundles on iOS 27 / macOS 27; the linked projects document their own model, device, and toolchain requirements.

## Start with a task

| What you want to do | Start here |
|---|---|
| Try a model before writing code | [Core AI start page](https://john-rocky.github.io/core-ai/) — Mac download, iPhone TestFlight, and a recorded demo with its test environment |
| Add a specific model to a Swift app | [CoreAIKit quickstart](https://github.com/john-rocky/coreai-kit#quickstart) — package setup, a small chat model, and the Foundation Models integration |
| Choose a downloadable model | [Core AI model zoo](https://github.com/john-rocky/coreai-model-zoo#models) — model cards, conversion recipes, and device-specific evidence |
| Give a coding agent the relevant sources | [Task index](https://john-rocky.github.io/core-ai/llms.txt) and [resource manifest](https://john-rocky.github.io/core-ai/resources.json) — package guidance, catalogs, examples, and release links |
| Understand model conversion and runtime behavior | [The Art of Core AI](https://john-rocky.github.io/the-art-of-core-ai/) and the [conversion guide](https://john-rocky.github.io/coreai-model-zoo/knowledge/conversion-guide.html) |

Check Apple's system-provided models and task APIs first. A custom model is useful when the app needs a particular model or capability; the linked releases state what was actually tested, including beta environments.

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

- [coreai-kit ChatDemo](https://github.com/john-rocky/coreai-kit/tree/0.4.1/Examples/ChatDemo) — SwiftUI chat app and terminal example. Follow the [release quickstart](https://github.com/john-rocky/coreai-kit/blob/0.4.1/README.md#quickstart) for the package path, first model download, and tested environment.
- [timokoethe/CoreAIChat](https://github.com/timokoethe/CoreAIChat) — Minimal SwiftUI chat app for macOS showing the smallest `CoreAILanguageModel` → `LanguageModelSession` wiring.
- [rbniranjan/WWDC2026CoreAI](https://github.com/rbniranjan/WWDC2026CoreAI) — Hands-on examples following the WWDC26 sessions.
- [The Art of Core AI](https://john-rocky.github.io/the-art-of-core-ai/) — Free hands-on book: 13 chapters + labs from first export to custom kernels ([source](https://github.com/john-rocky/the-art-of-core-ai), [Japanese edition on Zenn](https://zenn.dev/mlboydaisuke/books/coreai-textbook)).

## Running models in your app

- [john-rocky/coreai-kit](https://github.com/john-rocky/coreai-kit) — Swift package for chat, vision, speech, and other local model tasks, with downloads, caching, and a catalog pinned to Hugging Face revisions. Catalog models can plug into `LanguageModelSession`; see the documented tool-calling and guided-generation limits.
- [rudrankriyam/Core-AI-Framework-Lab](https://github.com/rudrankriyam/Core-AI-Framework-Lab) — Practical lab app: model asset management, specialization states, compute-unit configuration, benchmarking across modalities.
- [Techopolis/AFM-Studio](https://github.com/Techopolis/AFM-Studio) — Chat app spanning Apple Foundation Models, Private Cloud Compute, and Core AI models behind one provider interface.
- [mweinbach/NemotronCoreAI](https://github.com/mweinbach/NemotronCoreAI) — SwiftPM streaming-ASR runtime for NVIDIA Nemotron 3.5 on Core AI.
- [massif-01/coreai-hybrid-state-runtime](https://github.com/massif-01/coreai-hybrid-state-runtime) — Device-validated four-state hybrid decoder support for Apple Core AI sequential runtime

## Models

- [john-rocky/coreai-model-zoo](https://github.com/john-rocky/coreai-model-zoo) — Downloadable Core AI models for language, vision, audio, generation, and forecasting. Model cards link the conversion recipe, validation results, and available sample app; platform support and test coverage vary by model.
- [Hugging Face: mlboydaisuke](https://huggingface.co/mlboydaisuke) — The zoo's published `.aimodel` bundles.
- [SAL2-Dev/ComfyUI-CoreAI](https://github.com/SAL2-Dev/ComfyUI-CoreAI) — Core AI vision nodes (depth, detection, VLM, CLIP, on-device LLM) for ComfyUI.
- [kevinqz/coreai-catalog](https://github.com/kevinqz/coreai-catalog) — Source-grounded registry of Core AI models, artifacts, upstreams, and provenance.
- [tmorales2000/fastvlm-coreai](https://github.com/tmorales2000/fastvlm-coreai) — FastVLM vision-language model converted to Apple Core AI .aimodel format for Neural Engine deployment on iOS/macOS 27.
- [0Itsuki0/Swift_STTWithCoreAI](https://github.com/0Itsuki0/Swift_STTWithCoreAI) — A demo of using the CoreAI framework (OS 27+) for on-device Speech to text.

## Conversion

- [apple/coreai-torch](https://github.com/apple/coreai-torch) — The official bring-your-own-PyTorch-model path (see [Official](#official)).
- [devin-lai/coreai-onnx](https://github.com/devin-lai/coreai-onnx) — Convert ONNX models directly to `.aimodel`.
- [coreai-model-zoo/conversion](https://github.com/john-rocky/coreai-model-zoo/tree/main/conversion) — Reproducible per-model conversion recipes (pinned base + overlay) behind every zoo bundle, with a `doctor`/`run` CLI.
- [Conversion guide (zoo knowledge base)](https://john-rocky.github.io/coreai-model-zoo/knowledge/conversion-guide.html) — Which path for which model (zoo recipe / Apple preset / re-author / `TorchConverter` five-liner / ONNX), the canonical API, and the [error index](https://john-rocky.github.io/coreai-model-zoo/knowledge/coreai-error-index.html) for when it fails.
- [lucasnewman/mlx2coreai](https://github.com/lucasnewman/mlx2coreai) — Convert MLX models to Core AI.
- [weichao1221/coreai-models-gui](https://github.com/weichao1221/coreai-models-gui) — SwiftUI GUI for Core AI model export, with ModelScope source support.
- [NagaYu/silicon-forge](https://github.com/NagaYu/silicon-forge) — Pull, convert, quantize, benchmark, and package open-weight LLMs for Apple silicon (MLX → Core AI).
- [massif-01/qwen3-1.7b-coreai-ios](https://github.com/massif-01/qwen3-1.7b-coreai-ios) — High-fidelity Qwen3-1.7B W8 onboarding with A17 Pro Neural Engine validation for Apple Core AI.
- [massif-01/qwen3-1.7b-coreai-reproduction](https://github.com/massif-01/qwen3-1.7b-coreai-reproduction) — Reproducible Qwen3-1.7B Core AI INT4 GPU conversion, physical-device benchmarks, and W8/ANE comparison.
- [AustinJiangH/voixful](https://github.com/AustinJiangH/voixful) — A SpeechAnalyzer-shaped on-device speech API for Apple Silicon — local ASR backends running through Core AI (Nemotron, Parakeet, Granite, Cohere, Canary).
- [xocialize/coreai-realesrgan-swift](https://github.com/xocialize/coreai-realesrgan-swift) — Real-ESRGAN 4× super-resolution on the Apple Neural Engine via CoreAI — fp16, parity-locked, macOS 27+
- [sinkect/paddleocr-coreai](https://github.com/sinkect/paddleocr-coreai) — Core AI exporters and Swift runtime for PaddleOCR-VL 1.6 and PP-DocLayoutV3.
- [ETeissonniere/coreai-agent](https://github.com/ETeissonniere/coreai-agent) — (no description)
- [joaaosc/aguardente](https://github.com/joaaosc/aguardente) — Ferramenta CLI elegante e minimalista baseada no framework CoreAI para a converter e destilar automaticamente modelos PyTorch em nativo Apple Silicon. Recome...
- [cadamcat/llms-on-apple-neural-engine](https://github.com/cadamcat/llms-on-apple-neural-engine) — Apple Neural Engine (ANE/NPU) vs GPU for local LLM inference on Apple Silicon / macOS. Core ML (CoreML), Core AI (CoreAI), MLX and Metal benchmarks: prefill,...

## Serving

- [RedHillsMediaFL/caix](https://github.com/RedHillsMediaFL/caix) — Native Core AI inference server for Apple silicon: OpenAI/Anthropic-compatible API, dashboard, streaming chat.

## Benchmarks & engineering notes

- [coreai-model-zoo decode-throughput tables](https://github.com/john-rocky/coreai-model-zoo#models) — Device-verified tok/s (greedy, top-1 exact vs the Hugging Face reference) on iPhone 17 Pro GPU/ANE and M4 Max.
- [Core AI knowledge base](https://john-rocky.github.io/coreai-model-zoo/) — Engineering notes organized by topic: stateful KV cache, AOT and specialization, ANE vs GPU authoring rules, quantization ladders, chunked prefill, speculative decoding, custom Metal kernels. Apple documents the API surface; these cover what the runtime does when you run it — thresholds, failure modes, measured numbers. [`llms.txt`](https://john-rocky.github.io/coreai-model-zoo/llms.txt) indexes every page. ([source](https://github.com/john-rocky/coreai-model-zoo/tree/main/knowledge))
- [rwrun/coreAIvsMLLLM](https://github.com/rwrun/coreAIvsMLLLM) — Core AI vs MLX LLM comparison on iOS (Russian).

## Learning

- [The Art of Core AI](https://john-rocky.github.io/the-art-of-core-ai/) — see [Getting started](#getting-started).
- WWDC26 sessions — see [Official](#official).
- [Steven-ZN/Apple-26-ai-skill](https://github.com/Steven-ZN/Apple-26-ai-skill) — Guide coding agents to instrument, trace, compare, and optimize Apple Foundation Models, PCC, Core AI, and multi-session agentic flows using Instruments, str...
- [CoreAIKit integration skill](https://github.com/john-rocky/coreai-kit-skills) — Installable coding-agent guide for adding a local model to a Swift app, with exact release/catalog selection, platform-specific bundle lookup, and first-download handling.

## Maintainer

[**Daisuke Majima (MLBoy)**](https://github.com/john-rocky) — who also ports the
[Core AI model zoo](https://github.com/john-rocky/coreai-model-zoo) ([huggingface.co/mlboydaisuke](https://huggingface.co/mlboydaisuke)),
runs [devicemark](https://devicemark.github.io/) (on-device LLM leaderboard), and wrote
[The Art of Core AI](https://john-rocky.github.io/the-art-of-core-ai/). Entries above are ordered by usefulness, not authorship.

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
