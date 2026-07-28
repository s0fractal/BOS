---
id: bos:requirement:canonical-atom-bytes
schema: bos.atom@v0.3
kind: requirement
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
  priority: bos:status:priority:now
title: Atom revisions have one normative byte domain
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
  statement: "A BOS atom revision MUST be the SHA-256 of its exact normalized UTF-8 file bytes under the revision-placeholder algorithm defined by BOS-0001."
  level: MUST
  verification_class: mechanical
  verification:
    - "Reject BOM, CRLF, invalid UTF-8, missing final LF, and duplicate YAML keys."
    - "Require exactly one unindented revision field inside frontmatter for adopted atoms; ignore body look-alikes."
    - "Replace only its 64 lowercase hex digits with 64 zeroes before hashing the complete file."
    - "Require the computed digest to equal the declared revision."
    - "Require repository .gitattributes to pin .bos.md files to LF."
---

# Canonical atom bytes

The Markdown body is part of the atom revision. Human context cannot change
without changing content identity.
