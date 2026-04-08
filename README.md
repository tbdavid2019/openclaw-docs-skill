# OpenClaw Documentation Skill (Auto-Sync Version)

[繁體中文](README_TW.md) | English

A high-performance **Agent Skill** for [OpenClaw](https://github.com/openclaw/openclaw), pre-loaded with the latest official documentation. Unlike static skills, this version includes a sync engine to keep your AI assistant's knowledge always up-to-date.

## Key Features
- **Always Current**: Syncs directly from the official OpenClaw repository's `/docs` folder.
- **Deep Knowledge**: Covering 400+ MD files across installation, channels, tools, and architecture.
- **Agent Optimized**: Structured for AI Coding Assistants (like Claude + Antigravity) to find answers rapidly.

## Skill Structure
```
openclaw-docs-skill/
├── SKILL.md             # Main entry point (Agent instructions & roadmap)
├── scripts/             
│   └── sync-docs.sh     # The Sync Engine (Run to update references)
└── references/          # 400+ Markdown files (The actual Knowledge Base)
    ├── getting-started/ # Installation & Onboarding
    ├── channels/        # WhatsApp, Telegram, Discord, etc.
    ├── tools/           # Browser, Search, Code, Media tools
    └── advanced/        # Plugins, Architecture, Memory, etc.
```

## Setup for AI Agents
If you are using **Antigravity (Claude)**, follow these steps:

1. **Clone this repository** to your local machine:
   ```bash
   git clone https://github.com/tbdavid2019/openclaw-docs-skill.git
   ```

2. **Register the skill**:
   Copy the folder to your agent's skills directory:
   ```bash
   cp -r openclaw-docs-skill ~/.gemini/antigravity/skills/openclaw-docs
   ```

3. **Verify**:
   Ask the agent: *"What are the latest requirements for setting up a WhatsApp channel in OpenClaw?"*

## Updating the Documentation
This is the most important part. To ensure your Agent has the latest information (new features, changed APIs), run:
```bash
sh scripts/sync-docs.sh
```
This script uses `sparse-checkout` to pull the latest changes from the official repo without downloading thousands of unnecessary files.

## Contributing
Since this repository is a documentation skill, contributions that improve the `SKILL.md` (the agent's reasoning guide) or the `sync-docs.sh` (the performance engine) are highly welcome!

## License
AGPL-3.0 License. OpenClaw documentation is sourced from the official [OpenClaw repository](https://github.com/openclaw/openclaw).
