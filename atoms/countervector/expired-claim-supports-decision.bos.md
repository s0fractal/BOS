---
id: bos:countervector:expired-claim-supports-decision
schema: bos.atom@v0.2
kind: countervector
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: Decision cites a claim past its valid_until
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
  target: bos:vehicle:bos-0001
  construction: "A decision atom cites, as its reason, a claim whose valid_until precedes the decision's created_at, with no override record."
  expected_failure: "Freshness must have a normative effect at the authority boundary: the decision is rejected or requires an explicit adjudicated override naming the expired reason."
  verification_class: mechanical
  verification:
    - "Validator compares reason-atom valid_until against decision created_at."
    - "Override path, if any, is a first-class record, not prose."
---

# Expired claim supports decision

Section 13 makes freshness a projection only. This countervector shows the
projection failing at the exact boundary where freshness matters.
