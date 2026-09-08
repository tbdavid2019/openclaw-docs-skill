# Ci documentation catalog

Documentation under `ci/`.

Open only the entries relevant to the current request. Start with at most three documents.

- [CI capacity and shard weights](../ci/capacity.md) — Runner registration budget, concurrency headroom, and measured shard timings. Read when: You are tuning CI concurrency or shard counts; You need the measured timings behind shard packing.
- [CI checkout ownership](../ci/checkout.md) — Shared checkout anchors, retry budgets, and trusted action policy. Read when: A CI checkout step failed or retried; You are changing checkout anchors or trusted action policy.
- [CI pipeline jobs](../ci/pipeline.md) — Job graph, fail-fast order, and the Control UI size budgets. Read when: You need to know which CI job owns a check; You want the order jobs run in and what blocks what.
- [CI runner classes](../ci/runners.md) — Trust-based runner routing, Blacksmith classes, and runner backend modes. Read when: You need to know which runner a lane uses; You are choosing or changing a runner class.
- [CI scope and routing](../ci/scope-and-routing.md) — Changed-scope detection, lane routing, and manual dispatch behavior. Read when: You need to understand why a CI job did or did not run; You are changing changed-scope detection or dispatch inputs.
- [Local checks and Testbox](../ci/local-proof.md) — Local command equivalents, shrink-only ratchets, and Crabbox remote proof. Read when: You want to reproduce a CI lane on your own machine; You are producing Testbox or Crabbox proof for a pull request.
- [Release validation workflows](../ci/release-validation.md) — Full Release Validation, Package Acceptance, install smoke, and Docker E2E. Read when: You are coordinating a release validation run or rerun; You need to validate a published package or plugin build.
- [Scheduled and maintenance workflows](../ci/scheduled-workflows.md) — Performance, QA Lab, CodeQL, maintenance jobs, and ClawSweeper forwarding. Read when: You are changing ClawSweeper dispatch or GitHub activity forwarding; You are triaging a nightly, scheduled, or maintenance workflow.
- [Watch a CI run](../ci/watching-runs.md) — Wait on a pull request head, recover a stuck run, and clear the evidence gate. Read when: You are debugging a failing GitHub Actions check; You need to rerun or recover a pull request run.
