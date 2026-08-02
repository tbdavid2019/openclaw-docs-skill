# General documentation catalog

Top-level concepts and cross-cutting documentation.

Open only the entries relevant to the current request. Start with at most three documents.

- [Agent runtime architecture](../agent-runtime-architecture.md) — How OpenClaw structures the built-in agent runtime: code layout, boundaries, resource manifests, and runtime selection.
- [Auth credential semantics](../auth-credential-semantics.md) — Canonical credential eligibility and resolution semantics for auth profiles. Read when: Working on auth profile resolution or credential routing; Debugging model auth failures or profile order.
- [Brave search](../brave-search.md) — Redirect to /tools/brave-search.
- [CI pipeline](../ci.md) — CI job graph, scope gates, release umbrellas, and local command equivalents. Read when: You need to understand why a CI job did or did not run; You are debugging a failing GitHub Actions check; You are coordinating a release validation run or rerun; You are changing ClawSweeper dispatch or GitHub activity forwarding.
- [Date and time](../date-time.md) — Date and time handling across envelopes, prompts, tools, and connectors. Read when: You are changing how timestamps are shown to the model or users; You are debugging time formatting in messages or system prompt output.
- [Docs Guide](../AGENTS.md)
- [Docs map source](../docs_map.md) — Generated heading map for OpenClaw docs pages. Read when: Finding which docs page covers a topic before reading the page.
- [Linux server](../vps.md) — Run OpenClaw on a Linux server or cloud VPS — provider picker, architecture, and tuning. Read when: You want to run the Gateway on a Linux server or cloud VPS; You need a quick map of hosting guides; You want generic Linux server tuning for OpenClaw.
- [Logging](../logging.md) — File logs, console output, CLI tailing, and the Control UI Logs tab. Read when: You need a beginner-friendly overview of OpenClaw logging; You want to configure log levels, formats, or redaction; You are troubleshooting and need to find logs quickly.
- [Network](../network.md) — Network hub: gateway surfaces, pairing, discovery, and security. Read when: You need the network architecture + security overview; You are debugging local vs tailnet access or pairing; You want the canonical list of networking docs.
- [OpenClaw](../index.md) — OpenClaw is a multi-channel gateway for AI agents that runs on any OS. Read when: Introducing OpenClaw to newcomers.
- [OpenClaw agent runtime workflow](../openclaw-agent-runtime.md) — Developer workflow for OpenClaw agent runtime: build, test, and live validation. Read when: Working on OpenClaw agent runtime code or tests; Running agent-runtime lint, typecheck, and live test flows.
- [OpenProse](../prose.md) — OpenProse is a markdown-first workflow format for multi-agent AI sessions. In OpenClaw it ships as a plugin with a /prose slash command and a skill pack. Read when: You want to run or write .prose workflow files; You want to enable the OpenProse plugin; You need to understand how OpenProse maps to OpenClaw primitives.
- [Perplexity search](../perplexity.md) — Redirect to /tools/perplexity-search.
- [Text-to-speech](../tts.md) — Redirect to /tools/tts.
