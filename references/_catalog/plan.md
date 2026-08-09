# Plan documentation catalog

Documentation under `plan/`.

Open only the entries relevant to the current request. Start with at most three documents.

- [Channel presentation refactor plan](../plan/ui-channels.md) — Decouple semantic message presentation from channel native UI renderers. Read when: Refactoring channel message UI, interactive payloads, or native channel renderers; Changing message tool capabilities, delivery hints, or cross-context markers; Debugging Discord Carbon import fanout or channel plugin runtime laziness.
- [Cloud workers plan](../plan/cloud-workers.md) — Run agent sessions on ephemeral SSH-reachable machines with gateway-proxied inference and live sidebar streaming. Read when: Designing or implementing cloud worker provisioning, worker mode, or session handoff; Changing environments.*, the worker protocol, transcript ingestion, or inference proxy RPCs; Reviewing security posture of remote agent execution.
- [Path 3 SQLite session artifact family](../plan/path3-sqlite-session-artifact-family.md) — Path 3 plan for archiving all SQLite transcript artifacts that belong to a session. Read when: You are implementing clawdbot-d63.2 / clawdbot-04b; You are touching SQLite session retention, reset, delete, or agent-deletion archival; You need to distinguish SQLite-era artifact families from legacy JSONL sidecars.
- [Runners plan](../plan/runners.md) — One placement model for sessions — the gateway, paired devices, and cloud boxes are all runners; clients attach to sessions, never to runners. Read when: Designing or reviewing where sessions run (gateway, device, cloud); Changing the Where picker, device pairing, or worker dispatch surfaces; Naming anything around sessions, devices, or placement.
- [Swarms — agent fan-out and orchestration in code mode](../plan/swarms.md)
