---
id: bos:requirement:context-cut
schema: bos.atom@v0
kind: requirement
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: Autonomous reasoning binds an immutable context cut
created_at: "2026-07-28T00:00:00Z"
created_by: human:s0fractal+model:codex
scope: [bos, autonomy]
relations:
  - predicate: realizes
    object: bos:claim:experience-is-trajectory
  - predicate: mitigates
    object: bos:risk:false-replay
payload:
  statement: "A trajectory that may inform an adopted decision or material action MUST bind the exact repository commits, source digests, and external anchors available to the actor."
  level: MUST
  verification:
    - "A clean repository observation names a full commit hash."
    - "A dirty repository observation additionally commits a working-tree digest."
    - "Research inputs are content-addressed evidence atoms, not mutable paths alone."
    - "Later data cannot be silently inserted into an earlier context cut."
---

# Immutable context cut

Wall-clock time is descriptive. Git commitments, source digests, WarrantIDs,
and Bitcoin block references are stronger historical coordinates.
