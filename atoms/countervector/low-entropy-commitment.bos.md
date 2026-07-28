---
id: bos:countervector:low-entropy-commitment
schema: bos.atom@v0.2
kind: countervector
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
  priority: bos:status:priority:now
title: Dictionary attack on a bare SHA-256 payload commitment
created_at: "2026-07-28T17:42:51Z"
created_by:
  - bos:actor:model:kimi-k3
scope: [bos, privacy]
disclosure:
  classification: public
  payload_mode: embedded
  retention: indefinite
relations:
  - predicate: derived_from
    object: bos:evidence:review:kimi-bos-0001-rev2
payload:
  target: bos:vehicle:bos-0001
  construction: "A confidential atom with payload_mode commitment whose secret payload is a short low-entropy string (for example a two-letter answer or a 4-digit PIN), committed as bare SHA-256 as section 12 currently permits."
  expected_failure: "The commitment scheme must reject unkeyed nonce-less commitments: a public commitment must not admit offline recovery or equality correlation across atoms."
  verification_class: mechanical
  verification:
    - "Recovering the fixture payload from its public commitment by dictionary enumeration takes seconds — demonstrating the failure under the current scheme."
    - "Two fixtures with identical payloads produce identical commitments, demonstrating correlation."
---

# Low-entropy commitment

A nonce stored with the private locator, or a keyed hash, closes this with one
schema line. Without it, commitment mode relocates secrets instead of
protecting them.
