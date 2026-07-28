---
id: bos:countervector:immutable-secret
schema: bos.atom@v0.2
kind: countervector
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: Secret plaintext embedded in an immutable atom
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
  target: bos:requirement:privacy-boundary
  construction: "Declare classification secret with payload_mode embedded and place private research in the body."
  expected_failure: "Schema rejects the disclosure envelope before the atom can enter the active graph."
  verification_class: mechanical
  verification:
    - "Secret and confidential classifications require commitment mode, commitment, private locator, and encryption descriptor."
---

# Immutable secret

The countervector prevents a false promise that later tombstones can remove
already published plaintext.
