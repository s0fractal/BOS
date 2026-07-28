---
id: bos:risk:commitment-low-entropy
schema: bos.atom@v0.2
kind: risk
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
  priority: bos:status:priority:now
title: Bare SHA-256 commitments are brute-forceable and correlatable
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
  statement: "The commitment payload mode requires a SHA-256 commitment but no nonce or keyed hash. A low-entropy confidential payload (short key, yes/no answer, small enum) is recoverable by dictionary attack against the public commitment, and identical secrets in different atoms produce identical commitments, enabling correlation. The retention vocabulary is also not enumerated."
  likelihood: medium
  impact: critical
  mitigation:
    - "Require a random nonce stored with the private locator, committed as SHA-256(nonce || payload), or a keyed hash."
    - "Make the nonce requirement mechanically checkable in the commitment payload schema."
    - "Close the retention vocabulary in the disclosure schema."
  evidence:
    - bos:evidence:review:kimi-bos-0001-rev2
---

# Low-entropy commitments

A commitment scheme that leaks equality and admits dictionary attack does not
protect the payload; it only relocates the plaintext. This is exactly the
class of requirement the schema can enforce mechanically.
