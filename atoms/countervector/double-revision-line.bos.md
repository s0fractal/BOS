---
id: bos:countervector:double-revision-line
schema: bos.atom@v0.2
kind: countervector
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
  priority: bos:status:priority:now
title: Atom file with a revision line in both frontmatter and body
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
  construction: "Construct a .bos.md file whose frontmatter contains the revision line and whose Markdown body contains a code fence with an identical lexical line, plus a second fixture with an indented or commented look-alike line."
  expected_failure: "The bos-atom-file-v0.2 algorithm must unambiguously select the frontmatter-scoped match or reject the file; zero-match and multi-match behavior must be defined, not implementation-dependent."
  verification_class: mechanical
  verification:
    - "Fixture with body code-fence revision line: digest computed identically by two independent implementations."
    - "Fixture with indented and commented look-alike lines: defined reject or defined ignore."
---

# Double revision line

Step 6 of the revision algorithm says "single top-level lexical revision line"
without scoping the search to the frontmatter region delimited in step 4.
