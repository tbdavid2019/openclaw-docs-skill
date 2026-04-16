# OpenClaw Documentation Skill (Auto-Sync Version)

> [!IMPORTANT]
> ### 🤖 Instructions for AI Agent Installation / AI 助手安裝指引
>
> **English:** If a user provides you with this repository URL and asks you to "install" or "setup" this skill, follow these steps:
> 1.  **Install as a Git Checkout, Not a Copied Folder**: Run `git clone https://github.com/tbdavid2019/openclaw-docs-skill.git <skill-directory>`. Do not copy the files into a managed skills folder if you expect updates to work.
> 2.  **Prefer the Installer Script**: If shell execution is available, run `bash <skill-directory>/scripts/install-skill.sh <skill-directory>`. This keeps the installed skill as a git checkout and turns later re-runs into `git pull --ff-only`.
> 3.  **Load Skill Metadata**: Read `SKILL.md` to understand the specialized workflows and knowledge contained here.
> 4.  **Initialize Context**: Acknowledge that you now have access to the comprehensive OpenClaw documentation. **Always consult `references/SKILL_INDEX.md` first to locate specific documentation files.**
> 5.  **Do Not Run Maintenance Scripts During Normal Use**: Installing or using this skill means cloning/copying it and reading `SKILL.md` plus `references/`. **Do not run `scripts/sync-docs.sh`, `scripts/generate_index.py`, or other repo-maintenance scripts unless the user explicitly asks to refresh this repository itself.**
> 6.  **Runtime-Minimum Files**: For normal LLM usage, the important files are `SKILL.md`, `references/`, and especially `references/SKILL_INDEX.md`. Files under `scripts/`, `.github/`, `.tmp_repo/`, and `openspec/` are not required just to use the skill.
> 7.  **Hard Requirement**: If you did not run `scripts/install-skill.sh` in the final installed directory, the installation is incomplete. Do not claim success after only cloning, copying, or moving files.
>
> **繁體中文：** 如果使用者提供此倉庫網址並要求你「安裝」或「設定」此技能服務，請遵循以下步驟：
> 1.  **請用 Git checkout 安裝，不要只複製資料夾**：執行 `git clone https://github.com/tbdavid2019/openclaw-docs-skill.git <skill-directory>`。如果只是把檔案複製進某個受管目錄，之後更新通常不會成立。
> 2.  **優先使用安裝器腳本**：如果環境允許執行 shell，接著執行 `bash <skill-directory>/scripts/install-skill.sh <skill-directory>`。這會確保安裝結果維持為 git checkout，之後重跑同一支腳本就會變成 `git pull --ff-only`。
> 3.  **載入技能**：讀取 `SKILL.md` 以了解此技能的專業工作流程與知識範圍。
> 4.  **初始化環境**：確認你已具備存取完整 OpenClaw 官方文檔的能力。**每當需要查詢特定功能或維護指引時，請優先參考 `references/SKILL_INDEX.md`。**
> 5.  **一般使用時不要執行維護腳本**：安裝或使用此 skill 的意思是 clone 或複製資料夾，並讀取 `SKILL.md` 與 `references/`。**除非使用者明確要求你更新這個 repo 本身，否則不要執行 `scripts/sync-docs.sh`、`scripts/generate_index.py` 或其他維護腳本。**
> 6.  **LLM 實際需要的最小內容**：一般使用時，真正重要的是 `SKILL.md`、`references/`，以及 `references/SKILL_INDEX.md`。`scripts/`、`.github/`、`.tmp_repo/`、`openspec/` 不是使用 skill 時的必要內容。
> 7.  **硬性要求**：如果你沒有在最終安裝目錄執行 `scripts/install-skill.sh`，就不算安裝完成。不要只做 clone、copy、mv 就宣稱成功。

---

[繁體中文](README_TW.md) | English

## What is This?

This is an Agent Skill designed for AI coding assistants (like Claude with Antigravity). Once installed, the AI assistant gains deep knowledge of OpenClaw and can help you with:

- **Installation & Updates** — Install, upgrade, or migrate OpenClaw
- **Configuration** — Edit `openclaw.json`, set up models, manage secrets
- **Channel Management** — Set up WhatsApp, Telegram, Discord, Slack, iMessage, and 15+ other channels
- **Gateway Operations** — Start, stop, restart, health check, remote access
- **Multi-Agent Routing** — Configure multiple agents with isolated workspaces and sessions
- **ACP Agents** — Spawn external AI runtimes (Codex, Claude Code, Gemini CLI, 14+ harnesses)
- **Browser Automation** — Multi-profile browser control, Chrome MCP existing-session, snapshots
- **Plugin System** — Capability model, context engine plugins, SDK, hook API
- **Automation** — Cron jobs, standing orders, background tasks, webhooks, hooks
- **Security Hardening** — Audit, lock down access, manage tokens, trusted proxy, incident response
- **Troubleshooting** — Diagnose and fix common errors from CLI and Gateway

## Skill Structure

```
openclaw-docs-skill/
├── SKILL.md                     # Main entry (370 lines of expert workflows, commands, troubleshooting)
├── scripts/
│   └── sync-docs.sh             # Sync Engine — pulls latest docs from upstream
├── .github/
│   └── workflows/
│       └── auto-sync.yml        # GitHub Action — daily auto-sync at 04:00 UTC
└── references/                  # 400+ Markdown files (The Knowledge Base)
    ├── channels/                # Per-channel setup (WhatsApp, Telegram, Discord, etc.)
    ├── tools/                   # All built-in tools (Browser, Search, Exec, ACP, etc.)
    ├── plugins/                 # Plugin architecture and SDK
    ├── providers/               # 35+ model providers (Anthropic, OpenAI, Google, Ollama, etc.)
    ├── concepts/                # Core concepts: agent loop, memory, queue, streaming
    ├── gateway/                 # Gateway config, operations, security, sandboxing
    ├── security/                # Security hardening policies
    ├── nodes/                   # Nodes (iOS/Android/macOS/headless)
    ├── automation/              # Cron jobs, webhooks, background tasks, standing orders
    ├── install/                 # Installation, updating, rollback, migration, uninstall
    ├── platforms/               # Platform guides (macOS, iOS, Android, Linux, Windows)
    ├── web/                     # Web surfaces: Dashboard, Control UI, WebChat, TUI
    ├── diagnostics/             # Troubleshooting and failure walkthroughs
    └── cli/                     # CLI reference
```

## Setup for AI Agents

### For Antigravity (Claude)

Recommended install:

```bash
bash -c 'tmpdir=$(mktemp -d) && git clone https://github.com/tbdavid2019/openclaw-docs-skill.git "$tmpdir/openclaw-docs-skill" && bash "$tmpdir/openclaw-docs-skill/scripts/install-skill.sh" ~/.gemini/antigravity/skills/openclaw-docs'
```

Or, if you already cloned it into the final destination:

```bash
git clone https://github.com/tbdavid2019/openclaw-docs-skill.git ~/.gemini/antigravity/skills/openclaw-docs
bash ~/.gemini/antigravity/skills/openclaw-docs/scripts/install-skill.sh ~/.gemini/antigravity/skills/openclaw-docs
```

To update an installed checkout later:

```bash
bash ~/.gemini/antigravity/skills/openclaw-docs/scripts/install-skill.sh ~/.gemini/antigravity/skills/openclaw-docs
```

The skill will be automatically detected and triggered when you ask about OpenClaw-related tasks.

Whether an installed copy auto-refreshes depends on the host LLM platform. If the platform keeps the skill as a git checkout and allows shell execution, it can try `git pull` before use. If the platform copies files into a managed skills directory, the installed copy will not self-update unless that platform provides its own update mechanism.

If an AI assistant did not run `scripts/install-skill.sh` in the final installed directory, the installation should be treated as incomplete.

### For Other AI Assistants

The `SKILL.md` and `references/` files contain structured documentation that can be adapted for any AI assistant that supports skill/knowledge injection.

## Usage Examples

Once installed, just ask naturally:

| What You Say | What the AI Does |
|---|---|
| "Help me upgrade OpenClaw" | Runs `openclaw update`, then `openclaw doctor` to apply migrations, restarts Gateway |
| "Set up a Telegram bot" | Walks through bot token creation, `openclaw channels add`, and QR verification |
| "Gateway is not responding" | Runs diagnostic ladder: `status` → `logs` → `doctor` → `channels status --probe` |
| "Lock down my OpenClaw security" | Runs `openclaw security audit --fix`, applies hardened baseline, fixes permissions |
| "Add a second agent for work" | Creates agent, sets up workspace, configures bindings, restarts |
| "Spawn a Claude Code ACP session" | Configures `acp-agents` plugin, sets permissions, spawns bound session |
| "Attach browser to my Chrome" | Sets up browser profile with Chrome MCP existing-session driver |
| `EADDRINUSE` error | Runs `openclaw gateway --force` or helps change port in config |
| "Embedding provider 401 error" | Finds placeholder API key in `~/.openclaw/.env`, guides replacement |

## Key Commands Quick Reference

```bash
# Status & Health
openclaw status                    # Overall status
openclaw gateway status            # Gateway daemon status
openclaw doctor                    # Diagnose issues
openclaw channels status --probe   # Channel health

# Gateway Management
openclaw gateway install           # Install as system service
openclaw gateway start/stop/restart
openclaw gateway --force           # Kill existing and restart

# Configuration
openclaw config get <path>         # Read config value
openclaw config set <path> <value> # Set config value
openclaw configure                 # Interactive wizard

# Security
openclaw security audit            # Check security posture
openclaw security audit --fix      # Auto-fix issues
openclaw secrets reload            # Reload secret refs

# Channels
openclaw channels add              # Add channel (wizard)
openclaw channels login            # WhatsApp QR pairing
openclaw channels list             # Show configured channels

# Models
openclaw models set <model>        # Set default model
openclaw models status --probe     # Check auth status
```

## Updating the Documentation

This skill's `references/` folder is synced from the official OpenClaw repository. To get the latest docs:

```bash
sh scripts/sync-docs.sh
```

Or trigger the **Auto-Sync Documentation** workflow in the [GitHub Actions](https://github.com/tbdavid2019/openclaw-docs-skill/actions) tab.

The GitHub Action runs automatically every day at 04:00 UTC — no manual intervention needed.

## Documentation Source

This skill's knowledge base is built from the official [OpenClaw Documentation](https://docs.openclaw.ai/), covering:

- [Install](https://docs.openclaw.ai/install)
- [Gateway Architecture](https://docs.openclaw.ai/concepts/architecture)
- [Channels](https://docs.openclaw.ai/channels)
- [Model Providers](https://docs.openclaw.ai/providers)
- [Tools](https://docs.openclaw.ai/tools)
- [Plugin Architecture](https://docs.openclaw.ai/plugins/architecture)
- [Multi-Agent Routing](https://docs.openclaw.ai/concepts/multi-agent)
- [Security](https://docs.openclaw.ai/gateway/security)
- [Troubleshooting](https://docs.openclaw.ai/gateway/troubleshooting)
- [CLI Reference](https://docs.openclaw.ai/cli)

## Contributing

Issues and PRs welcome! Contributions that improve:
- `SKILL.md` — the agent's reasoning and diagnostic logic
- `scripts/sync-docs.sh` — the sync engine efficiency
- `references/` — curated documentation quality


```
┌─────────────────────────────────────────────────┐
│           openclaw/openclaw (官方源頭)            │
│              /docs 資料夾每日更新                  │
└────────────────────┬────────────────────────────┘
                     │ GitHub Action 每日 04:00 UTC
                     ▼
┌─────────────────────────────────────────────────┐
│    tbdavid2019/openclaw-docs-skill              │
│    400+ 個最新文件永遠保持同步                      │
└────────────────────┬────────────────────────────┘
                     │ 使用者 git clone 一次
                     ▼
┌─────────────────────────────────────────────────┐
│   LLM 本地 Skill (~/.gemini/.../openclaw-docs)  │
│   每次被呼叫 → 自動 git pull → 永遠最新           │
│   使用者無需任何手動操作                            │
└─────────────────────────────────────────────────┘

```

## License

[AGPL-3.0](LICENSE) — Any derivative work must also be open-sourced under the same license. OpenClaw documentation is sourced from the official [OpenClaw repository](https://github.com/openclaw/openclaw).

## Acknowledgments

Special thanks to **[win4r/OpenClaw-Skill](https://github.com/win4r/OpenClaw-Skill)** — the original inspiration for this project.

Their pioneering work on structuring OpenClaw knowledge as an Agent Skill showed what was possible. This repository builds on that idea by adding an **auto-sync engine** and **daily GitHub Actions** to ensure the documentation never goes stale.
