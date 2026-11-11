# Awesome Core AI

A list of tools, converted models, sample apps, benchmarks and guides for Core AI, Apple's on-device ML runtime in iOS 27 and macOS 27 and the successor to Core ML. It runs `.aimodel` bundles.

## Start with a task

| What you want to do | Start here |
|---|---|
| Try a model before writing code | [Core AI start page](https://john-rocky.github.io/core-ai/) — a Mac download, an iPhone TestFlight and a recorded demo |
| Add a specific model to a Swift app | [CoreAIKit quickstart](https://github.com/john-rocky/coreai-kit#quickstart) — package setup, a small chat model, and the Foundation Models integration |
| Choose a downloadable model | [Core AI model zoo](https://github.com/john-rocky/coreai-model-zoo#models) — model cards, conversion recipes and measurements on each device |
| Give a coding agent the relevant sources | [Task index](https://john-rocky.github.io/core-ai/llms.txt) and [resource manifest](https://john-rocky.github.io/core-ai/resources.json) — package guidance, catalogs, examples, and release links |
| Understand model conversion and runtime behavior | [The Art of Core AI](https://john-rocky.github.io/the-art-of-core-ai/) and the [conversion guide](https://john-rocky.github.io/coreai-model-zoo/knowledge/conversion-guide.html) |
| Get a choice, a score or a yes/no with probabilities, instead of generated text | [`CoreAI.decide`](https://github.com/john-rocky/coreai-kit/blob/main/docs/SYSTEM_ONE.md) — the Swift call and ten example uses on Mac and iPhone, with measurements |

Apple's [Foundation Models](https://developer.apple.com/documentation/foundationmodels) framework gives you the model built into the system. Core AI is for running a model you choose.

I maintain this list. The links in this table are my own projects, and the sections below cover everyone's. A weekly script adds new projects, so I haven't read every community entry. Pull requests are welcome under the rules in [Contributing](#contributing).

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

- [coreai-kit ChatDemo](https://github.com/john-rocky/coreai-kit/tree/0.5.0/Examples/ChatDemo) — SwiftUI chat app and terminal example. Follow the [release quickstart](https://github.com/john-rocky/coreai-kit/blob/0.5.0/README.md#quickstart) for the package path, first model download, and tested environment.
- [timokoethe/CoreAIChat](https://github.com/timokoethe/CoreAIChat) — Minimal SwiftUI chat app for macOS showing the smallest `CoreAILanguageModel` → `LanguageModelSession` wiring.
- [rbniranjan/WWDC2026CoreAI](https://github.com/rbniranjan/WWDC2026CoreAI) — Hands-on examples following the WWDC26 sessions.
- [The Art of Core AI](https://john-rocky.github.io/the-art-of-core-ai/) — Free hands-on book: 13 chapters + labs from first export to custom kernels ([source](https://github.com/john-rocky/the-art-of-core-ai), [Japanese edition on Zenn](https://zenn.dev/mlboydaisuke/books/coreai-textbook)).

## Running models in your app

- [john-rocky/coreai-kit](https://github.com/john-rocky/coreai-kit) — Swift package for chat, vision, speech, and other local model tasks, with downloads, caching, and a catalog pinned to Hugging Face revisions. Catalog models also work with `LanguageModelSession`.
- [rudrankriyam/Core-AI-Framework-Lab](https://github.com/rudrankriyam/Core-AI-Framework-Lab) — Practical lab app: model asset management, specialization states, compute-unit configuration, benchmarking across modalities.
- [Techopolis/AFM-Studio](https://github.com/Techopolis/AFM-Studio) — Chat app spanning Apple Foundation Models, Private Cloud Compute, and Core AI models behind one provider interface.
- [mweinbach/NemotronCoreAI](https://github.com/mweinbach/NemotronCoreAI) — SwiftPM streaming-ASR runtime for NVIDIA Nemotron 3.5 on Core AI.
- [massif-01/coreai-hybrid-state-runtime](https://github.com/massif-01/coreai-hybrid-state-runtime) — Device-validated four-state hybrid decoder support for Apple Core AI sequential runtime.
- [Andrei-cloud/laya-plugin](https://github.com/Andrei-cloud/laya-plugin) — On-device Core AI decision layer for coding agents, over MCP. It downloads its model from Hugging Face at install.
- [SAL2-Dev/ComfyUI-CoreAI](https://github.com/SAL2-Dev/ComfyUI-CoreAI) — Core AI vision nodes (depth, detection, VLM, CLIP, on-device LLM) for ComfyUI.
- [0Itsuki0/Swift_STTWithCoreAI](https://github.com/0Itsuki0/Swift_STTWithCoreAI) — A demo of using the CoreAI framework (OS 27+) for on-device Speech to text.
- [james-333i/coreai-models-xcframework](https://github.com/james-333i/coreai-models-xcframework) — Build scripts for creating coreai-models xcframework to enable support for using it in projects requiring lower min SDK than coreai-models supports.
- [RohanLala04/dult-tracker-detector](https://github.com/RohanLala04/dult-tracker-detector) — On-device BLE tracker detector implementing the Apple-Google DULT spec, with Core AI inference, Swift and Core Bluetooth.
- [AustinJiangH/voixful](https://github.com/AustinJiangH/voixful) — A SpeechAnalyzer-shaped on-device speech API for Apple Silicon — local ASR backends running through Core AI (Nemotron, Parakeet, Granite, Cohere, Canary).
- [oka-yuji/coreai-samples](https://github.com/oka-yuji/coreai-samples) — Open LLMs on Apple silicon with Core AI and Foundation Models: Swift runtime, verification harness, sample app (work in progress)
- [ETeissonniere/coreai-agent](https://github.com/ETeissonniere/coreai-agent) — Native macOS agent app on Core AI with local models, tool use, web search and persistent conversations.

## Models

- [john-rocky/coreai-model-zoo](https://github.com/john-rocky/coreai-model-zoo) — Downloadable Core AI models for language, vision, audio, generation, and forecasting. Each model card links its conversion recipe and test results.
- [Hugging Face: mlboydaisuke](https://huggingface.co/mlboydaisuke) — The zoo's published `.aimodel` bundles.
- [mlboydaisuke/decider-0.8b-CoreAI](https://huggingface.co/mlboydaisuke/decider-0.8b-CoreAI) — A model trained to pick from fixed answers. The converted model picks the same answer as the original on all 44 test rows.
- [kevinqz/coreai-catalog](https://github.com/kevinqz/coreai-catalog) — Source-grounded registry of Core AI models, artifacts, upstreams, and provenance.
- [tmorales2000/fastvlm-coreai](https://github.com/tmorales2000/fastvlm-coreai) — FastVLM vision-language model converted to Apple Core AI .aimodel format for Neural Engine deployment on iOS/macOS 27.
- [RahulRachuri/bonsai-swift](https://github.com/RahulRachuri/bonsai-swift) — Bonsai 2 27B (PrismML ternary Qwen3.8) on Apple Core AI, in Swift.
- [xocialize/coreai-realesrgan-swift](https://github.com/xocialize/coreai-realesrgan-swift) — Real-ESRGAN 4× super-resolution on the Apple Neural Engine via CoreAI — fp16, parity-locked, macOS 27+.

## Conversion

- [apple/coreai-torch](https://github.com/apple/coreai-torch) — The official bring-your-own-PyTorch-model path (see [Official](#official)).
- [devin-lai/coreai-onnx](https://github.com/devin-lai/coreai-onnx) — Convert ONNX models directly to `.aimodel`.
- [coreai-model-zoo/conversion](https://github.com/john-rocky/coreai-model-zoo/tree/main/conversion) — Reproducible per-model conversion recipes (pinned base + overlay) behind every zoo bundle, with a `doctor`/`run` CLI.
- [Conversion guide (zoo knowledge base)](https://john-rocky.github.io/coreai-model-zoo/knowledge/conversion-guide.html) — Which conversion path to use for which model, and an [error index](https://john-rocky.github.io/coreai-model-zoo/knowledge/coreai-error-index.html) for when it fails.
- [lucasnewman/mlx2coreai](https://github.com/lucasnewman/mlx2coreai) — Convert MLX models to Core AI.
- [weichao1221/coreai-models-gui](https://github.com/weichao1221/coreai-models-gui) — SwiftUI GUI for Core AI model export, with ModelScope source support.
- [NagaYu/silicon-forge](https://github.com/NagaYu/silicon-forge) — Pull, convert, quantize, benchmark, and package open-weight LLMs for Apple silicon (MLX → Core AI).
- [massif-01/qwen3-1.7b-coreai-ios](https://github.com/massif-01/qwen3-1.7b-coreai-ios) — High-fidelity Qwen3-1.7B W8 onboarding with A17 Pro Neural Engine validation for Apple Core AI.
- [massif-01/qwen3-1.7b-coreai-reproduction](https://github.com/massif-01/qwen3-1.7b-coreai-reproduction) — Reproducible Qwen3-1.7B Core AI INT4 GPU conversion, physical-device benchmarks, and W8/ANE comparison.
- [sinkect/paddleocr-coreai](https://github.com/sinkect/paddleocr-coreai) — Core AI exporters and Swift runtime for PaddleOCR-VL 1.6 and PP-DocLayoutV3.
- [joaaosc/aguardente](https://github.com/joaaosc/aguardente) — CLI that converts and distills PyTorch models to run natively on Apple silicon through Core AI. At least 32 GB of RAM is recommended.
- [maxffarrell/julia-1-coreai](https://github.com/maxffarrell/julia-1-coreai) — Apple Core AI conversion of Supersonic Labs Julia-1.
- [intexcor/torch-ane](https://github.com/intexcor/torch-ane) — Run PyTorch models on the Apple Neural Engine via Core AI: compile any nn.Module, LLMs with KV cache, Stable Diffusion.

## Serving

- [RedHillsMediaFL/caix](https://github.com/RedHillsMediaFL/caix) — Native Core AI inference server for Apple silicon: OpenAI/Anthropic-compatible API, dashboard, streaming chat.
- [coreai-kit `decide-cli serve`](https://github.com/john-rocky/coreai-kit/tree/main/Examples/Decide#the-same-endpoint-your-client-already-speaks) — A local HTTP server that answers with fixed choices and their probabilities, with curl and Python examples.

## Benchmarks & engineering notes

- [coreai-model-zoo decode-throughput tables](https://github.com/john-rocky/coreai-model-zoo/blob/main/MODELS.md) — Decode speed of each model on an iPhone 17 Pro and an M4 Max, with its output checked against the Hugging Face reference.
- [Core AI knowledge base](https://john-rocky.github.io/coreai-model-zoo/) — Engineering notes organized by topic: stateful KV cache, AOT and specialization, ANE vs GPU authoring rules, quantization levels, chunked prefill, speculative decoding, custom Metal kernels. [`llms.txt`](https://john-rocky.github.io/coreai-model-zoo/llms.txt) indexes every page. ([source](https://github.com/john-rocky/coreai-model-zoo/tree/main/knowledge))
- [rwrun/coreAIvsMLLLM](https://github.com/rwrun/coreAIvsMLLLM) — Core AI vs MLX LLM comparison on iOS (Russian).
- [cadamcat/llms-on-apple-neural-engine](https://github.com/cadamcat/llms-on-apple-neural-engine) — Apple Neural Engine against GPU for local LLM inference on Apple silicon: Core ML, Core AI, MLX and Metal benchmarks, with reproducible tests.

## Learning

- [Steven-ZN/Apple-26-ai-skill](https://github.com/Steven-ZN/Apple-26-ai-skill) — Guides coding agents to trace, compare and optimize Apple Foundation Models, Private Cloud Compute, Core AI and multi-session flows with Instruments, evals and runtime profiles.
- [CoreAIKit integration skill](https://github.com/john-rocky/coreai-kit-skills) — Guides a coding agent through adding a local model to a Swift app.
- [hechen/apple-platforms-27-skills](https://github.com/hechen/apple-platforms-27-skills) — Portable Agent Skills for iOS 27, iPadOS 27, macOS 27 and Xcode 27: SwiftUI migration, App Intents, Foundation Models and Core AI.

## Maintainer

[Daisuke Majima (MLBoy)](https://github.com/john-rocky). I also port the
[Core AI model zoo](https://github.com/john-rocky/coreai-model-zoo) ([huggingface.co/mlboydaisuke](https://huggingface.co/mlboydaisuke)),
run [devicemark](https://devicemark.github.io/), an on-device LLM leaderboard, and wrote
[The Art of Core AI](https://john-rocky.github.io/the-art-of-core-ai/).

## Contributing

PRs welcome. Criteria for inclusion:

- Public repo (or published resource) that is specifically about Apple's Core AI framework / `.aimodel`.
- Has a README that lets a stranger use it: what it is, how to run it, what OS/hardware it needs.
- Model entries should state the license and how correctness was verified (e.g. parity vs the upstream reference).

Keep each entry short and factual, with no superlatives. Each section lists official Apple resources first, then the entries I've chosen. The script adds new ones at the bottom.

A [weekly script](.github/workflows/radar.yml) searches GitHub and Hugging Face for new projects. It adds the ones that clearly mention Core AI and have at least one star, and lists the rest in [RADAR.md](RADAR.md). If an entry is wrong, open an issue or a pull request. A removed project goes in [`.github/radar-ignore.txt`](.github/radar-ignore.txt), so the script doesn't add it back.
