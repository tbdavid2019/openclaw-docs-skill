# Automation documentation catalog

Cron, hooks, tasks, standing orders, and webhooks.

Open only the entries relevant to the current request. Start with at most three documents.

- [Automation](../automation/index.md) — Overview of automation mechanisms: tasks, automations, hooks, standing orders, and Task Flow. Read when: Deciding how to automate work with OpenClaw; Choosing between heartbeat, automations, hooks, and standing orders; Looking for the right automation entry point.
- [Automations](../automation/cron-jobs.md) — Automations: scheduled jobs, webhooks, and Gmail PubSub triggers for the Gateway scheduler. Read when: Scheduling background jobs or wakeups; Wiring external triggers (webhooks, Gmail) into OpenClaw; Deciding between heartbeat and automations for scheduled work.
- [Background tasks](../automation/tasks.md) — Background task tracking for ACP runs, subagents, automation runs, and CLI operations. Read when: Inspecting background work in progress or recently completed; Debugging delivery failures for detached agent runs; Understanding how background runs relate to sessions, automations, and heartbeat.
- [Hooks](../automation/hooks.md) — Internal hooks: install, write, and verify automation for commands and lifecycle events. Read when: You want event-driven automation for /new, /reset, /stop, or session and Gateway events; You want to write, install, enable, or debug an internal hook; You need to understand hook discovery, event data, or reply delivery.
- [IMAP email trigger](../automation/imap.md) — Watch an IMAP mailbox and route authenticated incoming email to an isolated restricted reader agent. Read when: Triggering OpenClaw from Fastmail, iCloud, or another IMAP mailbox; Configuring sender authentication and isolated email reader sessions; Troubleshooting IMAP IDLE, mailbox credentials, or rejected senders.
- [Standing orders](../automation/standing-orders.md) — Define permanent operating authority for autonomous agent programs. Read when: Setting up autonomous agent workflows that run without per-task prompting; Defining what the agent can do independently vs. what needs human approval; Structuring multi-program agents with clear boundaries and escalation rules.
- [Task flow](../automation/taskflow.md) — Task Flow orchestration layer above background tasks. Read when: You want to understand how Task Flow relates to background tasks; You encounter Task Flow or openclaw tasks flow in release notes or docs; You want to inspect or manage durable flow state.
