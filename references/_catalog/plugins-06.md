# Plugins documentation catalog

Plugin architecture, SDKs, and bundled integrations.

Open only the entries relevant to the current request. Start with at most three documents.

- [Plugin reference](../plugins/reference.md) — Generated index of OpenClaw plugin reference pages. Read when: You need a reference page for a specific OpenClaw plugin; You are auditing plugin docs coverage.
- [Plugin runtime helpers](../plugins/sdk-runtime.md) — api.runtime -- the injected runtime helpers available to plugins. Read when: You need to call core helpers from a plugin (TTS, STT, image gen, web search, Gateway, subagent, nodes); You want to understand what api.runtime exposes; You are accessing config, agent, or media helpers from plugin code; You are implementing model-picker persistence in a channel plugin.
- [Plugin SDK migration](../plugins/sdk-migration.md) — Migrate from the legacy backwards-compatibility layer to the modern plugin SDK. Read when: You used api.registerEmbeddedExtensionFactory before OpenClaw 2026.4.25; You are updating a plugin to the modern plugin architecture; You maintain an external OpenClaw plugin.
- [Plugin SDK overview](../plugins/sdk-overview.md) — Import map, registration API reference, and SDK architecture. Read when: You need to know which SDK subpath to import from; You want a reference for all registration methods on OpenClawPluginApi; You are looking up a specific SDK export.
- [Plugin SDK subpaths](../plugins/sdk-subpaths.md) — Plugin SDK subpath catalog: which imports live where, grouped by area. Read when: Choosing the right plugin-sdk subpath for a plugin import; Auditing bundled-plugin subpaths and helper surfaces.
- [Plugin setup and config](../plugins/sdk-setup.md) — Setup wizards, setup-entry.ts, config schemas, and package.json metadata. Read when: You are adding a setup wizard to a plugin; You need to understand setup-entry.ts vs index.ts; You are defining plugin config schemas or package.json openclaw metadata.
- [Plugin testing](../plugins/sdk-testing.md) — Testing utilities and patterns for OpenClaw plugins. Read when: You are writing tests for a plugin; You need test utilities from the plugin SDK; You want to understand contract tests for bundled plugins.
- [Policy plugin](../plugins/reference/policy.md) — Adds policy-backed doctor checks for workspace conformance. Read when: You are installing, configuring, or auditing the policy plugin.
- [QA Channel plugin](../plugins/reference/qa-channel.md) — Adds the QA Channel surface for sending and receiving OpenClaw messages. Read when: You are installing, configuring, or auditing the qa-channel plugin.
- [QA Lab plugin](../plugins/reference/qa-lab.md) — OpenClaw QA lab plugin with private debugger UI and scenario runner. Read when: You are installing, configuring, or auditing the qa-lab plugin.
- [Qianfan plugin](../plugins/reference/qianfan.md) — Adds Qianfan model provider support to OpenClaw. Read when: You are installing, configuring, or auditing the qianfan plugin.
- [QQ Bot plugin](../plugins/reference/qqbot.md) — OpenClaw QQ Bot channel plugin for group and direct-message workflows. Read when: You are installing, configuring, or auditing the qqbot plugin.
- [Qwen plugin](../plugins/reference/qwen.md) — Adds Qwen, Qwen Cloud, Model Studio, DashScope, Qwen Token Plan, Bailian Token Plan model provider support to OpenClaw. Read when: You are installing, configuring, or auditing the qwen plugin.
- [Raft plugin](../plugins/reference/raft.md) — OpenClaw Raft channel plugin for secure CLI wake bridges. Read when: You are installing, configuring, or auditing the raft plugin.
- [Reef plugin](../plugins/reference/reef.md) — Guarded end-to-end encrypted claw channel. Read when: You are installing, configuring, or auditing the reef plugin.
- [Registering tools](../plugins/agent-tools.md) — Redirects to Building Plugins (registering tools section). Read when: Legacy link to agent-tools.
- [Runway plugin](../plugins/reference/runway.md) — Adds video generation provider support. Read when: You are installing, configuring, or auditing the runway plugin.
- [SearXNG plugin](../plugins/reference/searxng.md) — Adds web search provider support. Read when: You are installing, configuring, or auditing the searxng plugin.
- [Senseaudio plugin](../plugins/reference/senseaudio.md) — Adds media understanding provider support. Read when: You are installing, configuring, or auditing the senseaudio plugin.
- [SGLang plugin](../plugins/reference/sglang.md) — Adds SGLang model provider support to OpenClaw. Read when: You are installing, configuring, or auditing the sglang plugin.
- [Signal plugin](../plugins/reference/signal.md) — Adds the Signal channel surface for sending and receiving OpenClaw messages. Read when: You are installing, configuring, or auditing the signal plugin.
- [Slack plugin](../plugins/reference/slack.md) — OpenClaw Slack channel plugin for channels, DMs, commands, and app events. Read when: You are installing, configuring, or auditing the slack plugin.
- [Sms plugin](../plugins/reference/sms.md) — Twilio SMS/MMS channel plugin for OpenClaw messages. Read when: You are installing, configuring, or auditing the sms plugin.
- [StepFun plugin](../plugins/reference/stepfun.md) — Adds StepFun, StepFun Plan model provider support to OpenClaw. Read when: You are installing, configuring, or auditing the stepfun plugin.
- [Supervise Codex sessions](../plugins/codex-supervision.md) — Browse non-archived native Codex sessions and paginated transcripts across OpenClaw nodes. Read when: You want Codex Desktop or CLI sessions to appear in OpenClaw; You need to branch from or archive a stored or idle local Codex session; You are exposing Codex sessions and transcript history from paired nodes.
- [Synology Chat plugin](../plugins/reference/synology-chat.md) — Synology Chat channel plugin for OpenClaw channels and direct messages. Read when: You are installing, configuring, or auditing the synology-chat plugin.
- [Synthetic plugin](../plugins/reference/synthetic.md) — Adds Synthetic model provider support to OpenClaw. Read when: You are installing, configuring, or auditing the synthetic plugin.
- [Talk Voice plugin](../plugins/reference/talk-voice.md) — Manage Talk voice selection (list/set). Read when: You are installing, configuring, or auditing the talk-voice plugin.
- [Tavily plugin](../plugins/reference/tavily.md) — Adds agent-callable tools. Adds web search provider support. Read when: You are installing, configuring, or auditing the tavily plugin.
- [Telegram plugin](../plugins/reference/telegram.md) — Adds the Telegram channel surface for sending and receiving OpenClaw messages. Read when: You are installing, configuring, or auditing the telegram plugin.
