---
id: bos:risk:supplied-read-confusion
schema: bos.atom@v0.2
kind: risk
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: Supplied model context is misreported as internally read
created_at: "2026-07-28T00:00:00Z"
created_by:
  - bos:actor:model:kimi-k3
scope: [bos, machine-experience]
disclosure:
  classification: public
  payload_mode: embedded
  retention: indefinite
relations:
  - predicate: derived_from
    object: bos:evidence:review:kimi-bos-0001-rev1
payload:
  statement: "The orchestrator can bind supplied inputs but generally cannot observe model attention, hidden prompts, tokenization effects, or internal reads."
  likelihood: high
  impact: high
  mitigation:
    - "Use supplied_set rather than read_set."
    - "Record known hidden-context limitations in actor and trajectory evidence."
  evidence:
    - bos:evidence:review:kimi-bos-0001-rev1
---

# Supplied versus read

Provenance must stop at the boundary of what the system can actually observe.
