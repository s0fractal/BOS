---
id: bos:countervector:dual-supersession
schema: bos.atom@v0.2
kind: countervector
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: Two successors both structurally supersede one predecessor
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
  construction: "Two atoms, authored by different actors, each carry a structural supersedes relation to the same predecessor atom, with incompatible payloads."
  expected_failure: "The conflict must surface as a contestable condition (for example a required relation_claim resolution), not pass silently as uncontestable topology."
  verification_class: mechanical
  verification:
    - "Validator flags competing structural supersedes edges to one predecessor."
    - "No projection may pick a winner without an explicit decision or adoption record."
---

# Dual supersession

Supersession decides which meaning is current. Leaving it structural makes the
most contested edge in the graph the least contestable.
