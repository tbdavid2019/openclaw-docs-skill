# Cli documentation catalog

Exact OpenClaw CLI command reference.

Open only the entries relevant to the current request. Start with at most three documents.

- [Uninstall and update plugins](../cli/plugins/uninstall-and-update.md) — What `plugins uninstall` removes, and how `plugins update` resolves sources, channels, pins, and integrity drift. Read when: You want to remove a plugin and know exactly what uninstall touches; You want to update a plugin and understand pin, channel, and integrity rules.
- [Uninstall CLI](../cli/uninstall.md) — CLI reference for `openclaw uninstall` (remove gateway service + local data). Read when: You want to remove the gateway service and/or local state; You want a dry-run first.
- [Update](../cli/update.md) — CLI reference for `openclaw update` (updates, repair, and recovery cleanup). Read when: You want to update a source checkout safely; You are debugging `openclaw update` output or options; You want to inspect or retire migration recovery originals after an update; You need to understand `--update` shorthand behavior.
- [Update repair and recovery](../cli/update/repair-and-recovery.md) — Recovering from a failed `openclaw update`, plus the `update repair` and `update cleanup` subcommands. Read when: An update or repair failed and you need a working install back; You are running `openclaw update repair` and need its flags or exit codes; You want to inspect or retire migration recovery originals after an update.
- [Update status and run history](../cli/update/status-and-history.md) — `openclaw update status` plus the durable run ledger, reports, and artifacts every update writes. Read when: You want to check whether an update is available before applying one; You are inspecting a past update run, its reports, or its artifacts.
- [Voicecall](../cli/voicecall.md) — CLI reference for `openclaw voicecall` (voice-call plugin command surface). Read when: You use the voice-call plugin and want every CLI entry point; You need flag tables and defaults for setup, smoke, call, continue, speak, dtmf, end, status, tail, latency, expose, and start.
- [Webhooks](../cli/webhooks.md) — CLI reference for `openclaw webhooks` (Gmail Pub/Sub setup and runner). Read when: You want to wire Gmail Pub/Sub events into OpenClaw; You need the full flag list and default values.
- [Wiki](../cli/wiki.md) — CLI reference for `openclaw wiki` (memory-wiki vault status, search, compile, lint, apply, bridge, ChatGPT import, and Obsidian helpers). Read when: You want to use the memory-wiki CLI; You are documenting or changing `openclaw wiki`.
- [Workboard CLI](../cli/workboard.md) — CLI reference for `openclaw workboard` cards, dispatch, and worker runs. Read when: You want to inspect or create Workboard cards from the terminal; You want to dispatch Workboard worker runs from the CLI; You are debugging Workboard CLI or slash command behavior.
- [Worker](../cli/worker.md) — Internal operator reference for the restricted cloud worker runtime. Read when: Operating or debugging gateway-launched cloud workers; Verifying worker admission, session assignment, or local tool isolation.
