---
id: bos:risk:freshness-without-teeth
schema: bos.atom@v0.2
kind: risk
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: Expired assertions remain usable for decisions
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
  statement: "Freshness is defined as a projection: an expired claim becomes stale in views but nothing forbids a decision from citing it. The watched-source-commitment trigger has no watcher registry, so watching is unrepresented in the graph. Staleness therefore has no normative effect at the authority boundary where it matters most."
  likelihood: high
  impact: medium
  mitigation:
    - "Define the normative effect of expiry: a decision MUST NOT cite an expired claim without an explicit adjudicated override."
    - "Represent watched sources as atoms or cut entries so the watcher set is graph-visible."
  evidence:
    - bos:evidence:review:kimi-bos-0001-rev2
---

# Freshness without teeth

A freshness axis that only repaints views reproduces the rev-1 problem one
level down: status that looks like governance but does not constrain it.
