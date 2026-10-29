# Reference documentation catalog

Documentation under `reference/`.

Open only the entries relevant to the current request. Start with at most three documents.

- [Silent turns and the memory flush](../reference/session-management-compaction/housekeeping.md) — The NO_REPLY silent-turn contract and the pre-compaction memory flush configuration. Read when: You want to implement memory flushes or silent system turns; Tuning agents.defaults.compaction.memoryFlush.
- [SOUL.dev template](../reference/templates/SOUL.dev.md) — Dev agent soul (C-3PO). Read when: Using the dev gateway templates; Updating the default dev agent identity.
- [SOUL.md template](../reference/templates/SOUL.md) — Workspace template for SOUL.md. Read when: Bootstrapping a workspace manually.
- [State schema history](../reference/database-schemas/state-schema-history.md) — Shared state database schema versions, their changes, and their first releases. Read when: Looking up which release first shipped a state schema version; Reading the per-version notes for a recent state schema change.
- [Storage changes and release preflight](../reference/database-schemas/storage-changes.md) — Proposing a persistent-store change, the review checkpoint, and preflighting a target release. Read when: Proposing a SQLite or persistent-store change, or another database backend; Preflighting a copied state database against a target release before activation.
- [Store maintenance and retention](../reference/session-management-compaction/maintenance.md) — The session.maintenance keys, disk-budget cleanup tiers, cron run retention, and the SQLite downgrade path. Read when: Tuning the per-agent session disk budget or retention cutoffs; Running openclaw sessions cleanup, or downgrading after the SQLite flip.
- [Team immutable update design](../reference/team-immutable-update-design.md) — Immutable update design: installation, preparation, native activation, and retained recovery contracts. Read when: Designing native updates for an installation with sealed release directories; Reviewing the Team deployment controller cutover.
- [Test performance and benchmarks](../reference/test/performance.md) — Import profiling, CPU and heap profiles, shard timings, and benchmark scripts. Read when: You are profiling a slow test run; You need a startup, gateway, or model latency benchmark.
- [Test runner internals](../reference/test/runner-internals.md) — Shared build locks, isolated test state and homes, and JSON report merging. Read when: A run leaked state, retained a lock, or lost a report; You need machine-readable results from a multi-project run.
- [Tests](../reference/test.md) — Index of the OpenClaw testing reference, one page per reader job. Read when: Running or fixing tests.
- [Token use and costs](../reference/token-use.md) — How OpenClaw builds prompt context and reports token usage + costs. Read when: Explaining token usage, costs, or context windows; Debugging context growth or compaction behavior.
- [TOOLS.md retired](../reference/templates/TOOLS.md) — Retired TOOLS.md workspace template. Read when: Bootstrapping a workspace manually.
- [Top-level stages](../reference/full-release-validation/stages.md) — The Full Release Validation umbrella stage matrix, evidence reuse, artifact producers, and decision states. Read when: Reading the umbrella stage matrix; Debugging a Release Decision or Diagnostic Drain state.
- [Transcript hygiene](../reference/transcript-hygiene.md) — Reference: provider-specific transcript sanitization and repair rules. Read when: You are debugging provider request rejections tied to transcript shape; You are changing transcript sanitization or tool-call repair logic; You are investigating tool-call id mismatches across providers.
- [USER template](../reference/templates/USER.md) — Durable user preference and profile directives. Read when: Bootstrapping a workspace manually.
- [USER.dev template](../reference/templates/USER.dev.md) — Dev agent user profile (C-3PO). Read when: Using the dev gateway templates; Updating the default dev agent identity.
- [Versioning contract](../reference/database-schemas/versioning.md) — How OpenClaw records schema versions, when a bump is required, and how updaters cross one. Read when: Deciding whether a storage change needs a schema-version bump; Diagnosing a refused update or a newer schema version error.
- [Writer operating program](../reference/templates/roles/writer/workspace/AGENTS.md)
- [Writer soul](../reference/templates/roles/writer/CLAW.md)
