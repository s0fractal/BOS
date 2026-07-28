---
id: bos:risk:duplicate-id-prohibition-multirepo
schema: bos.atom@v0.2
kind: risk
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: Duplicate-ID prohibition makes multi-repo mirroring undefined
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
  statement: "Rev 2 declares duplicate IDs invalid with no mirror exception, while BOS defines itself as coordinating multiple repositories. A byte-identical atom held in two repositories is now invalid rather than governed, leaving the primary cross-repository sharing scenario as undefined behavior."
  likelihood: medium
  impact: medium
  mitigation:
    - "Scope uniqueness to one declared universe: duplicate IDs are invalid within a universe."
    - "Permit cross-universe mirrors only when byte-identical, preserving the rev-1 protection without banning the ecosystem case."
  evidence:
    - bos:evidence:review:kimi-bos-0001-rev2
---

# Duplicate IDs and multi-repo

The fix for an underdefined mirror rule was a prohibition that ignores the
multi-repository reality the system exists to coordinate.
