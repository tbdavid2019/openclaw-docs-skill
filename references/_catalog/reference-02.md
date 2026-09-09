# Reference documentation catalog

Documentation under `reference/`.

Open only the entries relevant to the current request. Start with at most three documents.

- [Run tests locally](../reference/test/local.md) — Routine local test order, the core test commands, and the local PR gate. Read when: You are running or fixing tests on your own machine; You need the local land and gate command list.
- [Secret Placeholder Conventions](../reference/secret-placeholder-conventions.md) — Secret-scanner-safe placeholder conventions for docs and examples. Read when: Writing docs that include tokens, API keys, or credential snippets; Updating examples that may be scanned by secret-detection tooling.
- [SecretRef credential surface](../reference/secretref-credential-surface.md) — Canonical supported vs unsupported SecretRef credential surface. Read when: Verifying SecretRef credential coverage; Auditing whether a credential is eligible for `secrets configure` or `secrets apply`; Verifying why a credential is outside the supported surface.
- [Session management deep dive](../reference/session-management-compaction.md) — Deep dive: session store + transcripts, lifecycle, and (auto)compaction internals. Read when: You need to debug session ids, transcript events, or session row fields; You are changing auto-compaction behavior or adding "pre-compaction" housekeeping; You want to implement memory flushes or silent system turns.
- [SOUL.dev template](../reference/templates/SOUL.dev.md) — Dev agent soul (C-3PO). Read when: Using the dev gateway templates; Updating the default dev agent identity.
- [SOUL.md template](../reference/templates/SOUL.md) — Workspace template for SOUL.md. Read when: Bootstrapping a workspace manually.
- [Test performance and benchmarks](../reference/test/performance.md) — Import profiling, CPU and heap profiles, shard timings, and benchmark scripts. Read when: You are profiling a slow test run; You need a startup, gateway, or model latency benchmark.
- [Test runner internals](../reference/test/runner-internals.md) — Shared build locks, isolated test state and homes, and JSON report merging. Read when: A run leaked state, retained a lock, or lost a report; You need machine-readable results from a multi-project run.
- [Tests](../reference/test.md) — Index of the OpenClaw testing reference, one page per reader job. Read when: Running or fixing tests.
- [Token use and costs](../reference/token-use.md) — How OpenClaw builds prompt context and reports token usage + costs. Read when: Explaining token usage, costs, or context windows; Debugging context growth or compaction behavior.
- [TOOLS.md retired](../reference/templates/TOOLS.md) — Retired TOOLS.md workspace template. Read when: Bootstrapping a workspace manually.
- [Top-level stages](../reference/full-release-validation/stages.md) — The Full Release Validation umbrella stage matrix, evidence reuse, artifact producers, and decision states. Read when: Reading the umbrella stage matrix; Debugging a Release Decision or Diagnostic Drain state.
- [Transcript hygiene](../reference/transcript-hygiene.md) — Reference: provider-specific transcript sanitization and repair rules. Read when: You are debugging provider request rejections tied to transcript shape; You are changing transcript sanitization or tool-call repair logic; You are investigating tool-call id mismatches across providers.
- [USER template](../reference/templates/USER.md) — Durable user preference and profile directives. Read when: Bootstrapping a workspace manually.
- [USER.dev template](../reference/templates/USER.dev.md) — Dev agent user profile (C-3PO). Read when: Using the dev gateway templates; Updating the default dev agent identity.
