# Plan documentation catalog

Documentation under `plan/`.

Open only the entries relevant to the current request. Start with at most three documents.

- [Channel presentation refactor plan](../plan/ui-channels.md) — Decouple semantic message presentation from channel native UI renderers. Read when: Refactoring channel message UI, interactive payloads, or native channel renderers; Changing message tool capabilities, delivery hints, or cross-context markers; Debugging Discord Carbon import fanout or channel plugin runtime laziness.
- [Cloud workers historical plan](../plan/cloud-workers.md) — Historical design record for cloud workers before convergence onto node-backed worker turns. Read when: Reviewing the design history behind cloud worker provisioning and session placement; Comparing the superseded SSH reverse-tunnel proposal with the current node-backed architecture.
- [Computer use plan](../plan/computer-use.md) — Default background computer use via a two-provider seam (CUA + Peekaboo) behind one typed computer.act v2 contract, app-owned TCC, cloud-gateway/multi-node ready. Read when: Implementing or reviewing computer.act v2, the node provider seam, or the CUA/Peekaboo adapters; Changing macOS embedded driver spawning, provider selection UX, or managed driver artifacts; Extending Peekaboo or CUA integration surfaces.
- [Runners plan](../plan/runners.md) — Everything is a node — one placement model where paired machines and cloud boxes host sessions through the worker admission path; clients attach to sessions, never to runners. Read when: Designing or reviewing where sessions run (gateway, device, cloud); Changing the Where picker, device pairing, node onboarding, or worker dispatch surfaces; Naming anything around sessions, devices, nodes, or placement.
