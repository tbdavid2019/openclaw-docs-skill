---
name: openclaw-docs
description: Comprehensive expert documentation for OpenClaw. Use this skill to diagnose gateway failures, configure channels (WhatsApp, Telegram, etc.), manage model providers, and troubleshoot CLI/Service errors using a structured diagnostic ladder and reference index.
---

# OpenClaw Expert Maintenance Guide

This skill transforms the agent into a senior OpenClaw engineer. It provides structured procedures for maintaining, configuring, and troubleshooting the OpenClaw gateway.

## 1. The Diagnostic Ladder (Troubleshooting SOP)

When an issue occurs, DO NOT guess. Follow this 5-step diagnostic sequence in order:

1.  **Global Status Check**: Run `openclaw status`. Is the gateway even listed as active?
2.  **Service Daemon Check**: Run `openclaw gateway status`. Check if the daemon is running, stopped, or errored.
3.  **Log Analysis**: Run `openclaw logs --latest` (or check `~/.openclaw/logs/`). Look for "ERROR" or "CRITICAL" tags.
4.  **Automated Doctor**: Run `openclaw doctor`. This will check port availability, node versions, and common config errors.
5.  **Channel Connectivity**: Run `openclaw channels status --probe`. Check if specific channels (e.g., WhatsApp) are authenticated and connected.

## 2. Troubleshooting Matrix (Common Errors)

| Error Signature | Potential Root Cause | Fix Procedure |
|---|---|---|
| `EADDRINUSE: address already in use` | Gateway port (default 1333) is blocked by another process. | 1. Run `openclaw gateway stop --force`. <br> 2. Change port in `openclaw.json` if needed. |
| `401 Unauthorized` / `Auth failed` | Expired API Key or incorrect Provider token. | 1. Verify `openclaw.json` secrets. <br> 2. Open dashboard to re-authenticate provider. |
| `WhatsApp: Scan QR Code` | Session expired or disconnected. | Run `openclaw channels login <id>` and scan the QR code. |
| `mDNS/Bonjour Discovery failed` | Network isolation or firewall blocking multicast. | Check `references/advanced/bonjour.md` for firewall settings. |

## 3. Operational Workflows

### Configuring Channels
- **Setup**: Refer to `references/channels/` for specific platform guides.
- **Verification**: Always run `openclaw channels list` after adding.

### Managing Tools & Skills
- **Configuration**: Skills are configured in `openclaw.json` or through the TUI.
- **Reference**: See `references/tools/skills-config.md` for JSON schema details.

### Updating Documentation
- **Procedure**: Run `sh scripts/sync-docs.sh` to pull the latest official docs into `references/`.
- **Note**: This keeps the agent's knowledge base current with the upstream repository.

## 4. Documentation Index (Internal References)

Use `grep_search` or `view_file` on these specialized folders:

- **Setup & Install**: `references/getting-started/` (onboarding, setup, quickstart)
- **Messaging Channels**: `references/channels/` (WhatsApp, Telegram, Discord, Slack, etc.)
- **Agent Capabilities**: `references/tools/` (Browser, Search, Code Execution, Subagents)
- **Internal Architecture**: `references/advanced/` (Plugins, Memory, Providers, Security)

---

> [!IMPORTANT]
> **Constraint**: Always prioritize official reference files for specific API parameters. The `SKILL.md` provides the *logic*, while the `references/` files provide the *data*.
