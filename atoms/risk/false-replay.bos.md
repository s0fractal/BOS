---
id: bos:risk:false-replay
schema: bos.atom@v0.2
kind: risk
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: A recorded model context is misrepresented as deterministic replay
created_at: "2026-07-28T00:00:00Z"
created_by:
  - bos:actor:human:s0fractal
  - bos:actor:model:codex
scope: [bos, machine-experience]
disclosure:
  classification: public
  payload_mode: embedded
  retention: indefinite
relations: []
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
