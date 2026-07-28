---
id: bos:requirement:model-trajectory
schema: bos.atom@v0.2
kind: requirement
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: Model paths are preserved as separate trajectories
created_at: "2026-07-28T00:00:00Z"
created_by:
  - bos:actor:human:s0fractal
  - bos:actor:model:codex
scope: [bos, autonomy, machine-experience]
disclosure:
  classification: public
  payload_mode: embedded
  retention: indefinite
relations: []
payload:
  statement: "BOS MUST preserve each actor's supplied set and produced atoms without merging disagreement into an artificial consensus."
  level: MUST
  verification_class: mechanical
  verification:
    - "A trajectory identifies its actor, objective, context cut, supplied set, output evidence, and produced set."
    - "Claude, Codex, Gemini, Kimi, and human paths remain separately addressable."
    - "A synthesis is a new atom derived from named trajectories, not an edit of them."
    - "Rejected and losing paths remain available as evidence or compost."
---

# Model trajectories

Disagreement is signal. Convergence is meaningful only when independent paths
remain distinguishable.
