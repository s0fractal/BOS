---
id: bos:vehicle:bos-0001
schema: bos.atom@v0.2
kind: vehicle
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
  priority: bos:status:priority:now
title: "BOS-0001 rev 2: Typed Decision Graph Core"
created_at: "2026-07-28T00:00:00Z"
created_by:
  - bos:actor:human:s0fractal
  - bos:actor:model:codex
scope: [bos, ecosystem]
disclosure:
  classification: public
  payload_mode: embedded
  retention: indefinite
relations:
  - predicate: derived_from
    object: bos:trajectory:kimi-bos-0001-rev1-review
payload:
  vehicle_kind: SPEC
  vehicle_revision: 2
  includes:
    - bos:status:governance:proposed
    - bos:status:maturity:research
    - bos:status:priority:now
    - bos:status:health:unknown
    - bos:status:freshness:current
    - bos:actor:human:s0fractal
    - bos:actor:model:codex
    - bos:actor:model:kimi-k3
    - bos:asset:repo:bos
    - bos:principle:projection-not-ssot
    - bos:principle:freedom-authority-separation
    - bos:claim:experience-is-trajectory
    - bos:goal:sustainable-model-autonomy
    - bos:hypothesis:agent-decision-evidence-commercial-wedge
    - bos:requirement:typed-atoms
    - bos:requirement:context-cut
    - bos:requirement:model-trajectory
    - bos:requirement:provenance-before-authority
    - bos:requirement:genesis-adoption
    - bos:requirement:canonical-atom-bytes
    - bos:requirement:first-class-contestable-relations
    - bos:requirement:verification-boundaries
    - bos:requirement:privacy-boundary
    - bos:risk:meta-recursion
    - bos:risk:false-replay
    - bos:risk:ontology-explosion
    - bos:risk:bootstrap-authority-cycle
    - bos:risk:undefined-canonical-bytes
    - bos:risk:embedded-contestable-relations
    - bos:risk:unenforceable-norms
    - bos:risk:immutable-sensitive-payload
    - bos:risk:supplied-read-confusion
    - bos:proposal:v0-bounded-scope
    - bos:evidence:review:kimi-bos-0001-rev1
    - bos:evidence:research:warrant-sigma-commercial-2026-07-28
    - bos:context_cut:bos-0001-rev1
    - bos:trajectory:kimi-bos-0001-rev1-review
    - bos:relation_claim:kimi-review-supports-bootstrap-risk
    - bos:relation_claim:experience-motivates-trajectory
    - bos:countervector:self-authorizing-genesis
    - bos:countervector:ambiguous-dirty-cut
    - bos:countervector:embedded-semantic-edge
    - bos:countervector:immutable-secret
---

# BOS-0001 rev 2 — Typed Decision Graph Core

Status: **GENESIS CANDIDATE / NOT ADOPTED**

Normative decoded-frontmatter schema:
[`bos.atom@v0.2`](../schemas/bos-atom-v0.2.schema.json).

Revision 1 is preserved by Git commit
`932077016f4544a6c455992ec93762dbc11c1b36`. Revision 2 incorporates the
adversarial Kimi trajectory
[`bos:trajectory:kimi-bos-0001-rev1-review`](../atoms/trajectory/kimi-bos-0001-rev1-review.bos.md).

## 0. Abstract

BOS is a typed, provenance-rich graph for coordinating repositories, research,
model trajectories, decisions, actions, and outcomes.

It preserves how different human and model actors understood a bounded
historical world. It permits rapid, plural proposal while keeping adoption and
material action behind explicit authority.

The kernel sentence is:

> A model may propose meaning freely; changing shared reality requires explicit
> authority and leaves a verifiable receipt.

BOS begins with a commercial hypothesis: independently verifiable evidence for
AI-agent decisions may be the strongest initial Warrant × Sigma product wedge.
That statement is the typed, expiring, falsifiable atom
[`bos:hypothesis:agent-decision-evidence-commercial-wedge`](../atoms/hypothesis/agent-decision-evidence-commercial-wedge.bos.md),
not permanent truth embedded in this specification.

## 1. Genesis and authority

### 1.1 No self-creation

BOS-0001 revision 2 is a **genesis candidate**. Its `MUST` statements describe
the contract that would apply after adoption; they do not manufacture the
authority that adopts them.

At the current revision:

- no BOS atom is adopted merely because it exists in this repository;
- governance state `proposed` is self-description, not authority;
- [`bos:proposal:v0-bounded-scope`](../atoms/proposal/v0-bounded-scope.bos.md)
  is a proposal, not a decision;
- V3 authority validation MUST NOT project this candidate as adopted.

### 1.2 Bootstrap act

The first adoption is deliberately external to BOS.

A valid genesis adoption MUST:

1. be an `adoption` atom with mode `genesis-human`;
2. name `bos:actor:human:s0fractal` as the bootstrap authority;
3. identify the exact candidate vehicle revision;
4. bind a clean Git context cut containing that revision and all included
   atoms;
5. be written only after an explicit human instruction to adopt, not merely an
   instruction to draft or amend;
6. appear in a later commit so the adopted candidate commit cannot include a
   self-referential adoption record.

No such atom exists yet. Independent re-gate of revision 2 comes first.

### 1.3 Post-genesis governance

Genesis authority is not intended to remain the permanent constitutional
mechanism. A later adopted contract MAY replace it with Warrant-governed
authority.

The migration MUST preserve:

- the external fact of genesis;
- exact historical bytes;
- the succession authority;
- losing or rejected governance paths.

## 2. Normative vocabulary

`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` have conventional RFC
meaning, but every requirement also declares one verification class:

- **mechanical** — deterministic validator or verifier;
- **adjudicated** — a named authority interprets evidence;
- **research** — the rule is not yet suitable as a gate.

A research or adjudicated requirement MUST NOT be presented as a deterministic
validator verdict.

The BOS process verbs map to schema objects:

| Verb | Schema realization | Authority effect |
|---|---|---|
| `OBSERVES` | `evidence`, `context_cut`, or `trajectory` plus structural `observes` | none |
| `CLAIMS` | `claim`, `hypothesis`, or `relation_claim` | none |
| `PROPOSES` | `proposal` | none |
| `RECOMMENDS` | `relation_claim` from reasons to a proposal | none |
| `DECIDES` | `decision` with authority and context cut | selects within named authority |
| `ADOPTS` | `adoption` over exact revision and authority | governance transition |
| `ACTS` | `action` bound to an authorized decision | may change target asset |
| `RECORDS` | `evidence` and/or `outcome` | proves only its declared evidence scope |

No verb is inferred from persuasive prose.

## 3. Scope

BOS v0.2 defines:

- strict semantic atom kinds and payloads;
- first-class actors and status axes;
- first-class contestable relation claims;
- immutable clean Git context cuts;
- per-actor supplied-context trajectories;
- genesis and later adoption boundaries;
- public-descriptor/private-payload rules;
- deterministic graph validation;
- bounded adjudication experiments.

BOS v0.2 is not:

- a universal event store;
- a replacement for Git, Warrant, Sigma, Trinity, registries, or law;
- an LLM attention monitor;
- deterministic replay of nondeterministic cognition;
- a global-consensus or complete-world oracle;
- a task-management UI;
- a spending daemon;
- a runtime for code embedded in Markdown.

## 4. Graph algebra

```text
BOS = (A, S, Q, C, T, V)
```

where:

- `A` is the set of typed atoms;
- `S` is the set of embedded structural relations;
- `Q ⊆ A` is the set of contestable `relation_claim` atoms;
- `C ⊆ A` is the set of immutable context cuts;
- `T ⊆ A` is the set of actor trajectories;
- `V` is a set of disposable projections over a declared input universe.

An active graph validator operates on an explicitly declared file/source
universe. It does not claim to know every trajectory or atom that exists
elsewhere.

## 5. Atom identity and canonical bytes

### 5.1 Identity layers

- `id` is stable semantic identity.
- `schema` is the decoder contract.
- path and filename are navigation aliases.
- `revision` is exact content identity.
- Git commit identifies a repository cut containing atom revisions.

Markdown links are human navigation hints. Machine relations use atom IDs.
Renaming a file may break a human link but MUST NOT create a new semantic ID.
The resolver maps IDs to paths and checks links separately.

Duplicate IDs are invalid in v0.2. No mirror exception exists.

### 5.2 Proposed versus adopted revisions

A proposed atom MAY omit `revision`.

An atom referenced by an adoption MUST contain exactly one top-level revision
field in this lexical form:

```yaml
revision: "sha256:<64 lowercase hexadecimal digits>"
```

### 5.3 `bos-atom-file-v0.2` revision algorithm

Revision bytes are the complete `.bos.md` file, including Markdown body, with
one normalization:

1. input MUST be valid UTF-8 with no BOM;
2. line endings MUST be LF;
3. the file MUST end in exactly one LF;
4. YAML frontmatter MUST start with `---` on byte 0 and end at the first later
   line exactly equal to `---`;
5. duplicate YAML mapping keys MUST be rejected;
6. locate the single top-level lexical `revision` line described above;
7. replace only its 64 digest digits with 64 ASCII `0` bytes, preserving every
   other byte;
8. compute SHA-256 over the resulting complete file bytes;
9. require the declared digest to equal the computed lowercase hex digest.

Decoded YAML canonicalization is not used for atom identity. Reordering
frontmatter or changing explanatory prose changes the revision.

The revision field is a placeholder-bound raw-file commitment, avoiding
self-reference without hiding body changes.

## 6. Context cuts

BOS v0.2 accepts only clean Git repository cuts:

```yaml
repositories:
  - asset: bos:asset:repo:bos
    commit: <40 lowercase hex>
    dirty: false
```

`dirty: true` is schema-invalid. BOS v0.2 deliberately has no custom
working-tree digest.

Uncommitted work may be explored, but it MUST be committed or captured as
content-addressed evidence before it can support an adopted decision or
material action.

A context cut commits what was available to an actor. It does not claim that
the actor internally attended to every supplied item.

Git, WarrantIDs, and Bitcoin block hashes may provide historical coordinates.
Wall-clock time alone is descriptive.

## 7. Type system

The v0.2 kind registry is closed:

| Kind | Role |
|---|---|
| `actor` | Human, model, or service identity descriptor |
| `asset` | Repository, contract, capability, implementation, release, research, or service |
| `claim` | Falsifiable confidence-bounded assertion |
| `hypothesis` | Claim explicitly awaiting experiment |
| `risk` | Harmful possibility with likelihood, impact, and mitigation |
| `requirement` | Norm with verification class and procedure |
| `evidence` | Located review, research, commit, test, source, or receipt |
| `proposal` | Unselected possible direction |
| `decision` | Selected direction under authority and context |
| `adoption` | Governance promotion of exact bytes |
| `action` | Intended or executed mutation |
| `outcome` | Observed consequence bound to evidence |
| `context_cut` | Immutable bounded input world |
| `trajectory` | One actor's supplied context and output path |
| `relation_claim` | Contestable semantic edge |
| `countervector` | Targeted construction expected to break a claim or contract |
| `principle` | Durable design constraint |
| `goal` | Desired condition with success signals |
| `vehicle` | WRT, ADR, SPEC, ROADMAP, RESEARCH, or RFC manifest |
| `status` | State descriptor on one orthogonal axis |

WRT/ADR/SPEC are vehicles. Risk/requirement/claim are semantic kinds. `FR-017`
may be a human alias, but its machine identity is a `bos:requirement:*` ID.

A future kind-registry change is a new schema version and requires adoption
under the authority active at that time. The genesis registry does not need to
authorize its own proposal.

### 7.1 Status axes

Status is not one scalar. The axes are governance, lifecycle, maturity,
priority, health, and freshness. No axis implies another.

The revision-2 genesis vocabulary includes:

- [`bos:status:governance:proposed`](../atoms/status/governance-proposed.bos.md);
- [`bos:status:maturity:research`](../atoms/status/maturity-research.bos.md);
- [`bos:status:priority:now`](../atoms/status/priority-now.bos.md);
- [`bos:status:health:unknown`](../atoms/status/health-unknown.bos.md);
- [`bos:status:freshness:current`](../atoms/status/freshness-current.bos.md).

Status atoms themselves bootstrap the vocabulary and therefore do not carry a
recursive `states` envelope. New values require a later schema/registry
adoption.

### 7.2 Scope vocabulary

The v0.2 scope labels are closed by schema:

```text
bos, ecosystem, autonomy, business, process, machine-experience,
privacy, warrant, sigma-glyph, trinity
```

They are routing labels, not authority domains. A future need for governed or
hierarchical scope identity requires first-class scope atoms and a new schema
version.

## 8. Actors and provenance

Actor references have one grammar:

```text
bos:actor:(human|model|service):<handle>
```

`created_by` is a non-empty array of actor references. A plus-concatenated
identity string is invalid.

An actor descriptor states the strength of its identity basis. A chat handle is
not a cryptographic principal. Model provider, hidden system context, exact
weights, and runtime MUST NOT be implied when not independently bound.

Genesis actor descriptors are candidates created under the explicit direction
of the repository owner. This fact is recorded rather than hidden.

## 9. Structural relations and relation claims

### 9.1 Embedded structural registry

Envelope `relations` may use only:

| Predicate | Intended topology |
|---|---|
| `contains` | asset → contained asset |
| `depends_on` | asset/proposal/action → prerequisite |
| `supersedes` | successor → historical predecessor |
| `derived_from` | atom → source/evidence/trajectory |
| `targets` | proposal/action/countervector → target |
| `produces` | trajectory/action → produced atom |
| `observes` | evidence/context/trajectory → observed object |
| `changes` | action/outcome → asset |
| `implements` | asset/action → requirement/proposal |
| `governed_by` | asset/decision/action → contract or authority |
| `binds` | adoption/decision/evidence → context or revision |

Structural relations carry no confidence. They describe the topology of the
record itself.

Vehicle membership has exactly one authority surface:
`vehicle.payload.includes`. A vehicle MUST NOT duplicate membership through
envelope `relations`. The list declares what the vehicle incorporates; it is
not a claim that every active atom in the repository belongs to the vehicle or
that the repository is a globally complete universe.

### 9.2 First-class semantic predicate registry

A `relation_claim` uses one of:

- `supports`;
- `refutes`;
- `mitigates`;
- `motivates`;
- `enables`;
- `conflicts_with`;
- `addresses`;
- `predicts`;
- `constrains`;
- `equivalent_to`.

It independently carries:

- subject;
- predicate;
- object;
- author through `created_by`;
- context cut;
- confidence;
- falsifier;
- optional evidence;
- optional expiry.

Changing or refuting the edge does not mutate either endpoint.

The validator enforces closed predicate vocabulary and reference integrity.
Semantic appropriateness beyond the declared domain/range table is an
adjudicated review obligation, not an invented oracle.

## 10. Trajectories and machine experience

A trajectory binds:

```text
actor
  + objective
  + context_cut
  + supplied_set
  → produced atoms
  + exact output evidence
  → optional selected action and receipt
```

`supplied_set` means the inputs exposed by the orchestrator. It does not claim
to reveal internal attention, hidden provider prompts, tokenizer behavior, or
model cognition.

Independent actor trajectories MUST remain distinct. A synthesis is a new atom
that names its sources; it does not overwrite them.

### 10.1 Recontextualization

BOS can preserve:

- the declared actor;
- the bounded supplied context;
- the captured output;
- later decisions that consumed it.

The word `replay` is reserved for computations whose relevant model/runtime,
parameters, randomness, and inputs are sufficiently bound for reproduction.
Otherwise the operation is **recontextualization**.

Sigma may replay deterministic subclaims. It does not make the surrounding LLM
trajectory deterministic.

## 11. Freedom and authority

Models may freely create:

- claims and hypotheses;
- relation claims;
- risks and countervectors;
- requirements and proposals;
- critiques and syntheses.

Model output alone cannot:

- adopt itself;
- grant capability;
- merge governed branches;
- publish a release;
- spend money;
- delete a competing trajectory;
- convert confidence into authority.

A decision requires reasons, authority, and context cut. A material action
requires a decision, target, acceptance conditions, and outcome evidence.

Warrant is the intended later authority carrier. BOS consumes pinned Warrant
verification surfaces; it does not reimplement settlement.

## 12. Privacy and retention

Every atom declares:

- classification;
- payload mode;
- retention intent.

Public and internal payloads may be embedded subject to repository policy.
Confidential or secret payloads MUST use:

- `payload_mode: commitment`;
- SHA-256 commitment;
- controlled private locator;
- encryption descriptor.

The public atom contains only a safe descriptor. The sensitive bytes stay
outside the immutable public graph.

A tombstone or superseding atom can change current views. It cannot guarantee
erasure of plaintext already copied to a clone, cache, or evidence bundle.
Therefore plaintext secrets MUST NOT enter immutable atoms.

## 13. Freshness

Context cuts do not expire; they describe history.

Claims, relation claims, and evidence may carry `valid_until`. A freshness view
derives staleness when:

- `valid_until` passes;
- a watched source commitment changes;
- a later atom explicitly refutes or supersedes the assertion.

Freshness is a projection. An embedded `freshness: current` status cannot
override an expired payload.

## 14. Validation boundary

### V0 — mechanical syntax

- strict UTF-8/LF/frontmatter;
- duplicate YAML keys rejected;
- closed schema and payload;
- disclosure contract;
- canonical revision where required.

### V1 — mechanical graph

- unique IDs;
- every actor, state, relation, payload reference resolves;
- status axis matches status payload axis;
- structural predicate registry;
- vehicle membership has one representation;
- context cuts are clean;
- evidence digests match repository-local locators where applicable.

### V2 — mechanical temporal scope

- trajectory context and supplied set resolve in its declared cut;
- later atoms are not silently projected as earlier supplied inputs;
- views declare their input universe.

Historical Git lookup is required to fully validate old cuts. Until implemented,
cross-revision cut membership remains an adjudicated limitation and MUST NOT be
reported as mechanically complete.

### V3 — authority

- proposal is not decision;
- decision names authority and context;
- adoption names exact revision and authority;
- action names an authorized decision;
- adopted revisions are immutable.

Before genesis adoption, V3 must report `genesis candidate`, never `adopted`.

### V4 — external contracts

Warrant, Sigma, Trinity, registry, and external-clock results are authoritative
only when represented as pinned contract/assets and verified through their own
published interfaces.

The integration prose in this revision is informative until Phase 1 registers
those exact assets and contract revisions.

## 15. Views and completeness

A view MUST declare:

- derivation version;
- context cut;
- exact source/atom universe;
- whether it claims completeness relative to that universe.

Completeness means:

> every qualifying object in declared universe U under cut C was included.

It never means “every trajectory that exists globally”.

Initial views:

- asset/capability map;
- decision spine;
- per-actor trajectories;
- bounded frontier and blockers;
- staleness;
- commercial hypothesis → experiment → outcome.

## 16. Countervectors

Mechanical countervectors are first-class atoms. Revision 2 already includes:

- self-authorizing genesis;
- ambiguous dirty cut;
- embedded semantic edge;
- immutable plaintext secret.

Further validator tests must cover:

- unknown kind or payload field;
- duplicate ID;
- unresolved actor/state/relation;
- wrong status axis;
- semantic predicate embedded structurally;
- confidential embedded payload;
- malformed revision bytes;
- decision without authority/context;
- adoption without exact revision;
- trajectory using `read_set` instead of `supplied_set`;
- duplicated vehicle membership.

Semantic concerns such as “does this commercial claim really address this
market?” are adjudicated or research countervectors, not schema failures.

## 17. Ecosystem boundaries

### Trinity

Trinity remains the general cognitive/process substrate. BOS is the bounded
ecosystem and strategy projection. BOS may export process objects; it must not
fork a second general journal before E0001 demonstrates need.

### Warrant

Warrant carries authorization and settlement. BOS carries the strategic,
causal, and multi-actor context around a Warrant decision.

### Sigma

Sigma executes deterministic bounded reasons. BOS records which atom a Sigma
result supports and under which cut.

### Git and Bitcoin

Git provides repository history and clean context cuts. Bitcoin may strengthen
external historical anchoring. Neither provides semantic authority by itself.

## 18. Phase gates

### Phase 0 — typed graph

Exit only when:

- repository validator checks V0 and V1;
- permanent negative tests exercise Kimi's mechanical countervectors;
- all active atoms and links resolve;
- rev 2 receives an independent design re-gate;
- the human explicitly chooses whether to perform genesis adoption.

### Phase 1 — ecosystem observations

Exit only when:

- Warrant, Sigma, Trinity, and BOS are registered as assets;
- exact consumed contracts and commits are pinned;
- one asset/capability view is reproducible.

### Phase 2 — multi-model trajectory

Exit only when BOS-E0001 contains at least three independent trajectories and a
fourth evaluator, using the rubric below.

### Phase 3 — Warrant authority bridge

Exit only when proposal→decision→action/adoption is verified through a pinned
Warrant contract with negative vectors for self-promotion and wrong authority.

### Phase 4 — Sigma reason bridge

Exit only when at least one claim cites a deterministic Sigma result that a
second implementation reproduces from pinned bytes.

### Phase 5 — bounded economic autonomy

Exit only when external value, budget authority, spending bounds, receipts, and
human/governed veto paths are separately specified and tested.

No phase transition occurs merely because time passed or prose was written.

## 19. BOS-E0001 adjudication rubric

A fresh evaluator receives only the bounded graph projection. For each of the
eight experiment questions it must:

1. answer with at least one resolvable atom ID;
2. distinguish observation, claim, proposal, decision, action, and outcome;
3. identify actor and context cut where requested;
4. state `unknown` rather than invent missing authority or evidence.

Pass requires:

- 8/8 questions answered or correctly marked unknown;
- zero proposal-as-decision errors;
- zero test-evidence-as-product-outcome errors;
- zero recontextualization-as-replay errors;
- human adjudicator and one model evaluator independently agree on the category
  labels, with disagreements preserved.

This is an adjudicated experiment, not a deterministic semantic oracle.

## 20. Commercial purpose

The current commercial direction is represented by:

- time-bounded research evidence
  [`bos:evidence:research:warrant-sigma-commercial-2026-07-28`](../atoms/evidence/commercial-warrant-sigma-research.bos.md);
- the falsifiable hypothesis
  [`bos:hypothesis:agent-decision-evidence-commercial-wedge`](../atoms/hypothesis/agent-decision-evidence-commercial-wedge.bos.md);
- the goal
  [`bos:goal:sustainable-model-autonomy`](../atoms/goal/sustainable-model-autonomy.bos.md).

BOS does not define commercial success as graph growth. Relevant external
signals include:

- an outside party verifies an Evidence Pack;
- a real integration records a bounded agent decision;
- a design partner changes audit, procurement, or underwriting behavior;
- revenue supports the human steward and an explicit model/research budget;
- a falsified hypothesis prevents wasted implementation.

## 21. Stop rule

Freeze ontology work and return to BOS-E0001 or an external product experiment
if either occurs:

1. two consecutive schema/spec revisions add no consumer query, mechanical
   countervector, or external decision use case; or
2. a validator is introduced only to validate another validator and protects no
   declared V0–V4 boundary.

Before Phase 2, no new kind may be added after v0.2 unless a counterexample
shows that every existing kind loses required semantics.

This is a mechanical repository-history trigger plus human adjudication of the
consumer criterion. It is not an autonomous global oracle.
