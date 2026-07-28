---
id: bos:requirement:first-class-contestable-relations
schema: bos.atom@v0.2
kind: requirement
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: Contestable semantic relations are first-class atoms
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
  statement: "A causal, strategic, equivalence, support, refutation, or constraint edge MUST be a relation_claim with actor provenance, confidence, context, and falsifier; embedded relations MUST be structural only."
  level: MUST
  verification_class: mechanical
  verification:
    - "Reject semantic predicates in envelope relations."
    - "Validate relation_claim subject, predicate, object, context, confidence, and falsifier."
    - "Allow evidence and expiry to attach to the relation independently of either endpoint."
---

# First-class contestable relations

The subjective edge is preserved without mutating either endpoint.
