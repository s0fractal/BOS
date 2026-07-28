---
id: bos:decision:v0-bounded-scope
schema: bos.atom@v0
kind: decision
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
  priority: bos:status:priority:now
title: BOS v0 is a typed decision graph, not an autonomous journal runtime
created_at: "2026-07-28T00:00:00Z"
created_by: human:s0fractal+model:codex
scope: [bos]
relations:
  - predicate: mitigates
    object: bos:risk:meta-recursion
  - predicate: mitigates
    object: bos:risk:ontology-explosion
payload:
  question: "How much infrastructure should BOS build before proving that model trajectories improve one real ecosystem decision?"
  choice: "Start with strict typed Markdown atoms, immutable context cuts, and a read-only graph projection; defer event sourcing, autonomous execution, and rich UI."
  reasons:
    - bos:risk:meta-recursion
    - bos:risk:ontology-explosion
    - bos:principle:projection-not-ssot
  authority: "Proposed jointly by human:s0fractal and model:codex; adoption remains a human decision."
---

# Bounded v0

Trinity already explores the general cognitive/event substrate. BOS v0 proves
the narrower ecosystem-control use case before choosing how deeply to integrate.
