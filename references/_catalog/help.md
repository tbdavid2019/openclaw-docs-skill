# Help documentation catalog

Symptom-first troubleshooting and support.

Open only the entries relevant to the current request. Start with at most three documents.

- [Debugging](../help/debugging.md) — Debugging tools: watch mode, raw model streams, and tracing reasoning leakage. Read when: You need to inspect raw model output for reasoning leakage; You want to run the Gateway in watch mode while iterating; You need a repeatable debugging workflow; You are diagnosing Node or tsx startup errors.
- [Environment variables](../help/environment.md) — Where OpenClaw loads environment variables and the precedence order. Read when: You need to know which env vars are loaded, and in what order; You are debugging missing API keys in the Gateway; You are documenting provider auth or deployment environments.
- [FAQ](../help/faq.md) — Frequently asked questions about OpenClaw setup, configuration, and usage. Read when: Answering common setup, install, onboarding, or runtime support questions; Triaging user-reported issues before deeper debugging.
- [FAQ: first-run setup](../help/faq-first-run.md) — FAQ: quick-start and first-run setup — install, onboard, auth, subscriptions, initial failures. Read when: New install, onboarding stuck, or first-run errors; Choosing auth and provider subscriptions; Cannot access docs.openclaw.ai, cannot open dashboard, install stuck.
- [FAQ: models and auth](../help/faq-models.md) — FAQ: model defaults, selection, aliases, switching, failover, and auth profiles. Read when: Choosing or switching models, configuring aliases; Debugging model failover / "All models failed"; Understanding auth profiles and how to manage them.
- [General troubleshooting](../help/troubleshooting.md) — Symptom first troubleshooting hub for OpenClaw. Read when: OpenClaw is not working and you need the fastest path to a fix; You want a triage flow before diving into deep runbooks.
- [Help](../help/index.md) — Help hub: common fixes, install sanity, and where to look when something breaks. Read when: You are new and want a "what do I click/run" guide; Something broke and you want the fastest path to a fix.
- [Scripts](../help/scripts.md) — Repository scripts: purpose, scope, and safety notes. Read when: Running scripts from the repo; Adding or changing scripts under ./scripts.
- [Testing](../help/testing.md) — Testing kit: unit/e2e/live suites, Docker runners, and what each test covers. Read when: Running tests locally or in CI; Adding regressions for model/provider bugs; Debugging gateway + agent behavior.
- [Testing: live suites](../help/testing-live.md) — Live (network-touching) tests: model matrix, CLI backends, ACP, media providers, credentials. Read when: Running live model matrix / CLI backend / ACP / media-provider smokes; Debugging live-test credential resolution; Adding a new provider-specific live test.
- [Testing: updates and plugins](../help/testing-updates-plugins.md) — How OpenClaw validates update paths, package migrations, and plugin install/update behavior. Read when: Changing OpenClaw update, doctor, package acceptance, or plugin install behavior; Preparing or approving a release candidate; Debugging package update, plugin dependency cleanup, or plugin install regressions.
