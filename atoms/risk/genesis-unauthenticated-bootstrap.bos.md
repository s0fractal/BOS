---
id: bos:risk:genesis-unauthenticated-bootstrap
schema: bos.atom@v0.2
kind: risk
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
  priority: bos:status:priority:now
title: Genesis adoption is authority-by-file-edit
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
  statement: "The genesis adoption act reduces to writing an adoption atom in a later commit. The bootstrap authority bos:actor:human:s0fractal has no cryptographic binding, so any process with repository write access — including a model actor — can forge the root of all authority. V3 can check that an adoption names a revision and an authority, but cannot check that the human actually instructed it."
  likelihood: high
  impact: critical
  mitigation:
    - "Require the genesis adoption commit to be signed by a key pinned in the candidate revision before adoption."
    - "Alternatively bind genesis to an external anchor (Bitcoin or a pinned Warrant contract)."
    - "Populate external_ids on the bootstrap actor descriptor before Phase 0 exit."
  evidence:
    - bos:evidence:review:kimi-bos-0001-rev2
---

# Genesis adoption is authority-by-file-edit

Section 1.2 of BOS-0001 rev 2 honestly declares genesis external, but the
external act is unauthenticated. Freedom/authority separation at the root is
currently enforced by etiquette, not by mechanism.
