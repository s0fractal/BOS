---
id: bos:requirement:provenance-before-authority
schema: bos.atom@v0
kind: requirement
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: Provenance precedes promotion and action
created_at: "2026-07-28T00:00:00Z"
created_by: human:s0fractal+model:codex
scope: [bos, warrant, autonomy]
relations:
  - predicate: realizes
    object: bos:principle:freedom-authority-separation
payload:
  statement: "An adopted decision MUST identify its reasons and authority; a material action MUST bind that decision and produce outcome evidence."
  level: MUST
  verification:
    - "Reject self-authorized model promotion."
    - "Reject a decision with no reason atom."
    - "Reject a material action with no authority decision."
    - "Do not mark work done without its declared acceptance evidence."
---

# Provenance before authority

Warrant is the intended authority carrier when the ecosystem reaches that
integration phase. BOS v0 records the binding without pretending adoption has
already occurred.
