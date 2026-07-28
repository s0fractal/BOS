---
id: bos:relation_claim:experience-motivates-trajectory
schema: bos.atom@v0.2
kind: relation_claim
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: Experience claim motivates trajectory requirement
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
  subject: bos:claim:experience-is-trajectory
  predicate: motivates
  object: bos:requirement:model-trajectory
  confidence: medium
  falsifier: "State snapshots without actor trajectories preserve historical reasons and alternative paths equally well in BOS-E0001."
  evidence: []
  observed_in: bos:context_cut:bos-0001-rev1
---

# Experience motivates trajectory

This was an embedded edge in revision 1 and is first-class in revision 2.
