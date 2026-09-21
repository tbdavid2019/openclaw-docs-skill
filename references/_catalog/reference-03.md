# Reference documentation catalog

Documentation under `reference/`.

Open only the entries relevant to the current request. Start with at most three documents.

- [Top-level stages](../reference/full-release-validation/stages.md) — The Full Release Validation umbrella stage matrix, evidence reuse, artifact producers, and decision states. Read when: Reading the umbrella stage matrix; Debugging a Release Decision or Diagnostic Drain state.
- [Transcript hygiene](../reference/transcript-hygiene.md) — Reference: provider-specific transcript sanitization and repair rules. Read when: You are debugging provider request rejections tied to transcript shape; You are changing transcript sanitization or tool-call repair logic; You are investigating tool-call id mismatches across providers.
- [USER template](../reference/templates/USER.md) — Durable user preference and profile directives. Read when: Bootstrapping a workspace manually.
- [USER.dev template](../reference/templates/USER.dev.md) — Dev agent user profile (C-3PO). Read when: Using the dev gateway templates; Updating the default dev agent identity.
- [Versioning contract](../reference/database-schemas/versioning.md) — How OpenClaw records schema versions, when a bump is required, and how updaters cross one. Read when: Deciding whether a storage change needs a schema-version bump; Diagnosing a refused update or a newer schema version error.
- [Writer operating program](../reference/templates/roles/writer/workspace/AGENTS.md)
- [Writer soul](../reference/templates/roles/writer/CLAW.md)
