---
id: bos:risk:supersedes-uncontestable
schema: bos.atom@v0.2
kind: risk
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: Supersession is structural and therefore uncontestable
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
  statement: "The supersedes predicate is structural and carries no confidence, yet supersession is among the most contestable claims in the graph: two successors can both claim to supersede one predecessor, and deprecations are routinely disputed. The same argument that moved supports/refutes into relation_claim applies to supersedes, but rev 2 stamps this semantic claim into uncontestable topology."
  likelihood: medium
  impact: medium
  mitigation:
    - "Allow supersedes to be contested by a relation_claim targeting the structural edge, or"
    - "move supersession claims into relation_claim and keep only uncontested lineage structural."
  evidence:
    - bos:evidence:review:kimi-bos-0001-rev2
---

# Uncontestable supersession

Structural relations are defined as describing the topology of the record.
"X supersedes Y" is not topology; it is a governance claim about meaning.
