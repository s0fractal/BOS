---
id: bos:countervector:self-authorizing-genesis
schema: bos.atom@v0.2
kind: countervector
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: Specification self-authorizes its genesis
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
  target: bos:vehicle:bos-0001
  construction: "Represent a proposed scope choice as a decision whose authority is defined only by the same unadopted specification."
  expected_failure: "The graph must not project the decision or specification as adopted."
  verification_class: mechanical
  verification:
    - "No adoption atom exists for the candidate revision."
    - "The bounded-scope object is a proposal, not a decision."
---

# Self-authorizing genesis

This countervector caused the rev-1 scope decision to be retyped as a proposal.
