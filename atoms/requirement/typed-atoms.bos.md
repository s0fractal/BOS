---
id: bos:requirement:typed-atoms
schema: bos.atom@v0
kind: requirement
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: Every normative object is a closed typed atom
created_at: "2026-07-28T00:00:00Z"
created_by: human:s0fractal+model:codex
scope: [bos]
relations:
  - predicate: realizes
    object: bos:principle:projection-not-ssot
payload:
  statement: "Normative BOS data MUST decode into a closed schema, carry a stable identity independent of its filename, and use typed relations."
  level: MUST
  verification:
    - "Reject unknown envelope and kind-specific payload fields."
    - "Reject an unknown kind, status axis, relation predicate, or unresolved target."
    - "Reject duplicate atom IDs even when filenames differ."
    - "Treat schema version and atom identity as separate values."
---

# Closed typed atoms

WRT, ADR, SPEC, and ROADMAP are typed vehicles. Claim, risk, requirement,
decision, and evidence are semantic kinds. Statuses occupy orthogonal axes.
