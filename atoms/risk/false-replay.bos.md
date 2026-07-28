---
id: bos:risk:false-replay
schema: bos.atom@v0
kind: risk
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: A recorded model context is misrepresented as deterministic replay
created_at: "2026-07-28T00:00:00Z"
created_by: human:s0fractal+model:codex
scope: [bos, machine-experience]
relations:
  - predicate: motivates
    object: bos:requirement:context-cut
payload:
  statement: "A context cut can preserve what a model saw without proving that a future invocation will reproduce the same inference."
  likelihood: medium
  impact: high
  mitigation:
    - "Call the operation recontextualization unless model, weights, runtime, seed, and determinism are actually bound."
    - "Use Sigma only for the deterministic subclaims it can execute."
    - "Preserve the original output as evidence rather than regenerating it silently."
---

# False replay

BOS records a historical perspective. It does not manufacture determinism where
none existed.
