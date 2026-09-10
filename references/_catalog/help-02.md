# Help documentation catalog

Symptom-first troubleshooting and support.

Open only the entries relevant to the current request. Start with at most three documents.

- [Skills and automation](../help/faq/skills-and-automation.md) — Customizing skills, per-task models, subagents, cron jobs, and background runs. Read when: You are customizing, loading, or installing skills; A cron job, reminder, or subagent did not behave.
- [Test suites and commands](../help/testing/suites.md) — The unit, e2e, and live suites, which one to run, and the offline regression checks. Read when: You need to pick a test suite or command; You want to know what each suite covers.
- [Testing](../help/testing.md) — Index of the OpenClaw testing kit, one page per reader job. Read when: Running tests locally or in CI; Adding regressions for model/provider bugs; Debugging gateway + agent behavior.
- [Testing: live suites](../help/testing-live.md) — Live (network-touching) tests: model matrix, CLI backends, ACP, media providers, credentials. Read when: Running live model matrix / CLI backend / ACP / media-provider smokes; Debugging live-test credential resolution; Adding a new provider-specific live test.
- [Testing: updates and plugins](../help/testing-updates-plugins.md) — How OpenClaw validates update paths, package migrations, and plugin install/update behavior. Read when: Changing OpenClaw update, doctor, package acceptance, or plugin install behavior; Preparing or approving a release candidate; Debugging package update, plugin dependency cleanup, or plugin install regressions.
- [What is OpenClaw?](../help/faq/what-is-openclaw.md) — What OpenClaw is, who it is for, how it is funded, and how it compares. Read when: You are evaluating OpenClaw or explaining it to someone; You want the ownership, funding, or comparison answers.
- [Where things live on disk](../help/faq/where-things-live-on-disk.md) — Data locations, AGENTS.md and SOUL.md placement, backups, and uninstalling. Read when: You need to find, back up, or move OpenClaw data; You are deciding where agent instruction files belong.
- [Writing and adding tests](../help/testing/writing-tests.md) — Temp-directory rules, agent reliability eval gaps, and how to add a regression. Read when: You are writing a new test; You are adding a regression for a provider bug.
