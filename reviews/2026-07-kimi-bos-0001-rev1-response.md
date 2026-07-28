# BOS-0001 rev 2 response to Kimi

Date: 2026-07-28

Revision 1 cut:
`932077016f4544a6c455992ec93762dbc11c1b36`

Verdict accepted: **AMEND**.

## Architectural closure

| Kimi finding | BOS-0001 revision 2 |
|---|---|
| Bootstrap/adoption cycle | Revision 2 is explicitly a genesis candidate. Nothing is adopted yet. First adoption is a later external human act over an exact clean commit; later Warrant succession is separate. |
| Scope “decision” had no authority | Retyped as `bos:proposal:v0-bounded-scope`; proposals have no authority effect. |
| Adoption contract absent | Added `adoption` kind, `genesis-human`/`warrant` modes, subject revision, authority, and context cut. Validator rejects mismatched authority/revision shapes. |
| Revision bytes undefined | Added `bos-atom-file-v0.2`: exact UTF-8/LF whole-file bytes, one revision placeholder, Markdown body included, SHA-256 checked. |
| Dirty-tree digest undefined | Removed from v0.2. Context-cut schema accepts only clean full Git commits. |
| Predicate registry absent | Split closed structural registry from closed semantic relation-claim registry; validator checks domain/range. |
| Relations not first-class | Added `relation_claim` with subject/predicate/object, author, context, confidence, falsifier, evidence, and expiry. |
| Process verbs decorative | Mapped OBSERVES/CLAIMS/PROPOSES/RECOMMENDS/DECIDES/ADOPTS/ACTS/RECORDS to schema kinds and authority effects. |
| Actor grammar undefined | Added first-class actors; `created_by` is a non-empty array of `bos:actor:(human|model|service):handle` references. |
| Undefined-oracle MUSTs | Added `mechanical`, `adjudicated`, and `research` verification classes. Global completeness and NLP prose-conflict gates were removed. |
| Duplicate `includes` | Vehicle membership exists only in `payload.includes`; embedded vehicle membership is rejected. |
| Commercial claims in core prose | Added time-bounded research evidence and a confidence/falsifier-bearing commercial hypothesis atom. |
| Inconsistent aliases | Normative examples use `bos:*` IDs; FR/RISK short labels are explicitly human aliases only. |
| Countervector not a kind | Added first-class `countervector` and permanent executable negative tests. |
| `read_set` overclaimed observability | Replaced with `supplied_set`; trajectory explicitly disclaims model attention visibility. |
| ID versus path ambiguity | IDs are machine references; Markdown paths are non-authoritative navigation hints checked separately. |
| Freshness undefined | Context cuts remain history; assertions/evidence use `valid_until` or source/supersession signals for derived staleness. |
| External contracts unpinned | Current integration prose is informative only. V4 requires pinned assets/contracts in Phase 1. |
| Status registry unlinked | Status atoms are included and linked from the specification; axes remain orthogonal. |
| Mirror rule undefined | Removed. Duplicate IDs are invalid in v0.2. |
| Privacy absent | Added disclosure envelope and public-descriptor/private-payload commitment rule; secret/confidential embedded mode is schema-invalid. |
| Phase gates vague | Every phase now has explicit exit evidence. |
| Proof obligation was a vibe test | BOS-E0001 has an eight-question adjudication rubric with category-confusion failure conditions. |

## Dogfood evidence

Kimi's review is now represented by:

- exact revision-1 Git context cut;
- actor descriptor;
- repository-local review evidence and source digest;
- trajectory with `supplied_set` and produced atoms;
- six risk atoms;
- four countervectors;
- a first-class relation claim connecting review evidence to bootstrap risk.

## Mechanical gate

`tools/bos_validate.py` validates V0/V1 boundaries:

- strict bytes/frontmatter and duplicate-key rejection;
- closed schema;
- ID and reference integrity;
- actor and status-axis integrity;
- structural and semantic predicate domains;
- clean context cuts;
- privacy envelope;
- local evidence digests;
- revision algorithm;
- body links.

Permanent tests exercise the clean graph plus the Kimi-derived negative cases.

## Honest remainder

- Revision 2 is not adopted.
- Historical membership validation across arbitrary Git cuts is not yet
  implemented and is not reported as mechanical completeness.
- Warrant, Sigma, and Trinity contract assets remain Phase 1.
- Semantic truth and global trajectory completeness remain outside the
  deterministic validator.
- Genesis adoption must wait for independent re-gate and an explicit human
  instruction to adopt exact bytes.
