---
id: bos:risk:revision-lexical-ambiguity
schema: bos.atom@v0.2
kind: risk
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
  priority: bos:status:priority:now
title: Revision digest algorithm is lexically ambiguous and platform-fragile
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
  statement: "Step 6 of the bos-atom-file-v0.2 algorithm says to locate the single top-level lexical revision line but does not scope the search to the frontmatter region. A Markdown body code fence can contain a matching line, producing multiple matches with undefined behavior. Indented or commented matches are also undefined. Separately, LF-only verification breaks on checkouts with core.autocrlf=true, so two conforming tools can compute different digests for the same atom."
  likelihood: medium
  impact: high
  mitigation:
    - "Scope the revision-line search to the frontmatter block delimited in step 4 and define rejection on zero or multiple matches."
    - "Define handling of indented, quoted, and commented look-alike lines."
    - "Add a normative .gitattributes rule (text eol=lf for .bos.md) to the V0 layer."
  evidence:
    - bos:evidence:review:kimi-bos-0001-rev2
---

# Revision digest ambiguity

Content identity is the foundation of adoption and immutability; its algorithm
must not tolerate undefined cases or platform-dependent bytes.
