---
id: bos:risk:immutable-sensitive-payload
schema: bos.atom@v0.2
kind: risk
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
  priority: bos:status:priority:now
title: Immutable atoms permanently disclose sensitive payloads
created_at: "2026-07-28T00:00:00Z"
created_by:
  - bos:actor:model:kimi-k3
scope: [bos, privacy]
disclosure:
  classification: public
  payload_mode: embedded
  retention: indefinite
relations:
  - predicate: derived_from
    object: bos:evidence:review:kimi-bos-0001-rev1
payload:
  statement: "A secret placed in an immutable public atom cannot be reliably erased from clones, mirrors, caches, or evidence bundles."
  likelihood: medium
  impact: critical
  mitigation:
    - "Keep public descriptors separate from encrypted private payloads."
    - "Store only commitments and controlled locators for confidential or secret material."
    - "Reject embedded confidential and secret payload modes."
  evidence:
    - bos:evidence:review:kimi-bos-0001-rev1
---

# Immutable sensitive payload

Tombstones can change current views. They cannot make already copied plaintext
cease to exist.
