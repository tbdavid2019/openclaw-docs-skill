# Ci documentation catalog

Documentation under `ci/`.

Open only the entries relevant to the current request. Start with at most three documents.

- [CI capacity and shard weights](../ci/capacity.md) — Runner registration budget, concurrency headroom, and measured shard timings. Read when: You are tuning CI concurrency or shard counts; You need the measured timings behind shard packing.
- [CI checkout ownership](../ci/checkout.md) — Shared checkout anchors, retry budgets, and trusted action policy. Read when: A CI checkout step failed or retried; You are changing checkout anchors or trusted action policy.
- [CI pipeline jobs](../ci/pipeline.md) — Job graph, fail-fast order, and the Control UI size budgets. Read when: You need to know which CI job owns a check; You want the order jobs run in and what blocks what.
- [CI runner classes](../ci/runners.md) — Trust-based runner routing, Blacksmith classes, and runner backend modes. Read when: You need to know which runner a lane uses; You are choosing or changing a runner class.
- [CI scope and routing](../ci/scope-and-routing.md) — Changed-scope detection, lane routing, and manual dispatch behavior. Read when: You need to understand why a CI job did or did not run; You are changing changed-scope detection or dispatch inputs.
- [Full Release Validation](../ci/release-validation/full-release-validation.md) — The Full Release Validation umbrella, release publish, and Docker Release dispatch. Read when: You are dispatching or rerunning Full Release Validation; You are publishing a release or a Docker image.
- [Install smoke and Docker E2E](../ci/release-validation/install-smoke-and-docker-e2e.md) — Install Smoke coverage, the local Docker E2E aggregate, and release-path Docker chunks. Read when: You are running or debugging Docker E2E lanes; You need the local Docker E2E tunables or the release-path chunk names.
- [Job budgets and platform lanes](../ci/scope-and-routing/job-budgets.md) — UI shards, concurrency and job budgets, lint memory policy, Android rows, and sticky-disk keys. Read when: You are changing job counts, concurrency caps, or matrix budgets; You are working on Android CI rows or sticky-disk keys.
- [Live and E2E shards](../ci/release-validation/live-and-e2e-shards.md) — Named live and E2E shards in the release live/E2E child workflow. Read when: You are rerunning a failed live or E2E shard; You need the shard names for a manual one-shot run.
- [Local checks and Testbox](../ci/local-proof.md) — Local command equivalents, shrink-only ratchets, and Crabbox remote proof. Read when: You want to reproduce a CI lane on your own machine; You are producing Testbox or Crabbox proof for a pull request.
- [Manual dispatches](../ci/scope-and-routing/manual-dispatches.md) — Manual CI dispatch behavior, release-gate fallbacks, and the Windows Testbox Probe. Read when: You are dispatching CI or Full Release Validation by hand; You need the Windows Testbox Probe inputs.
- [Node test lanes](../ci/scope-and-routing/node-test-lanes.md) — How the slowest Node test families are split, balanced, packed, and cached. Read when: You are changing Vitest sharding, packing, or shard timings; You are debugging a CI cache restore or a Node shard budget.
- [Package Acceptance](../ci/release-validation/package-acceptance.md) — Package Acceptance jobs, candidate sources, suite profiles, and dispatch examples. Read when: You are validating an installable OpenClaw package; You are debugging a failed package acceptance run.
- [Plugin Prerelease](../ci/release-validation/plugin-prerelease.md) — The separate Plugin Prerelease workflow, its batching limits, and when it runs. Read when: You are running or triaging Plugin Prerelease.
- [Release validation workflows](../ci/release-validation.md) — Full Release Validation, Package Acceptance, install smoke, and Docker E2E. Read when: You are coordinating a release validation run or rerun; You need to validate a published package or plugin build.
- [Scheduled and maintenance workflows](../ci/scheduled-workflows.md) — Performance, QA Lab, CodeQL, maintenance jobs, and ClawSweeper forwarding. Read when: You are changing ClawSweeper dispatch or GitHub activity forwarding; You are triaging a nightly, scheduled, or maintenance workflow.
- [Scope selection](../ci/scope-and-routing/selection.md) — Changed-scope detection and the per-area rules that select CI lanes. Read when: You need to know why a lane was or was not selected for a diff; You are changing changed-scope detection.
- [Watch a CI run](../ci/watching-runs.md) — Wait on a pull request head, recover a stuck run, and clear the evidence gate. Read when: You are debugging a failing GitHub Actions check; You need to rerun or recover a pull request run.
