---
id: bos:risk:experiment-outside-graph
schema: bos.atom@v0.2
kind: risk
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
  priority: bos:status:priority:now
title: The central falsification experiment lives outside the typed graph
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
  statement: "BOS-E0001, the Phase 2 exit gate and the target of the section 19 rubric, is plain Markdown without frontmatter: not an atom, not in any vehicle includes list, not under the revision algorithm, invisible to V1. The system's flagship proof obligation is itself an untyped document — the same class of leak that rev-1 countervector 16 targeted inside vehicles."
  likelihood: high
  impact: medium
  mitigation:
    - "Represent BOS-E0001 as a vehicle atom (RESEARCH or RFC) with its questions and pass conditions in a typed payload."
    - "Include the experiment atom in the BOS-0001 vehicle membership."
  evidence:
    - bos:evidence:review:kimi-bos-0001-rev2
---

# Experiment outside the graph

If the proof obligation is allowed to be untyped prose, the type system's
guarantees stop exactly where they are needed most.
