# Gateway documentation catalog

Gateway configuration, operations, security, and networking.

Open only the entries relevant to the current request. Start with at most three documents.

- [Security audit checks](../gateway/security/audit-checks.md) — Reference catalog of checkIds emitted by openclaw security audit. Read when: You saw a specific `checkId` in `openclaw security audit` output and want to know what it means; You need the fix key/path for a given finding; You are triaging severity across a security audit run.
- [Session permission modes](../gateway/permission-modes.md) — Session permission modes, workspace boundaries, and escalation reviewers. Read when: Choosing a permission mode for an agent session; Understanding who reviews an exec escalation; Comparing session permissions with sandbox and tool policy.
- [Tailscale](../gateway/tailscale.md) — Integrated Tailscale Serve/Funnel for the Gateway dashboard. Read when: Exposing the Gateway Control UI outside localhost; Automating tailnet or public dashboard access.
- [Tools invoke API](../gateway/tools-invoke-http-api.md) — Invoke a single tool directly via the Gateway HTTP endpoint. Read when: Calling tools without running a full agent turn; Building automations that need tool policy enforcement.
- [Troubleshooting](../gateway/troubleshooting.md) — Deep troubleshooting runbook for gateway, channels, automation, nodes, and browser. Read when: The troubleshooting hub pointed you here for deeper diagnosis; You need stable symptom based runbook sections with exact commands.
- [Trusted proxy auth](../gateway/trusted-proxy-auth.md) — Delegate gateway authentication to a trusted reverse proxy (Pomerium, Caddy, nginx + OAuth). Read when: Running OpenClaw behind an identity-aware proxy; Setting up Pomerium, Caddy, or nginx with OAuth in front of OpenClaw; Fixing WebSocket 1008 unauthorized errors with reverse proxy setups; Deciding where to set HSTS and other HTTP hardening headers.
- [Usage telemetry and update checks](../gateway/telemetry.md) — What OpenClaw sends: a daily update check by default, optional anonymous feature statistics, and every privacy control. Read when: Checking what information OpenClaw sends and what it never collects; Deciding whether to share anonymous feature statistics; Enabling or disabling anonymous feature statistics; Disabling all automatic update-check requests.
