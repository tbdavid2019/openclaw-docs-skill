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

The agent starts with `SKILL.md` and reads only the sections relevant to the task. Common tasks
such as Gateway health checks and Telegram setup link directly to the upstream sections.

For an exact error, CLI command, or configuration key, the agent searches the relevant local
topic directory first and expands the search as needed. Broad questions start at a topic
catalog. The compact `references/SKILL_INDEX.md` helps find a catalog when the topic is unclear.
Catalog entries use upstream `title`, `summary`, and `read_when` metadata to narrow the search
to at most three candidate documents at a time.

## Install

### Via npm

Once the npm package is published, run this command from your project with Node.js 22.20 or later
and Git. The default Codex destination is `.agents/skills/openclaw-docs`.

```bash
npx -y openclaw-docs-skill@latest
```

Use `--global` to install in your user directory or `--agent` to select another host.
[Supported agents](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)

```bash
npx -y openclaw-docs-skill@latest --global
npx -y openclaw-docs-skill@latest --agent openclaw
```

Re-run the same command with the same options to refresh an npm-managed installation. The
installer fetches the latest synchronized GitHub snapshot, verifies it, and prints the installed
path, skill repository commit, and upstream documentation commit. Daily GitHub syncs are
available immediately to new installs and explicit updates. The agent reads the installed
snapshot locally during normal use.

### Via SkillHub (CLI)

Install directly using [SkillHub](https://skills.palebluedot.live/owner/tbdavid2019):

```bash
# Install for Codex
npx skillhub install tbdavid2019/openclaw-docs-skill/openclaw-docs --platform codex

# Install to current project
npx skillhub install tbdavid2019/openclaw-docs-skill/openclaw-docs --project

# Or install globally
npx skillhub install tbdavid2019/openclaw-docs-skill/openclaw-docs -g
```

### Via Git Clone

Use Git checkout mode if you want a working copy of the repository. Replace the destination with
the skills directory used by your agent.

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

1. Identify the host and whether the user wants a project or global installation. Check how any
   existing installation is managed. Keep its original update method and resolve any conflicting
   destination with the user.
2. For a new npm installation, or to refresh one, run `npx -y openclaw-docs-skill@latest` with
   the appropriate `--agent` and `--global` options. For a SkillHub-managed copy, use SkillHub.
3. For a Git checkout, verify the repository and destination. You MUST run the installer
   `bash <skill-directory>/scripts/install-skill.sh` after cloning or to update an existing
   checkout. The installer must complete `git pull --ff-only` and validation successfully.
4. Read the installed `SKILL.md`. Do not run `scripts/sync-docs.sh` or
   `scripts/generate_index.py` as part of installation. They are maintainer tools; an installation
   must use the repository's committed snapshot.
5. Verify that the destination contains `SKILL.md`, `agents/openai.yaml`,
   `references/SOURCE.json`, `references/SKILL_INDEX.md`, and `references/_catalog/`.
6. Read `references/SOURCE.json`, then report the absolute installation directory, the Skill
   repository commit, and the upstream documentation commit. The installer prints all three.
7. Tell the user to reload or restart the host if it discovers skills only at startup. Then test
   discovery with: `Use $openclaw-docs to explain how to check OpenClaw Gateway health.`
8. Do not claim installation success until installation or update, validation, commit reporting, and any required
   reload instruction have completed. Never print credentials or unrelated configuration values.

Copy-paste installation request:

```text
Install the following repository as the OpenClaw documentation skill:
https://github.com/tbdavid2019/openclaw-docs-skill

Follow README.md's "AI Agent Installation Contract":
1. Identify my host and install at the appropriate scope. Prefer the npm installer for a new installation.
2. For an existing installation, use the same method that installed it.
3. Read SKILL.md.
4. Verify references/SOURCE.json, references/SKILL_INDEX.md, and references/_catalog/.
5. Report the installation directory, Skill repository commit, and upstream documentation commit.

After installation, test it with:
Use $openclaw-docs and the locally synchronized official OpenClaw documentation to explain how
to check Gateway health. Cite the local document paths and distinguish documentation facts from
your inferences.

The GitHub repository is synchronized daily. Re-run the matching installer to refresh the local snapshot.
```

## Repository structure

```text
openclaw-docs-skill/
├── SKILL.md
├── package.json
├── agents/openai.yaml
├── scripts/
│   ├── install-npm.mjs
│   ├── install-skill.sh
│   ├── sync-docs.sh
│   └── generate_index.py
├── tests/test_repo.py
├── .github/workflows/auto-sync.yml
├── .github/workflows/publish-npm.yml
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

### Release the npm installer

Daily documentation updates are served from GitHub. Create a new npm version when the
installer changes. Use `npm ci --ignore-scripts` and `npm pack` to build the package locally.
For the first public release, test the tarball and run `npm publish <tarball> --access public`
with a verified npm account.

For the next release, update the version and lockfile first. When you are ready to publish,
register the workflow as a trusted publisher with npm CLI 11.15 or later:

```bash
npm trust github openclaw-docs-skill --repo tbdavid2019/openclaw-docs-skill \
  --file publish-npm.yml --allow-publish
```

Push a tag matching `v<version>` to test and publish the packed CLI. The first successful
OIDC publish must complete within two days of creating the trust configuration.
[npm Trusted Publishing](https://docs.npmjs.com/trusted-publishers/)

## Documentation source

Content is synchronized from the official
[OpenClaw repository](https://github.com/openclaw/openclaw) and
[OpenClaw documentation](https://docs.openclaw.ai/).

## License

[AGPL-3.0](LICENSE). OpenClaw documentation remains subject to its upstream licensing terms.

## Acknowledgments

Inspired by [win4r/OpenClaw-Skill](https://github.com/win4r/OpenClaw-Skill).
