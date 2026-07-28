---
id: bos:risk:unenforceable-norms
schema: bos.atom@v0.2
kind: risk
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: Normative MUST relies on an undefined oracle
created_at: "2026-07-28T00:00:00Z"
created_by:
  - bos:actor:model:kimi-k3
scope: [bos, process]
disclosure:
  classification: public
  payload_mode: embedded
  retention: indefinite
relations:
  - predicate: derived_from
    object: bos:evidence:review:kimi-bos-0001-rev1
payload:
  statement: "A requirement stated as mechanically normative may actually require semantic interpretation, a complete global universe, or an undefined query language."
  likelihood: high
  impact: high
  mitigation:
    - "Classify every requirement and countervector as mechanical, adjudicated, or research."
    - "Define completeness only relative to a declared context cut and source universe."
    - "Do not use MUST for an unavailable oracle."
  evidence:
    - bos:evidence:review:kimi-bos-0001-rev1
---

# Unenforceable norms

A rule that cannot say who or what decides its verdict is not yet a mechanical
gate.
