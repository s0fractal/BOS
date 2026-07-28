---
id: bos:requirement:verification-boundaries
schema: bos.atom@v0.3
kind: requirement
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: Every normative check declares its verification class
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
  statement: "Every requirement and countervector MUST declare whether its verdict is mechanical, adjudicated, or research; only mechanical checks may be presented as deterministic validator results."
  level: MUST
  verification_class: mechanical
  verification:
    - "Reject a requirement or countervector with no verification_class."
    - "A mechanical check names an executable deterministic rule."
    - "An adjudicated check names the authority that interprets it before adoption."
    - "A research check cannot block mechanically unless a later atom defines the missing contract."
    - "A machine-readable validator report binds its exact input universe and says when no clean historical cut is bound."
---

# Verification boundaries

The system must say where computation ends and judgment begins.
