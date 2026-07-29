# Security documentation catalog

Threat models, hardening, and incident response.

Open only the entries relevant to the current request. Start with at most three documents.

- [Contributing to the threat model](../security/CONTRIBUTING-THREAT-MODEL.md) — How to contribute to the OpenClaw threat model. Read when: You want to contribute security findings or threat scenarios; Reviewing or updating the threat model.
- [Formal verification (security models)](../security/formal-verification.md) — Machine-checked security models for OpenClaw's highest-risk paths. Read when: Reviewing formal security model guarantees or limits; Reproducing or updating TLA+/TLC security model checks.
- [Incident response](../security/incident-response.md) — How OpenClaw triages, responds to, and follows up on security incidents. Read when: Responding to a security report or suspected security incident; Preparing a coordinated disclosure or patched security release; Reviewing post-incident follow-up expectations.
- [Network proxy](../security/network-proxy.md) — How to route OpenClaw runtime HTTP and WebSocket traffic through an operator-managed filtering proxy. Read when: You want defense-in-depth against SSRF and DNS rebinding attacks; Configuring an external forward proxy for OpenClaw runtime traffic.
- [Threat model (MITRE ATLAS)](../security/THREAT-MODEL-ATLAS.md) — OpenClaw threat model mapped to the MITRE ATLAS framework. Read when: Reviewing security posture or threat scenarios; Working on security features or audit responses.
