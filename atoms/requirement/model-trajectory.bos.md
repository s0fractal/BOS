---
id: bos:requirement:model-trajectory
schema: bos.atom@v0
kind: requirement
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: Model paths are preserved as separate trajectories
created_at: "2026-07-28T00:00:00Z"
created_by: human:s0fractal+model:codex
scope: [bos, autonomy, machine-experience]
relations:
  - predicate: realizes
    object: bos:claim:experience-is-trajectory
payload:
  statement: "BOS MUST preserve each actor's read set and produced atoms without merging disagreement into an artificial consensus."
  level: MUST
  verification:
    - "A trajectory identifies its actor, objective, context cut, read set, and produced set."
    - "Claude, Codex, Gemini, Kimi, and human paths remain separately addressable."
    - "A synthesis is a new atom derived from named trajectories, not an edit of them."
    - "Rejected and losing paths remain available as evidence or compost."
---

# Model trajectories

Disagreement is signal. Convergence is meaningful only when independent paths
remain distinguishable.
