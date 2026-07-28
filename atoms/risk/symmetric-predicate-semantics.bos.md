---
id: bos:risk:symmetric-predicate-semantics
schema: bos.atom@v0.2
kind: risk
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: Symmetric predicates in a directed registry with undefined semantics
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
  statement: "conflicts_with and equivalent_to are symmetric relations stored as directed edges with no declared symmetry semantics. A validator cannot infer the reverse edge, and reversed duplicates are not caught by uniqueness rules. equivalent_to additionally has no reference-resolution semantics: it is unclear whether references to one endpoint resolve to the other, making it either hidden ID aliasing or an empty predicate."
  likelihood: medium
  impact: medium
  mitigation:
    - "Declare symmetry per predicate and require the validator to treat reversed duplicates as one edge."
    - "Define equivalent_to resolution semantics or remove it from the v0.2 registry."
  evidence:
    - bos:evidence:review:kimi-bos-0001-rev2
---

# Symmetric predicate semantics

A closed predicate registry is only closed if each predicate's semantics are
closed too. Direction, symmetry, and resolution are part of the semantics.
