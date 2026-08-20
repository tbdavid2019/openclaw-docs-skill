# Refactor documentation catalog

Documentation under `refactor/`.

Open only the entries relevant to the current request. Start with at most three documents.

- [ACP lifecycle refactor](../refactor/acp.md) — Current ACP session ownership and ACPX process-lease migration status. Read when: Refactoring ACP session lifecycle or ACPX process cleanup; Debugging ACPX orphan processes, PID reuse, or multi-gateway cleanup safety; Changing sessions_list visibility for spawned ACP or subagent sessions; Designing ownership metadata for background tasks, ACP sessions, or process leases.
- [Database-first state refactor](../refactor/database-first.md) — Migration plan for making SQLite the primary durable state and cache layer while keeping config file-backed. Read when: Moving OpenClaw runtime data, cache, transcripts, task state, or scratch files into SQLite; Designing doctor migrations from legacy JSON or JSONL files; Changing backup, restore, VFS, or worker storage behavior; Removing session locks, pruning, truncation, or JSON compatibility paths.
- [Multi-surface operator approvals](../refactor/operator-approvals.md) — Design for durable, deep-linkable approvals across Control UI, native apps, channels, and parent sessions. Read when: Changing exec or plugin approval lifecycle, storage, protocol, or authorization; Adding approval links or native approval controls to a channel; Projecting child-session approvals into parent or orchestrator views.
