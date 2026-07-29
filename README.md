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

After a direct clone, run the installer once to pull with fast-forward-only semantics, validate the
snapshot, and print its commits:

```bash
bash <skill-directory>/scripts/install-skill.sh
```

The installer can instead clone into a new destination when run from another checkout:

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

## AI Agent Installation Contract

When a user gives you this repository URL and asks you to install the skill:

1. Detect the host and resolve its actual skills directory before writing. For Codex, prefer
   `$CODEX_HOME/skills/openclaw-docs` when `CODEX_HOME` is set; otherwise use
   `~/.codex/skills/openclaw-docs`. A typical Antigravity destination is
   `~/.gemini/antigravity/skills/openclaw-docs`. For another host, inspect its configuration or
   ask the user instead of guessing.
2. Inspect the destination. If it does not exist, clone this repository with the final directory
   name `openclaw-docs`. If it is already this repository's Git checkout, keep it. Do not overwrite
   a non-Git directory; explain the conflict and ask the user how to proceed.
3. You MUST run the installer before verification:
   `bash <skill-directory>/scripts/install-skill.sh`. For an existing checkout, the installer MUST
   successfully complete `git pull --ff-only`; a pull or validation failure means the installation
   or update failed. Run the installer after a new clone as well so the same validation is applied.
4. Read the installed `SKILL.md`. Do not run `scripts/sync-docs.sh` or
   `scripts/generate_index.py` as part of installation. They are maintainer tools; an installation
   must use the repository's committed snapshot.
5. Verify that the destination contains `SKILL.md`, `agents/openai.yaml`,
   `references/SOURCE.json`, `references/SKILL_INDEX.md`, and `references/_catalog/`.
6. Read `references/SOURCE.json`, then report the absolute installation directory, the Skill
   repository commit, and the upstream documentation commit. The installer prints all three.
7. Tell the user to reload or restart the host if it discovers skills only at startup. Then test
   discovery with: `Use $openclaw-docs to explain how to check OpenClaw Gateway health.`
8. Do not claim installation success until pull, validation, commit reporting, and any required
   reload instruction have completed. Never print credentials or unrelated configuration values.

Copy-paste installation request:

```text
Install the following repository as the OpenClaw documentation skill:
https://github.com/tbdavid2019/openclaw-docs-skill

Follow README.md's "AI Agent Installation Contract":
1. Clone it into your skills directory with the final directory name openclaw-docs.
2. Run scripts/install-skill.sh. An existing checkout must complete git pull --ff-only.
3. Read SKILL.md.
4. Verify references/SOURCE.json, references/SKILL_INDEX.md, and references/_catalog/.
5. Report the installation directory, Skill repository commit, and upstream documentation commit.

After installation, test it with:
Use $openclaw-docs and the locally synchronized official OpenClaw documentation to explain how
to check Gateway health. Cite the local document paths and distinguish documentation facts from
your inferences.

The GitHub repository is synchronized daily, but an installed checkout does not update itself.
Re-run the installer, which performs git pull --ff-only, before relying on the latest snapshot.
```

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
