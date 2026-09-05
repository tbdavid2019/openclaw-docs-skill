# Providers documentation catalog

Model provider authentication and configuration.

Open only the entries relevant to the current request. Start with at most three documents.

- [Kilo Gateway](../providers/kilocode.md) — Use Kilo Gateway's unified API to access many models in OpenClaw. Read when: You want a single API key for many LLMs; You want to run models via Kilo Gateway in OpenClaw.
- [LiteLLM](../providers/litellm.md) — Run OpenClaw through LiteLLM Proxy for unified model access and cost tracking. Read when: You want to route OpenClaw through a LiteLLM proxy; You need cost tracking, logging, or model routing through LiteLLM.
- [llmman](../providers/llmman.md) — Run OpenClaw through llmman (OpenAI-compatible local server). Read when: You want to run OpenClaw against a local llmman server; You are serving Gemma or another model through llmman; You need the exact OpenClaw compat flags for llmman.
- [LM Studio](../providers/lmstudio.md) — Run OpenClaw with LM Studio. Read when: You want to run OpenClaw with open source models via LM Studio; You want to set up and configure LM Studio.
- [LongCat](../providers/longcat.md) — LongCat API setup for LongCat-2.0. Read when: You want to use LongCat-2.0 with OpenClaw; You need the LongCat API key or model limits.
- [Meta](../providers/meta.md) — Meta setup, authentication, and Muse Spark model selection. Read when: You want to use Meta with OpenClaw; You need the MODEL_API_KEY env var or CLI auth choice.
- [MiniMax](../providers/minimax.md) — Use MiniMax models in OpenClaw. Read when: You want MiniMax models in OpenClaw; You need MiniMax setup guidance.
- [Mistral](../providers/mistral.md) — Use Mistral models and Voxtral transcription with OpenClaw. Read when: You want to use Mistral models in OpenClaw; You want Voxtral realtime transcription for Voice Call; You need Mistral API key onboarding and model refs.
- [Model provider quickstart](../providers/models.md) — Model providers (LLMs) supported by OpenClaw. Read when: You want to choose a model provider; You want quick setup examples for LLM auth + model selection.
- [Moonshot AI](../providers/moonshot.md) — Configure Moonshot Kimi models vs Kimi Coding (separate providers + keys). Read when: You want Moonshot Kimi K3/K2 (Moonshot Open Platform) vs Kimi Coding setup; You need to understand separate endpoints, keys, and model refs; You want copy/paste config for either provider.
- [NovitaAI](../providers/novita.md) — Use NovitaAI's OpenAI-compatible API with OpenClaw. Read when: You want to run OpenClaw with NovitaAI models; You need the Novita provider id, key, or endpoint.
- [NVIDIA](../providers/nvidia.md) — Use NVIDIA's OpenAI-compatible API in OpenClaw. Read when: You want to use open models in OpenClaw for free; You need NVIDIA_API_KEY setup; You want to use Nemotron 3 Ultra through NVIDIA.
- [Ollama](../providers/ollama.md) — Run OpenClaw with Ollama (cloud and local models). Read when: You want to run OpenClaw with cloud or local models via Ollama; You need Ollama setup and configuration guidance; You want Ollama vision models for image understanding.
- [Ollama Cloud](../providers/ollama-cloud.md) — Use Ollama Cloud directly with OpenClaw. Read when: You want to use hosted Ollama models without a local Ollama server; You need the ollama-cloud provider id, key, or endpoint.
- [OpenAI](../providers/openai.md) — Use OpenAI via API keys or Codex subscription in OpenClaw. Read when: You want to use OpenAI models in OpenClaw; You want Codex subscription auth instead of API keys; You want Astra async tools, mid-turn steering, or cached reasoning changes; You need stricter GPT-5 agent execution behavior.
- [OpenCode](../providers/opencode.md) — Use OpenCode Zen and Go catalogs with OpenClaw. Read when: You want OpenCode-hosted model access; You want to pick between the Zen and Go catalogs.
- [OpenCode Go](../providers/opencode-go.md) — Use the OpenCode Go catalog with the shared OpenCode setup. Read when: You want the OpenCode Go catalog; You need the runtime model refs for Go-hosted models.
- [OpenRouter](../providers/openrouter.md) — Use OpenRouter's unified API to access many models in OpenClaw. Read when: You want a single API key for many LLMs; You want to run models via OpenRouter in OpenClaw; You want to use OpenRouter for image generation; You want to use OpenRouter for music generation; You want to use OpenRouter for video generation.
- [Perplexity](../providers/perplexity-provider.md) — Perplexity web search provider setup (API key, search modes, filtering). Read when: You want to configure Perplexity as a web search provider; You need the Perplexity API key or OpenRouter proxy setup.
- [PixVerse](../providers/pixverse.md) — PixVerse video generation setup in OpenClaw. Read when: You want to use PixVerse video generation in OpenClaw; You need the PixVerse API key/env setup; You want to make PixVerse the default video provider.
- [Provider directory](../providers/index.md) — Model providers (LLMs) supported by OpenClaw. Read when: You want to choose a model provider; You need a quick overview of supported LLM backends.
- [Qianfan](../providers/qianfan.md) — Use Qianfan's unified API to access many models in OpenClaw. Read when: You want a single API key for many LLMs; You need Baidu Qianfan setup guidance.
- [Qwen](../providers/qwen.md) — Use Qwen Cloud through its OpenClaw plugin. Read when: You want to use Qwen with OpenClaw; You have an Alibaba Cloud Token Plan subscription.
- [Runway](../providers/runway.md) — Runway video generation setup in OpenClaw. Read when: You want to use Runway video generation in OpenClaw; You need the Runway API key/env setup; You want to make Runway the default video provider.
- [SenseAudio](../providers/senseaudio.md) — SenseAudio batch speech-to-text for inbound voice notes. Read when: You want SenseAudio speech-to-text for audio attachments; You need the SenseAudio API key env var or audio config path.
- [SGLang](../providers/sglang.md) — Run OpenClaw with SGLang (OpenAI-compatible self-hosted server). Read when: You want to run OpenClaw against a local SGLang server; You want OpenAI-compatible /v1 endpoints with your own models.
- [StepFun](../providers/stepfun.md) — Use StepFun models with OpenClaw. Read when: You want StepFun models in OpenClaw; You need StepFun setup guidance.
- [Synthetic](../providers/synthetic.md) — Use Synthetic's Anthropic-compatible API in OpenClaw. Read when: You want to use Synthetic as a model provider; You need a Synthetic API key or base URL setup.
- [Tencent Cloud (TokenHub / TokenPlan)](../providers/tencent.md) — Tencent Cloud TokenHub and TokenPlan setup for hy3. Read when: You want to use Tencent hy3 with OpenClaw; You need the TokenHub or TokenPlan API key setup.
- [Together AI](../providers/together.md) — Together AI setup (auth + model selection). Read when: You want to use Together AI with OpenClaw; You need the API key env var or CLI auth choice.
