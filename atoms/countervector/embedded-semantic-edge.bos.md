---
id: bos:countervector:embedded-semantic-edge
schema: bos.atom@v0.2
kind: countervector
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: Contestable semantic edge hidden in envelope relations
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
  target: bos:requirement:first-class-contestable-relations
  construction: "Insert predicate motivates or supports into an atom's structural relations array."
  expected_failure: "Closed schema rejects the semantic predicate; the author must create a relation_claim atom."
  verification_class: mechanical
  verification:
    - "Structural predicate enum excludes motivates and supports."
---

# Embedded semantic edge

Semantic relation claims get independent identity and provenance.
