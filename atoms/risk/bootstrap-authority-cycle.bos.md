---
id: bos:risk:bootstrap-authority-cycle
schema: bos.atom@v0.2
kind: risk
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
  priority: bos:status:priority:now
title: BOS attempts to authorize its own genesis
created_at: "2026-07-28T00:00:00Z"
created_by:
  - bos:actor:model:kimi-k3
scope: [bos]
disclosure:
  classification: public
  payload_mode: embedded
  retention: indefinite
relations:
  - predicate: derived_from
    object: bos:evidence:review:kimi-bos-0001-rev1
payload:
  statement: "A proposed specification cannot derive the authority that adopts its own kind registry, scope decision, and adoption rules."
  likelihood: high
  impact: critical
  mitigation:
    - "Declare an external human genesis act over exact bytes."
    - "Represent unselected directions as proposals, not decisions."
    - "Move later adoption to an independently verified Warrant authority path."
  evidence:
    - bos:evidence:review:kimi-bos-0001-rev1
---

# Bootstrap authority cycle

Genesis must be acknowledged as an external boundary, not hidden inside the
system it creates.
