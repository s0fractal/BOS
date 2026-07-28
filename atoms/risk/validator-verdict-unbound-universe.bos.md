---
id: bos:risk:validator-verdict-unbound-universe
schema: bos.atom@v0.2
kind: risk
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: Validator verdicts do not bind their input universe
created_at: "2026-07-28T17:42:51Z"
created_by:
  - bos:actor:model:kimi-k3
scope: [bos]
disclosure:
  classification: public
  payload_mode: embedded
  retention: indefinite
relations:
  - predicate: derived_from
    object: bos:evidence:review:kimi-bos-0001-rev2
payload:
  statement: "Views must declare their source universe and cut, and the validator is defined as operating on an explicitly declared universe, but V0–V4 verdicts are not required to carry that declaration. Two honest validator runs over different file sets can report contradictory results, and neither verdict is comparable or portable."
  likelihood: medium
  impact: medium
  mitigation:
    - "Require every validator report to bind the exact universe and context cut it ran over, symmetric with the view requirements."
  evidence:
    - bos:evidence:review:kimi-bos-0001-rev2
---

# Unbound validator verdicts

"V1 passes" is meaningless without knowing over which files it passed. The
spec already solved this for views; the same line solves it for validators.
