---
id: bos:risk:ontology-explosion
schema: bos.atom@v0.2
kind: risk
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: Type and atom proliferation overwhelms useful attention
created_at: "2026-07-28T00:00:00Z"
created_by:
  - bos:actor:human:s0fractal
  - bos:actor:model:codex
scope: [bos, process]
disclosure:
  classification: public
  payload_mode: embedded
  retention: indefinite
relations: []
payload:
  statement: "Making every thought first-class can create orphan atoms, redundant types, and context windows dominated by bookkeeping."
  likelihood: high
  impact: high
  mitigation:
    - "Keep the v0 kind registry closed."
    - "Require a concrete query or decision consumer before adding a new kind."
    - "Separate cold history from bounded active context."
    - "Measure whether a fresh model can answer the five BOS orientation questions."
---

# Ontology explosion

First-class does not mean always loaded. Addressability and attention are
separate resources.
