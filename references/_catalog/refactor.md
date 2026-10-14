# Refactor documentation catalog

Documentation under `refactor/`.

Open only the entries relevant to the current request. Start with at most three documents.

- [Conversation transcript ownership](../refactor/conversation-transcript-ownership.md) — Proposed single owner for transcript entries: every visible message is in its chat's model history once. Read when: Changing where automation results, message-tool sends, or alerts are written into session transcripts; Adding a new path that posts messages into a chat; Reviewing cron session targets or delivery routing.
- [Transcript event bytes](../refactor/transcript-event-bytes.md) — Encode-once transcript events: ownership, transport copies, and the first broadcast slice. Read when: Changing transcript ingestion, replicas, worker transport, or subscriber encoding; Reducing transcript allocation without changing stored formats.
- [Worker-owned cron](../refactor/cron-worker-owned.md) — Proposed worker-owned cron scheduling with committed run requests and a small launcher. Read when: Simplifying cron scheduling and update reliability.
