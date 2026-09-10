# Gateway documentation catalog

Gateway configuration, operations, security, and networking.

Open only the entries relevant to the current request. Start with at most three documents.

- [Updates and rollbacks](../gateway/troubleshooting/updates-and-rollbacks.md) — Symptoms that appear after an update, a rollback, or a split-brain install of the Gateway. Read when: An update finished and the Gateway is down, channels are empty, or model calls return 401; Logs report a protocol mismatch, a newer-config guard, or a prepared model runtime timeout; You need to tell a version-drift problem apart from a runtime fault.
- [Usage telemetry and update checks](../gateway/telemetry.md) — What OpenClaw sends: a daily update check by default, optional anonymous feature statistics, and every privacy control. Read when: Checking what information OpenClaw sends and what it never collects; Deciding whether to share anonymous feature statistics; Enabling or disabling anonymous feature statistics; Disabling all automatic update-check requests.
- [Verify a cloud worker profile](../gateway/cloud-workers/verify-the-profile.md) — Validate config, restart the Gateway, and prove a new cloud worker profile end to end. Read when: You added or changed a cloud worker profile and want to prove it works before relying on it..
- [What doctor checks](../gateway/doctor/checks.md) — Summary of every repair, migration, and health check doctor runs. Read when: You want an overview of what doctor will touch before running it; You are deciding whether a change belongs in a doctor check.
- [What gets sandboxed](../gateway/sandboxing/what-gets-sandboxed.md) — Which tool calls move into the sandbox and which stay on the Gateway host. Read when: You want to know exactly which execution moves into the sandbox..
- [Worker setup and bundle installation](../gateway/cloud-workers/setup-and-bundle-installation.md) — The idempotent setup command, Gateway-prepared runtime archives, and building a custom node package. Read when: You are writing a profile setup command, or you need a custom node distribution..
- [Workspace access](../gateway/sandboxing/workspace-access.md) — The none, ro, and rw workspace access modes, the role-required cap, and skill mirroring. Read when: You are deciding what the sandbox can see of the agent workspace..
- [Workspace tips and Dreams UI actions](../gateway/doctor/workspace-and-dreams.md) — Config write, workspace tips, repointed aliases, and the Control UI Dreams actions. Read when: Doctor reports a repointed workspace alias or a workspace tip; You are using the Control UI Dreams backfill, reset, or clear actions.
