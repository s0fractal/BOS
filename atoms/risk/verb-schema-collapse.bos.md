---
id: bos:risk:verb-schema-collapse
schema: bos.atom@v0.2
kind: risk
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: Process verbs collapse at the schema level
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
  statement: "The verb table maps both OBSERVES and RECORDS to the evidence kind, and no schema field records which verb a given evidence atom performs. The claim that no verb is inferred from prose is therefore stronger than the realization supports: a validator cannot distinguish observation from recording without reading prose."
  likelihood: high
  impact: low
  mitigation:
    - "Add a verb or mode field to the evidence payload, or"
    - "narrow the normative sentence to claim verb realization only where the schema actually encodes it."
  evidence:
    - bos:evidence:review:kimi-bos-0001-rev2
---

# Verb collapse

The rev-2 verb table was introduced precisely to stop collapsing distinctions
that RFC prose collapses. The schema currently re-collapses one of them.
