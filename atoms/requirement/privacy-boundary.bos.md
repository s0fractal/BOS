---
id: bos:requirement:privacy-boundary
schema: bos.atom@v0.2
kind: requirement
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
  priority: bos:status:priority:now
title: Private payloads remain outside immutable public atoms
created_at: "2026-07-28T00:00:00Z"
created_by:
  - bos:actor:human:s0fractal
  - bos:actor:model:codex
scope: [bos, privacy]
disclosure:
  classification: public
  payload_mode: embedded
  retention: indefinite
relations: []
payload:
  statement: "Confidential and secret material MUST be represented by a public-safe descriptor plus a content commitment and controlled encrypted locator; it MUST NOT be embedded as plaintext in an immutable BOS atom."
  level: MUST
  verification_class: mechanical
  verification:
    - "Reject confidential or secret disclosure with embedded payload mode."
    - "Require commitment, private locator, and encryption descriptor."
    - "Warn that tombstones cannot erase plaintext already copied outside the controlled store."
---

# Privacy boundary

BOS may prove that private evidence existed without publishing the evidence
itself.
