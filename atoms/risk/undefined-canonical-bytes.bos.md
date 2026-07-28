---
id: bos:risk:undefined-canonical-bytes
schema: bos.atom@v0.2
kind: risk
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
  priority: bos:status:priority:now
title: Content identity lacks canonical bytes
created_at: "2026-07-28T00:00:00Z"
created_by:
  - bos:actor:model:kimi-k3
scope: [bos]
disclosure:
  classification: public
  payload_mode: embedded
  retention: indefinite
relations:
  - predicate: derived_from
    object: bos:evidence:review:kimi-bos-0001-rev1
payload:
  statement: "Revision and dirty-tree digests cannot be independently reproduced until their exact byte domains and self-reference rules are fixed."
  likelihood: high
  impact: critical
  mitigation:
    - "Define exact UTF-8/LF atom bytes and revision placeholder normalization."
    - "Reject dirty repository cuts in v0.2."
    - "Pin context with clean full Git commits."
  evidence:
    - bos:evidence:review:kimi-bos-0001-rev1
---

# Undefined canonical bytes

Content-addressed is a byte contract, not an adjective.
