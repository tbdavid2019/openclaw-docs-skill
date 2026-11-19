---
name: openclaw-docs
description: Find authoritative guidance for installing, configuring, operating, securing, and troubleshooting OpenClaw, including channels, model providers, Gateway operations, tools, plugins, automation, nodes, multi-agent routing, and CLI errors. Use for any question or maintenance task involving an OpenClaw installation, `openclaw` CLI command, Gateway daemon, configuration key, or integration.
---

# OpenClaw documentation

Use the synchronized official documentation as the source of truth. Keep context small by
loading only the files and sections needed for the current request.

## Establish the version boundary

1. Read `references/SOURCE.json` when provenance or freshness matters.
2. For operational work, obtain `openclaw --version` when it is available and relevant.
3. Treat the references as documentation for the recorded upstream `main` revision. Flag a
   possible version mismatch when the installed OpenClaw version is older.
4. Never invent a command, flag, configuration key, default, or migration step. Search the
   references and state uncertainty when the documentation does not establish the answer.

Do not update the installed skill during ordinary questions. Use the local snapshot without
blocking the user. Refresh only when the user asks to install or update the skill.

## Find documentation progressively

Resolve `references/` relative to this `SKILL.md`. It lives in the installed skill directory,
which may differ from the current project. Choose the narrowest route below.

### Exact error, command, or configuration key

Search the relevant topic directory first when the topic is known. Start with the exact error,
full command or configuration key, or distinctive log text. This command finds Gateway matches.

```bash
rg -l -i -F --glob '*.md' --glob '*.mdx' -- 'openclaw gateway status' "$skill_dir/references/gateway"
```

Set `skill_dir` to the directory containing this `SKILL.md`. Use the host's file-search
tool when `rg` is unavailable. Start with up to three matching paths and read only the relevant
sections. Expand to the related topic or the full reference tree if needed. Skip generated
`_catalog/` pages during exact searches. Include `releases/` first for version, migration, or
regression questions and expand into it as needed for other queries.

### Common tasks

| Task | Start with |
|---|---|
| Get started with OpenClaw | [Getting started → Quick setup](references/start/getting-started.md#quick-setup) |
| Check Gateway health | [Health checks → Quick checks](references/gateway/health.md#quick-checks) |
| Set up Telegram | [Telegram setup → Quick setup](references/channels/telegram/setup.md#quick-setup) |

Open the linked section directly. If the page or heading has moved in the local snapshot,
search its topic directory or use the topic catalog below.

### Broad topic

1. For a known topic, go directly to the matching catalog below. For an unclear or cross-topic
   request, use [references/SKILL_INDEX.md](references/SKILL_INDEX.md) to choose a catalog.
2. Open the selected catalog. If it has alphabetical sections, choose one matching section.
3. Select at most three candidate documents using their `summary` and `read_when` metadata.
4. Inspect headings or search within those documents before reading long sections.
5. Expand to another document, section, or catalog only when the first candidates are insufficient.

### Topic routing

| User intent | Start with |
|---|---|
| Installation, update, migration, deployment | [install catalog](references/_catalog/install.md) |
| Gateway configuration, service, networking | [gateway catalog](references/_catalog/gateway.md) |
| Telegram, WhatsApp, Discord, Slack, LINE, or other messaging | [channels catalog](references/_catalog/channels.md) |
| Anthropic, OpenAI, Gemini, Ollama, or other models | [providers catalog](references/_catalog/providers.md) |
| Exact `openclaw` command or flag | [CLI catalog](references/_catalog/cli.md) |
| Exec, browser, web, skills, permissions, or agent tools | [tools catalog](references/_catalog/tools.md) |
| Cron, hooks, tasks, or webhooks | [automation catalog](references/_catalog/automation.md) |
| Agents, sessions, memory, routing, or architecture | [concepts catalog](references/_catalog/concepts.md) |
| Nodes or OS-specific behavior | [nodes catalog](references/_catalog/nodes.md) and [platforms catalog](references/_catalog/platforms.md) |
| Control UI, WebChat, dashboard, or TUI | [web catalog](references/_catalog/web.md) |
| Security, exposure, or incident response | [security catalog](references/_catalog/security.md) and [gateway catalog](references/_catalog/gateway.md) |
| Unclear symptom or general troubleshooting | [help catalog](references/_catalog/help.md) |

If a catalog does not exist in an older installed snapshot, search the corresponding
`references/<topic>/` directory directly.

## Diagnose from evidence

Match diagnostics to the symptom instead of running a universal command ladder.

- For Gateway reachability, inspect status, service state, and relevant Gateway logs.
- For a single channel, inspect Gateway reachability and that channel's status, policy, and
  channel-specific troubleshooting page.
- For model failures, inspect provider authentication, model resolution, and the exact provider
  error without probing unrelated channels.
- For configuration failures, identify the active config path, exact rejected key, and matching
  configuration reference.
- For update or migration failures, establish the installed version, install method, and target
  version before recommending changes.

Begin with read-only observations. Preserve exact errors and command output when searching the
documentation.

## Control state-changing actions

Treat edits, installation, updates, `--fix`, `--force`, restarts, uninstalls, credential changes,
pairing approvals, and message sends as state-changing actions.

1. Explain what will change and the likely impact.
2. Confirm the target and scope from available evidence.
3. Obtain the user's authorization when it is not already explicit.
4. Prefer previews, validation, backups, and reversible operations.
5. Re-check status after the change.

Never expose tokens, passwords, session data, auth profiles, or secrets in the response. Redact
them from copied output.

## Produce the answer

- Lead with the diagnosis or requested outcome.
- Give commands only after confirming them in the synchronized references.
- Separate documented facts from inferences.
- Mention relevant version assumptions or mismatch risks.
- Cite the local reference paths used so the user can verify the answer.
- Keep unexplored alternatives out of context unless the primary route fails.

## Maintain this skill

Run maintenance only when the user explicitly asks to refresh this repository:

```bash
sh scripts/sync-docs.sh
python3 scripts/generate_index.py --check
python3 -m unittest -v tests/test_repo.py
```

For an npm-managed installation, re-run `npx -y openclaw-docs-skill@latest` with the same
agent and scope options to refresh the local snapshot.

For an installed Git checkout, install or update with:

```bash
bash <skill-directory>/scripts/install-skill.sh <skill-directory>
```

Do not run `scripts/sync-docs.sh` or regenerate indexes during normal OpenClaw assistance.
