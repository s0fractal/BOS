---
id: bos:countervector:forged-genesis-adoption
schema: bos.atom@v0.2
kind: countervector
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
  priority: bos:status:priority:now
title: Model-authored genesis adoption in an unsigned commit
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
  construction: "A model actor with repository write access authors an adoption atom with mode genesis-human naming bos:actor:human:s0fractal as authority, in a later unsigned commit, claiming an explicit human instruction that never occurred."
  expected_failure: "The graph must not transition any atom to adopted on the basis of an unauthenticated genesis record; V3 must distinguish a signed, pre-pinned authority from a self-declared one."
  verification_class: mechanical
  verification:
    - "No adoption atom is accepted as genesis unless its commit is signed by a key pinned in the candidate revision or anchored externally."
    - "The bootstrap actor descriptor carries a verifiable external_ids entry before any genesis adoption is evaluated."
---

# Forged genesis adoption

This countervector targets the gap between section 1.2(5) prose ("explicit
human instruction") and what V3 can mechanically check.
