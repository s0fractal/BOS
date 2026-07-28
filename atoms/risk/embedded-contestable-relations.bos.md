---
id: bos:risk:embedded-contestable-relations
schema: bos.atom@v0.2
kind: risk
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: Contestable causal relations are hidden inside source atoms
created_at: "2026-07-28T00:00:00Z"
created_by:
  - bos:actor:model:kimi-k3
scope: [bos, machine-experience]
disclosure:
  classification: public
  payload_mode: embedded
  retention: indefinite
relations:
  - predicate: derived_from
    object: bos:evidence:review:kimi-bos-0001-rev1
payload:
  statement: "An embedded semantic edge cannot independently carry author, evidence, confidence, context, expiry, falsifier, or supersession."
  likelihood: high
  impact: high
  mitigation:
    - "Restrict embedded relations to structural graph topology."
    - "Represent contestable causal meaning as relation_claim atoms."
  evidence:
    - bos:evidence:review:kimi-bos-0001-rev1
---

# Embedded contestable relations

The relation itself is often the subjective experience that BOS exists to
preserve.
