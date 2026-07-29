# OpenClaw Documentation Skill

[繁體中文](README_TW.md) | English

This repository turns the official OpenClaw documentation into an auto-updated Agent Skill.
GitHub Actions mirrors the upstream `docs/` directory daily, records the exact source revision,
and generates compact topic catalogs for progressive disclosure.

## What the skill helps with

- Installation, updates, migrations, and deployments
- Gateway configuration, operation, networking, and security
- Messaging channels such as Telegram, WhatsApp, Discord, Slack, LINE, and Signal
- Model providers, authentication, failover, and local models
- Agents, sessions, memory, tools, plugins, nodes, and automation
- CLI errors and symptom-first troubleshooting

## Progressive disclosure

The full documentation set is intentionally not injected into the model context.

```text
SKILL.md
  → compact references/SKILL_INDEX.md
  → one references/_catalog/<topic>.md
  → at most 1–3 relevant documents
  → only the relevant sections
```

Exact errors, CLI commands, and configuration keys bypass the catalog and are searched directly
across `references/`. The generated catalogs use each upstream page's `title`, `summary`, and
`read_when` metadata.

## Install

Install as a Git checkout so it can be updated reliably. Replace the destination with the skills
directory used by your agent:

```bash
git clone https://github.com/tbdavid2019/openclaw-docs-skill.git \
  ~/.gemini/antigravity/skills/openclaw-docs
```

For Codex, a typical destination is:

```bash
git clone https://github.com/tbdavid2019/openclaw-docs-skill.git \
  ~/.codex/skills/openclaw-docs
```

The installer can also clone into a new destination when run from another checkout:

```bash
bash openclaw-docs-skill/scripts/install-skill.sh <skill-directory>
```

To update an installed checkout later:

```bash
bash <skill-directory>/scripts/install-skill.sh
```

The public repository is synchronized daily. An installed checkout does not perform a network
update on every question; it changes only when the installer or `git pull` is explicitly run.

If a host platform copies skills into a managed directory, use that platform's update mechanism.
The copied snapshot remains usable but cannot update itself as a Git checkout.

## Repository structure

```text
openclaw-docs-skill/
├── SKILL.md
├── agents/openai.yaml
├── scripts/
│   ├── install-skill.sh
│   ├── sync-docs.sh
│   └── generate_index.py
├── tests/test_repo.py
├── .github/workflows/auto-sync.yml
└── references/
    ├── SOURCE.json
    ├── SKILL_INDEX.md
    ├── _catalog/
    └── <official OpenClaw documentation>
```

`references/SOURCE.json` identifies the upstream repository, commit, commit date, and document
count represented by the current snapshot.

## Maintainer workflow

Refresh from the official repository:

```bash
sh scripts/sync-docs.sh
```

Validate the skill and generated artifacts:

```bash
python3 -m unittest -v tests/test_repo.py
python3 scripts/generate_index.py --check
```

The sync is staged and validated before `references/` is replaced. A failed fetch, low document
count, missing required page, or invalid generated index leaves the current references intact.

Do not hand-edit synchronized documents, `references/SOURCE.json`,
`references/SKILL_INDEX.md`, or `references/_catalog/`.

## Documentation source

Content is synchronized from the official
[OpenClaw repository](https://github.com/openclaw/openclaw) and
[OpenClaw documentation](https://docs.openclaw.ai/).

## License

[AGPL-3.0](LICENSE). OpenClaw documentation remains subject to its upstream licensing terms.

## Acknowledgments

Inspired by [win4r/OpenClaw-Skill](https://github.com/win4r/OpenClaw-Skill).
