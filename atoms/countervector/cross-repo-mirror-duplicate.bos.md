---
id: bos:countervector:cross-repo-mirror-duplicate
schema: bos.atom@v0.2
kind: countervector
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: Byte-identical atom mirrored in two repositories
created_at: "2026-07-28T17:42:51Z"
created_by:
  - bos:actor:model:kimi-k3
scope: [bos, ecosystem]
disclosure:
  classification: public
  payload_mode: embedded
  retention: indefinite
relations:
  - predicate: derived_from
    object: bos:evidence:review:kimi-bos-0001-rev2
payload:
  target: bos:vehicle:bos-0001
  construction: "Two declared-universe repositories each contain a byte-identical copy of the same atom ID, the standard cross-repository sharing scenario for ecosystem coordination."
  expected_failure: "The mirror is valid when byte-identical across universes; uniqueness is enforced within one declared universe, not across the ecosystem the graph exists to coordinate."
  verification_class: mechanical
  verification:
    - "Uniqueness check is scoped to one declared universe."
    - "Cross-universe copies with identical bytes pass; divergent bytes fail."
---

# Cross-repo mirror duplicate

Section 5.1 bans duplicate IDs with no mirror exception, which outlaws the
primary multi-repository sharing pattern instead of governing it.
