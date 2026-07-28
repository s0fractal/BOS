---
id: bos:countervector:reverse-symmetric-edge
schema: bos.atom@v0.2
kind: countervector
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: One-directional use of a symmetric predicate
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
  target: bos:vehicle:bos-0001
  construction: "Author relation_claim A conflicts_with B without the reverse edge, and a second pair where both directions exist as separate atoms with different confidence values."
  expected_failure: "Symmetry semantics must be defined per predicate: either the reverse edge is entailed, or reversed duplicates are merged; contradictory confidences on a symmetric pair must be detectable."
  verification_class: mechanical
  verification:
    - "Validator behavior for missing reverse edge is specified and implemented."
    - "Validator flags asymmetric confidence on symmetric predicate pairs."
---

# Reverse symmetric edge

conflicts_with and equivalent_to are symmetric; the registry stores them as
directed edges with no declared symmetry rule.
