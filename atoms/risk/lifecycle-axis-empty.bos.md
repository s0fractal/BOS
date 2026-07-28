---
id: bos:risk:lifecycle-axis-empty
schema: bos.atom@v0.2
kind: risk
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: Lifecycle axis declared but has no values, and status additions require schema adoption
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
  statement: "Six status axes are declared but the genesis vocabulary covers only five; no status atom exists on the lifecycle axis. Any atom needing a lifecycle state is blocked until a schema or registry adoption. Because adding a status value requires adoption, routine vocabulary growth becomes a constitutional procedure, which will either stall work or push state into unstructured payload fields. The same applies to the closed scope vocabulary."
  likelihood: high
  impact: low
  mitigation:
    - "Seed at least one lifecycle value per declared axis in the genesis vocabulary."
    - "Define a lighter path for adding status values within an existing axis, distinct from schema-version adoption."
  evidence:
    - bos:evidence:review:kimi-bos-0001-rev2
---

# Empty lifecycle axis

Verified against the repository: atoms/status contains exactly five atoms and
none of them is on the lifecycle axis.
