---
name: openclaw-docs
description: Comprehensive guide for installing, configuring, operating, and troubleshooting OpenClaw — a self-hosted, multi-channel AI agent gateway. Use when the user asks about OpenClaw setup, configuration, channel management (WhatsApp/Telegram/Discord/Slack/iMessage/etc.), model provider setup, Gateway operations, multi-agent routing, security hardening, troubleshooting, or any maintenance task related to their local OpenClaw installation. Also use when encountering errors from `openclaw` CLI commands or the Gateway daemon.
---

# OpenClaw Maintenance Skill

> [!CAUTION]
> ## Auto Self-Update on Every Invocation
> Because the documentation changes frequently, try to refresh the installed skill checkout on each invocation when possible.
>
> Use this boundary:
> 1. **Do auto-update the installed skill checkout** with `git -C <skill-directory> pull origin main --ff-only`.
> 2. **Do not run repo-maintenance scripts** such as `scripts/sync-docs.sh` or `scripts/generate_index.py` during normal skill usage.
> 3. If `git pull` fails, continue with the local files and do not block the user.

OpenClaw is a self-hosted, open-source gateway that routes AI agents across WhatsApp, Telegram, Discord, Slack, iMessage, Signal, and 15+ other channels simultaneously.

1. **Find the local skill directory** — it will be somewhere under the agent's skills path (e.g., `~/.gemini/antigravity/skills/openclaw-docs/`).

2. **Before using the docs, try to self-update** by running:
   ```bash
   git -C <skill-directory> pull origin main --ff-only
   ```
   After pulling, reload any reference files you are about to use.

3. **If pull fails** (no internet, API rate limit, git not available) → silently continue using the local version. Never block the user.

4. **If already up-to-date** → proceed normally with no output to the user.

> **Key principle**: The user never needs to manually sync or update. The LLM handles this autonomously.


Use `view_file` or `grep_search` to read these references as needed.

**MANDATORY: Always check [references/SKILL_INDEX.md](references/SKILL_INDEX.md) first to locate the exact documentation needed for any OpenClaw task.**

| Reference | Coverage |
|---|---|
| [SKILL_INDEX.md](references/SKILL_INDEX.md) | **Directory of ALL available documentation (Start here)** |
| [channels/](references/channels/) | Channel setup (WhatsApp, Telegram, Discord, Slack, iMessage, etc.) |
| [providers/](references/providers/) | Model provider setup (Anthropic, OpenAI, Google, Ollama, etc.) |
| [tools/](references/tools/) | Detailed per-tool documentation (exec, browser, web, etc.) |
| [gateway/](references/gateway/) | Gateway operations, config, and security |
| [automation/](references/automation/) | Cron jobs, webhooks, and background tasks |
| [concepts/](references/concepts/) | Core concepts: agent loop, memory, queue, sessions |
| [diagnostics/](references/diagnostics/) | Troubleshooting guides and failure walkthroughs |
| [cli/](references/cli/) | Full CLI command reference |
| [install/](references/install/) | Installation, updating, and migration |
| [platforms/](references/platforms/) | OS-specific guides (macOS, Linux, Windows, etc.) |
| [web/](references/web/) | Web Surfaces: Dashboard, Control UI, TUI, nodes |

## Quick Reference

### Key Paths

| Path | Purpose |
|---|---|
| `~/.openclaw/openclaw.json` | Main config (JSON5) |
| `~/.openclaw/.env` | Global env fallback |
| `~/.openclaw/workspace` | Default agent workspace |
| `~/.openclaw/agents/<id>/` | Per-agent state + sessions |
| `~/.openclaw/skills/` | Managed/local skills |
| `~/.openclaw/agents/<id>/qmd/` | QMD memory backend state |
| `~/.openclaw/agents/<id>/agent/auth-profiles.json` | Auth profiles + OAuth tokens |
| `OPENCLAW_CONFIG_PATH` | Override config location |
| `OPENCLAW_STATE_DIR` | Override state directory |
| `OPENCLAW_HOME` | Override home directory |

### Essential Commands

```bash
openclaw status                    # Overall status
openclaw gateway status            # Gateway daemon status
openclaw gateway status --deep     # Deep scan including system services
openclaw doctor                    # Diagnose config/service issues
openclaw doctor --fix              # Auto-fix safe issues
openclaw logs --follow             # Tail gateway logs
openclaw channels status --probe   # Channel health check
openclaw security audit            # Security posture check
openclaw security audit --fix      # Auto-fix security issues
openclaw update                    # Self-update
openclaw dashboard                 # Open Control UI in browser
openclaw tui                       # Terminal UI (interactive REPL)
openclaw agent                     # Direct agent interaction via CLI
openclaw health                    # Health check
openclaw usage                     # Usage tracking
openclaw config validate           # Validate config file
openclaw config file               # Print active config path
openclaw sessions cleanup          # Session disk cleanup
openclaw agents bindings           # Agent-channel bindings
openclaw agents bind               # Bind agent to account
openclaw agents unbind             # Unbind agent
openclaw update --dry-run          # Preview update
openclaw system presence           # View connected clients/nodes
openclaw system heartbeat last     # Last heartbeat info
openclaw system heartbeat now      # Trigger heartbeat immediately
openclaw memory search <query>     # CLI memory search
openclaw docs <query>              # Search OpenClaw docs
openclaw tasks list                # List background/detached task runs
openclaw tasks show <id>           # Show specific task details
openclaw tasks cancel <id>         # Cancel a running task
openclaw tasks audit               # Identify problematic task runs
openclaw agent --message "..."     # Run single agent turn (scripted/testing)
openclaw nodes pending             # List pending pairing requests
openclaw nodes approve <id>        # Approve node pairing
openclaw nodes status              # Show all paired nodes
openclaw health --json             # Full health snapshot (JSON)
openclaw message send --media <p>  # Send media message
```

### Default Gateway

- Bind: `127.0.0.1:18789` (loopback)
- Dashboard: `http://127.0.0.1:18789/`
- Protocol: WebSocket (JSON text frames)

## Core Workflow

### Diagnosing Issues

Always follow this command ladder in order — do NOT skip steps:

1. `openclaw status` — quick overview
2. `openclaw gateway status` — daemon running? RPC probe ok?
3. `openclaw logs --follow` — watch for errors
4. `openclaw doctor` — config/service diagnostics
5. `openclaw channels status --probe` — per-channel health

### Starting / Restarting Gateway

```bash
# Foreground with verbose logging
openclaw gateway --port 18789 --verbose

# Force-kill existing listener then start
openclaw gateway --force

# Service management (launchd on macOS, systemd on Linux)
openclaw gateway install
openclaw gateway start
openclaw gateway stop
openclaw gateway restart
```

### Configuration

Edit config via any method:

```bash
# Interactive wizard
openclaw onboard                    # Full setup
openclaw configure                  # Config wizard

# CLI one-liners
openclaw config get <path>          # Read value
openclaw config set <path> <value>  # Set value (JSON5 or raw string)
openclaw config unset <path>        # Remove value

# Direct edit
# Edit ~/.openclaw/openclaw.json (JSON5 format)
# Gateway hot-reloads on save (if gateway.reload.mode != "off")
```

Minimal config example:

```json5
{
  agents: { defaults: { workspace: "~/.openclaw/workspace" } },
  channels: { whatsapp: { allowFrom: ["+15555550123"] } },
}
```

### Channel Setup

For detailed per-channel setup, see [references/channels/](references/channels/).
For per-channel troubleshooting (failure signatures, setup walkthroughs), see [references/diagnostics/](references/diagnostics/).
For plugins adding new channels (Matrix, Nostr, MS Teams, etc.), see [references/plugins/](references/plugins/).

Quick channel add:

```bash
# Interactive wizard
openclaw channels add

# Non-interactive
openclaw channels add --channel telegram --account default --name "My Bot" --token $BOT_TOKEN
openclaw channels login --channel whatsapp     # QR pairing for WhatsApp
openclaw channels status --probe               # Verify
```

### Model Provider Setup

For detailed provider setup, see [references/providers/](references/providers/).

```bash
# Set default model
openclaw models set anthropic/claude-sonnet-4-5

# List available models
openclaw models list --all

# Check auth/token status
openclaw models status --probe

# Add auth interactively
openclaw models auth add
```

Config example:

```json5
{
  agents: {
    defaults: {
      model: {
        primary: "anthropic/claude-sonnet-4-5",
        fallbacks: ["openai/gpt-4o"],
      },
    },
  },
}
```

### Multi-Agent Routing

For detailed multi-agent config, see [references/concepts/](references/concepts/).

```bash
openclaw agents add <id>                # Create agent
openclaw agents list --bindings         # Show agent-channel bindings
openclaw agents delete <id>             # Remove agent
```

### Nodes (iOS / Android / macOS / Headless)

For detailed node setup, see [references/nodes/](references/nodes/).

```bash
openclaw nodes status                   # List connected nodes
openclaw nodes describe --node <id>     # Node capabilities
openclaw devices list                   # Pending device approvals
openclaw devices approve <requestId>    # Approve a device
openclaw node run --host <host> --port 18789  # Start headless node host
```

### Security

For detailed security hardening, see [references/gateway/security.md](references/gateway/security.md) and [references/security/](references/security/).

```bash
openclaw security audit                 # Check posture
openclaw security audit --deep          # Live gateway probe
openclaw security audit --fix           # Auto-fix safe issues
openclaw secrets reload                 # Re-resolve secret refs
openclaw secrets audit                  # Scan for plaintext leaks
```

### Update / Uninstall

For detailed installation, updating, rollback, and migration guide, see [references/install/](references/install/).

```bash
# Install (recommended)
curl -fsSL https://openclaw.ai/install.sh | bash

# Update
openclaw update                    # Self-update command
# Or: npm install -g openclaw@latest
openclaw doctor                    # Run after update to apply migrations

# Uninstall
openclaw uninstall
```

### Keeping This Skill Up-to-Date

This skill syncs its `references/` from the official OpenClaw repository. To update:

```bash
sh scripts/sync-docs.sh
```

Or trigger the **Auto-Sync** workflow on GitHub Actions (runs daily at 04:00 UTC).

## Tools Reference

For detailed per-tool documentation, see [references/tools/index.md](references/tools/index.md).

For specific tools:
- [references/tools/exec.md](references/tools/exec.md) — Exec tool deep-dive
- [references/tools/exec-approvals.md](references/tools/exec-approvals.md) — Exec approvals and allowlists
- [references/tools/browser.md](references/tools/browser.md) — Browser automation deep-dive
- [references/tools/web.md](references/tools/web.md) — Web search/fetch with multiple providers
- [references/tools/plugin.md](references/tools/plugin.md) — Plugin system (install, author, distribute)
- [references/tools/skills.md](references/tools/skills.md) — Skills system (load, config, ClawHub)
- [references/tools/acp-agents.md](references/tools/acp-agents.md) — ACP agents (Codex, Claude Code, Gemini CLI)
- [references/tools/firecrawl.md](references/tools/firecrawl.md) — Firecrawl anti-bot fallback
- [references/tools/slash-commands.md](references/tools/slash-commands.md) — Chat slash commands
- [references/tools/thinking.md](references/tools/thinking.md) — Thinking levels (/think, /verbose)
- [references/tools/clawhub.md](references/tools/clawhub.md) — ClawHub skill registry
- [references/web/tui.md](references/web/tui.md) — Terminal UI (TUI)
- [references/tools/tts.md](references/tools/tts.md) — Talk Mode and Voice Wake

**Tool profiles**: `minimal`, `coding`, `messaging`, `full` (default).

**Tool groups** (for allow/deny):

| Group | Tools Included |
|---|---|
| `group:runtime` | exec, bash, process |
| `group:fs` | read, write, edit, apply_patch |
| `group:sessions` | sessions_list/history/send/spawn, session_status |
| `group:memory` | memory_search, memory_get |
| `group:web` | web_search, web_fetch |
| `group:ui` | browser, canvas |
| `group:automation` | cron, gateway |
| `group:messaging` | message |
| `group:nodes` | nodes |
| `group:openclaw` | all built-in OpenClaw tools (excludes provider plugins) |

## Common Failure Signatures

| Error | Cause | Fix |
|---|---|---|
| `refusing to bind gateway ... without auth` | Non-loopback bind without token | Set `gateway.auth.token` or `gateway.auth.password` |
| `another gateway instance is already listening` / `EADDRINUSE` | Port conflict | `openclaw gateway --force` or change port |
| `Gateway start blocked: set gateway.mode=local` | Local mode not enabled | Set `gateway.mode="local"` |
| `unauthorized` / reconnect loop | Token/password mismatch | Check `OPENCLAW_GATEWAY_TOKEN` or config auth |
| `device identity required` | Missing device auth | Ensure client completes connect.challenge flow |
| No replies from bot | Pairing/allowlist/mention gating | Check `openclaw pairing list`, DM policy, mention patterns |
| `Embedding provider authentication failed (401)` | Placeholder API key in `.env` | Replace with real API key in `~/.openclaw/.env`, restart Gateway |
| `openclaw flows list` / `ClawFlow` references | ClawFlow is deprecated | Use `openclaw tasks list/show/cancel/audit` instead |
| `config change requires gateway restart (plugins.*)` | Plugin config can't hot-reload | Full `openclaw gateway restart` or `launchctl kickstart -k` |
| `Bootstrap failed: 5: Input/output error` | LaunchAgent plist stuck/stale | `openclaw gateway install` then `launchctl kickstart -k gui/$(id -u)/ai.openclaw.gateway` |
| `Missing env var "X" referenced at config path: ...` | `.env` missing or variable not defined | Add variable to `~/.openclaw/.env` and restart Gateway |

## Environment Variables

| Variable | Purpose |
|---|---|
| `OPENCLAW_GATEWAY_TOKEN` | Gateway auth token |
| `OPENCLAW_GATEWAY_PASSWORD` | Gateway auth password |
| `OPENCLAW_GATEWAY_PORT` | Override gateway port |
| `OPENCLAW_CONFIG_PATH` | Override config file path |
| `OPENCLAW_STATE_DIR` | Override state directory |
| `OPENCLAW_HOME` | Override home directory |
| `OPENCLAW_LOAD_SHELL_ENV` | Import shell env (set to `1`) |
| `OPENCLAW_VERBOSE` | Verbose logging |
| `OPENCLAW_LOG_FILE` | File logging path |
| `OPENCLAW_LOG_LEVEL` | Log level control |
| `OPENCLAW_SHELL` | Set by OpenClaw in exec/acp/tui runtimes |
| `BRAVE_API_KEY` | For web_search tool |
| `FIRECRAWL_API_KEY` | For Firecrawl anti-bot fallback |
| `ELEVENLABS_API_KEY` | For Talk Mode TTS |
| `ELEVENLABS_VOICE_ID` | Default voice for Talk Mode |
| `CLAWHUB_TOKEN` | ClawHub API token for CI/automation |
| `CLAWHUB_WORKDIR` | ClawHub working directory override |
| `OLLAMA_API_KEY` | For Ollama embeddings provider |
| `OPENCLAW_SKIP_CRON` | Disable cron scheduler (set to `1`) |
| `OPENCLAW_HIDE_BANNER` | Suppress banner output |
| `OPENCLAW_SUPPRESS_NOTES` | Suppress informational notes |
