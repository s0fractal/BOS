---
id: bos:requirement:genesis-adoption
schema: bos.atom@v0.2
kind: requirement
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
  priority: bos:status:priority:now
title: Genesis adoption is an explicit external act
created_at: "2026-07-28T00:00:00Z"
created_by:
  - bos:actor:human:s0fractal
  - bos:actor:model:codex
scope: [bos]
disclosure:
  classification: public
  payload_mode: embedded
  retention: indefinite
relations: []
payload:
  statement: "The first adopted BOS contract MUST be selected by an explicitly named external human authority over an exact clean Git revision; BOS MUST NOT derive that authority from its own proposed rules."
  level: MUST
  verification_class: mechanical
  verification:
    - "The genesis adoption atom uses mode genesis-human."
    - "Its authority resolves to a human actor."
    - "Its subject revision resolves to an exact canonical atom revision in a clean context cut."
    - "No genesis candidate is projected as adopted before that atom exists."
---

# Genesis adoption

Later governance may supersede the bootstrap authority through Warrant. It may
not rewrite the fact that genesis was external.
