---
id: bos:context_cut:bos-0001-rev3-input
schema: bos.atom@v0.3
kind: context_cut
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: BOS-0001 revision 3 amendment input cut
created_at: "2026-07-28T20:00:00Z"
created_by:
  - bos:actor:model:codex
scope: [bos]
disclosure:
  classification: public
  payload_mode: embedded
  retention: indefinite
relations:
  - predicate: observes
    object: bos:asset:repo:bos
payload:
  repositories:
    - asset: bos:asset:repo:bos
      commit: c0b31b3f38c33de1a0b498bee2ac09bda9939d5c
      dirty: false
  sources: []
  anchors:
    - kind: git
      value: "c0b31b3f38c33de1a0b498bee2ac09bda9939d5c"
---

# BOS-0001 revision 3 amendment input cut

This clean commit contains Kimi's revision-2 adversarial trajectory before the
Codex amendment.
