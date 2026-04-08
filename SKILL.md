---
name: openclaw-docs
description: Comprehensive documentation for OpenClaw, covering installation, configuration, channels, tools, and advanced settings. Use this skill to answer questions about OpenClaw's architecture, API, and plugin system.
---

# OpenClaw Documentation Skill

This skill provides access to the official documentation of [OpenClaw](https://github.com/openclaw/openclaw), an open-source, local-first AI agent gateway.

## How to use this skill

The documentation is organized into several key areas within the `references/` folder. You can use `grep_search` to find specific keywords or `view_file` to read specific guides.

### Documentation Categories

- **Getting Started**: `references/getting-started/` (Installation, Quickstart, Onboarding)
- **Channels**: `references/channels/` (WhatsApp, Telegram, Discord, Slack, etc.)
- **Tools**: `references/tools/` (Browser automation, Search, Code execution, Media generation)
- **Advanced**: `references/advanced/` (Plugins, Providers, Memory, Architecture)
- **Configuration**: Guides for `openclaw.json` and system settings.

## Common Tasks

### 1. Connecting a New Channel
If you need to connect OpenClaw to a messaging app:
1. Search for the channel in `references/channels/`.
2. Follow the setup instructions (e.g., getting API keys, scan QR codes).

### 2. Configuring Tools
To extend the agent's capabilities:
1. Check `references/tools/` for available tools.
2. configure them in the OpenClaw dashboard or config file.

### 3. Troubleshooting
Common issues are often documented in the specific tool or channel file. Check for "Troubleshooting" or "FAQ" sections within the `.md` files.

---

## Maintenance
To keep this documentation up to date, run:
```bash
sh scripts/sync-docs.sh
```
This will pull the latest content from the upstream OpenClaw repository.
