---
id: bos:countervector:ambiguous-dirty-cut
schema: bos.atom@v0.2
kind: countervector
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: Two tools hash the same dirty workspace differently
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
  target: bos:requirement:context-cut
  construction: "One tool includes untracked files and mode bits while another hashes only tracked contents and normalized line endings."
  expected_failure: "BOS v0.2 must reject the dirty repository cut before either digest is treated as history."
  verification_class: mechanical
  verification:
    - "The context-cut schema accepts only dirty=false."
---

# Ambiguous dirty cut

Dirty reasoning work may exist, but it is not an authoritative historical cut
in v0.2.
