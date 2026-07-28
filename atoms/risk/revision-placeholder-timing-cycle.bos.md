---
id: bos:risk:revision-placeholder-timing-cycle
schema: bos.atom@v0.2
kind: risk
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
  priority: bos:status:priority:now
title: Revision field appears only at adoption, changing the re-gated bytes
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
  statement: "The genesis candidate carries no revision field, while adoption requires exactly one. Introducing the placeholder line changes the candidate bytes, so the adopted object differs from what the independent re-gate reviewed. The ritual describing when the zeroed revision line is introduced — and that re-gate must run over the placeholder-bearing file — is undefined."
  likelihood: high
  impact: high
  mitigation:
    - "Define the placeholder ritual: re-gate MUST run over the file that already contains the zeroed revision line."
    - "State in Phase 0 exit criteria that the re-gated bytes and the adopted bytes are the same file."
  evidence:
    - bos:evidence:review:kimi-bos-0001-rev2
---

# Revision placeholder timing cycle

Section 5.2 requires the revision field at adoption; section 1.2(3) requires
the adoption to identify the exact candidate revision; the candidate currently
has none. Two of the spec's own requirements point at different bytes.
