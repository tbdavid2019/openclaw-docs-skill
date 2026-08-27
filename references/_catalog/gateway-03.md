# Gateway documentation catalog

Gateway configuration, operations, security, and networking.

Open only the entries relevant to the current request. Start with at most three documents.

- [Trusted proxy auth](../gateway/trusted-proxy-auth.md) — Delegate gateway authentication to a trusted reverse proxy (Pomerium, Caddy, nginx + OAuth). Read when: Running OpenClaw behind an identity-aware proxy; Setting up Pomerium, Caddy, or nginx with OAuth in front of OpenClaw; Fixing WebSocket 1008 unauthorized errors with reverse proxy setups; Deciding where to set HSTS and other HTTP hardening headers.
- [Usage telemetry and update checks](../gateway/telemetry.md) — What OpenClaw sends: a daily update check by default, optional anonymous feature statistics, and every privacy control. Read when: Checking what information OpenClaw sends and what it never collects; Deciding whether to share anonymous feature statistics; Enabling or disabling anonymous feature statistics; Disabling all automatic update-check requests.
