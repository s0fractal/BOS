---
id: bos:vehicle:bos-0001
schema: bos.atom@v0
kind: vehicle
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
  priority: bos:status:priority:now
title: "BOS-0001: Typed Decision Graph Core"
created_at: "2026-07-28T00:00:00Z"
created_by: human:s0fractal+model:codex
scope: [bos, ecosystem]
relations:
  - predicate: includes
    object: bos:principle:projection-not-ssot
  - predicate: includes
    object: bos:principle:freedom-authority-separation
  - predicate: includes
    object: bos:claim:experience-is-trajectory
  - predicate: includes
    object: bos:goal:sustainable-model-autonomy
  - predicate: includes
    object: bos:requirement:typed-atoms
  - predicate: includes
    object: bos:requirement:context-cut
  - predicate: includes
    object: bos:requirement:model-trajectory
  - predicate: includes
    object: bos:requirement:provenance-before-authority
  - predicate: includes
    object: bos:risk:meta-recursion
  - predicate: includes
    object: bos:risk:false-replay
  - predicate: includes
    object: bos:risk:ontology-explosion
  - predicate: includes
    object: bos:decision:v0-bounded-scope
payload:
  vehicle_kind: SPEC
  includes:
    - bos:principle:projection-not-ssot
    - bos:principle:freedom-authority-separation
    - bos:claim:experience-is-trajectory
    - bos:goal:sustainable-model-autonomy
    - bos:requirement:typed-atoms
    - bos:requirement:context-cut
    - bos:requirement:model-trajectory
    - bos:requirement:provenance-before-authority
    - bos:risk:meta-recursion
    - bos:risk:false-replay
    - bos:risk:ontology-explosion
    - bos:decision:v0-bounded-scope
---

# BOS-0001 — Typed Decision Graph Core

Status: **PROPOSED / RESEARCH**
Audience: humans and model actors coordinating the s0fractal ecosystem
Normative schema: [`bos-atom-v0.schema.json`](../schemas/bos-atom-v0.schema.json)

## Abstract

BOS is a typed, provenance-rich graph for coordinating repositories, research,
model trajectories, decisions, actions, and outcomes.

Its commercial starting objective is to help turn the research in
`raw/Комерційне застосування Warrant × Σ-GLYPH — дип-ресерч/` and its independent
model variations into externally useful Warrant × Sigma products. Its deeper
objective is to let multiple model actors reason freely over a shared ecosystem
without letting persuasive output silently become authority.

BOS does not attempt to make one model the canonical planner. It preserves
independent trajectories, makes their inputs historically explicit, and binds
material actions to explicit decision authority.

The core sentence is:

> A model may propose meaning freely; changing shared reality requires explicit
> authority and leaves a verifiable receipt.

## 1. Normative language modified for BOS

`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` have their conventional
RFC meaning.

BOS additionally distinguishes verbs that ordinary RFCs often collapse:

- **OBSERVES** — records a source in a bounded context without endorsing it.
- **CLAIMS** — makes a falsifiable or confidence-bounded assertion.
- **PROPOSES** — offers a possible graph change with no authority effect.
- **RECOMMENDS** — ranks a proposal for an identified actor or objective.
- **DECIDES** — selects a path under named authority.
- **ACTS** — changes an external or shared asset.
- **ADOPTS** — promotes an atom into the governed shared contract.
- **RECEIPTS** — records evidence that an action or transition occurred.

An actor that may `PROPOSE` does not thereby have permission to `DECIDE`, `ACT`,
or `ADOPT`.

## 2. Normative atoms consumed by this specification

BOS-0001 is a vehicle. Its load-bearing semantics live in separately
addressable atoms:

### Principles and goal

- [`bos:principle:projection-not-ssot`](../atoms/principle/projection-not-ssot.bos.md)
- [`bos:principle:freedom-authority-separation`](../atoms/principle/freedom-authority-separation.bos.md)
- [`bos:goal:sustainable-model-autonomy`](../atoms/goal/sustainable-model-autonomy.bos.md)

### Claim

- [`bos:claim:experience-is-trajectory`](../atoms/claim/experience-is-trajectory.bos.md)

### Requirements

- [`bos:requirement:typed-atoms`](../atoms/requirement/typed-atoms.bos.md)
- [`bos:requirement:context-cut`](../atoms/requirement/context-cut.bos.md)
- [`bos:requirement:model-trajectory`](../atoms/requirement/model-trajectory.bos.md)
- [`bos:requirement:provenance-before-authority`](../atoms/requirement/provenance-before-authority.bos.md)

### Known risks

- [`bos:risk:meta-recursion`](../atoms/risk/meta-recursion.bos.md)
- [`bos:risk:false-replay`](../atoms/risk/false-replay.bos.md)
- [`bos:risk:ontology-explosion`](../atoms/risk/ontology-explosion.bos.md)

### Scope decision

- [`bos:decision:v0-bounded-scope`](../atoms/decision/v0-bounded-scope.bos.md)

If prose in this document conflicts with one of those atoms, the conflict MUST
be made explicit. A model MUST NOT silently select whichever wording better
supports its intended action.

## 3. Scope

### 3.1 BOS v0 does

BOS v0:

1. defines strict semantic atom kinds;
2. separates semantic kinds, document vehicles, and status axes;
3. records upstream assets without replacing their authority;
4. binds model work to immutable historical context cuts;
5. preserves different model trajectories without forced consensus;
6. connects reasons, authority, actions, and outcomes;
7. produces reconstructable read-only views;
8. supports countervector-driven validation of the graph itself.

### 3.2 BOS v0 does not

BOS v0 is not:

- a universal event store;
- a replacement for Git, GitHub, registries, Warrant, or Trinity;
- a task-management UI;
- an autonomous bank account or spending daemon;
- a deterministic replay engine for LLM cognition;
- a claim that a typed graph makes its contents true;
- a runtime for executable Python embedded in Markdown;
- a global-consensus protocol.

These exclusions are deliberate protection against
[`bos:risk:meta-recursion`](../atoms/risk/meta-recursion.bos.md).

## 4. Core algebra

A BOS space is:

```text
BOS = (A, R, C, T, V)
```

where:

- `A` is a set of typed atoms;
- `R` is a set of typed directed relations between atoms;
- `C ⊆ A` is the set of immutable context cuts;
- `T ⊆ A` is the set of actor trajectories;
- `V` is a set of deterministic, disposable views over `A` and `R`.

Views are not atoms merely because they are rendered. A view becomes evidence
only when its exact bytes, derivation, and observation context are themselves
captured.

Current state is a projection. Historical meaning is reconstructed from atoms,
relations, context cuts, decisions, and receipts.

## 5. Atom envelope

Every normative atom MUST decode from its Markdown frontmatter into
[`bos.atom@v0`](../schemas/bos-atom-v0.schema.json).

The envelope has:

```yaml
id: bos:<kind>:<stable-name>
schema: bos.atom@v0
kind: claim
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: Human-readable title
created_at: "2026-07-28T00:00:00Z"
created_by: model:example
scope: [bos]
revision: "sha256:<optional canonical revision hash>"
relations: []
payload: {}
```

### 5.1 Identity

- `id` is semantic identity.
- Filename and path are mutable navigation aliases.
- `schema` is the decoder contract, not the atom identity.
- `revision`, when present, binds a canonical envelope and payload revision.

Two files with the same `id` are a conflict unless one is a byte-identical
mirror under an explicitly governed mirror rule.

Changing `@v0` to `@v1` changes the schema. It does not automatically create a
new real-world asset or supersede the old claim.

### 5.2 Mutation

Before adoption, a proposed atom MAY be revised in Git.

Once an atom becomes governed/adopted:

- its accepted revision MUST be content-addressed;
- historical bytes MUST remain resolvable;
- a semantic replacement MUST be a new revision or successor atom;
- the replacement MUST name what it supersedes and why;
- derived views MUST retain the losing or superseded history.

BOS-0001 does not yet define the adoption byte contract. Until that contract is
integrated with Warrant, all new atoms in this draft remain proposed.

### 5.3 Atomicity

An atom SHOULD carry one independently contestable meaning.

Good atoms:

- one risk;
- one requirement;
- one claim;
- one decision;
- one evidence item;
- one action;
- one outcome.

WRT, ADR, SPEC, ROADMAP, and RESEARCH are **vehicles** that include atoms. A
vehicle MAY contain explanatory prose, but a normative statement that affects
implementation or authority SHOULD be promoted into an addressable atom.

## 6. Type system

### 6.1 Semantic kinds

The v0 kind registry is closed:

| Kind | Meaning |
|---|---|
| `asset` | Repository, capability, specification, implementation, release, service, dataset, or research asset |
| `claim` | Falsifiable assertion with confidence |
| `hypothesis` | Claim explicitly awaiting experiment |
| `risk` | Possible harmful condition with likelihood, impact, and mitigation |
| `requirement` | Normative constraint with verification |
| `evidence` | Located, observed support, refutation, report, receipt, or source |
| `decision` | Selection under named authority and reasons |
| `action` | Intended or executed mutation of an asset |
| `outcome` | Observed consequence bound to evidence |
| `context_cut` | Immutable set of source states visible to an actor |
| `trajectory` | One actor's path from a context cut to produced atoms/actions |
| `principle` | Durable design constraint |
| `goal` | Desired future condition with success signals |
| `vehicle` | WRT, ADR, SPEC, ROADMAP, RESEARCH, or RFC manifest |
| `status` | First-class state descriptor on one orthogonal axis |

A new kind requires:

1. a query that existing kinds cannot answer without semantic loss;
2. a closed payload schema;
3. at least one positive example;
4. at least two confusing-neighbor counterexamples;
5. a decision atom authorizing registry expansion.

### 6.2 Vehicles are not semantic assertions

`WRT`, `ADR`, and `SPEC` answer “what kind of governed document assembles these
atoms?” `risk`, `requirement`, and `claim` answer “what semantic role does this
atom play?”

Therefore:

```text
WRT-002 includes RISK-008 and FR-017
```

is meaningful, while:

```text
WRT-002 is a subtype of RISK
```

is not.

### 6.3 Status axes

Statuses are first-class atoms, but state axes remain distinct:

- governance;
- lifecycle;
- maturity;
- priority;
- health;
- freshness.

`active` MUST NOT simultaneously mean adopted, implemented, high-priority, and
healthy.

An atom may be:

```yaml
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
  priority: bos:status:priority:now
  health: bos:status:health:unknown
  freshness: bos:status:freshness:current
```

No axis implies the value of another.

## 7. Relations

Relations are typed, directed, and attributable through the containing atom.

Important distinctions:

- `depends_on` is a structural claim;
- `supports` and `refutes` connect evidence or claims;
- `motivates` does not mean “proves”;
- `authorizes` is invalid without a recognized authority path;
- `changes` connects action to asset;
- `supersedes` preserves rather than deletes history.

“Feature X solves market force Y” MUST NOT be stored as an unqualified
structural edge. It is a strategic claim with author, evidence, confidence,
time, and falsifier.

The v0 validator MUST eventually enforce predicate domain/range rules in
addition to the JSON Schema vocabulary.

## 8. Context cuts

A `context_cut` defines the world available to one trajectory.

It may bind:

- full Git commit hashes;
- dirty working-tree digests;
- content-addressed research/evidence atoms;
- WarrantIDs;
- Bitcoin height plus block hash;
- wall-clock timestamps as descriptive coordinates.

Example:

```yaml
kind: context_cut
payload:
  repositories:
    - asset: bos:asset:repo:warrant
      commit: 0123456789abcdef0123456789abcdef01234567
      dirty: false
  sources:
    - bos:evidence:research:commercial-warrant-sigma
  anchors:
    - kind: bitcoin
      value: "height=<n>;block=<hash>"
```

A context cut MUST NOT claim completeness beyond the sources it commits.

A dirty repository with no working-tree digest is not a reproducible cut and
MUST be rejected for any trajectory that may authorize material action.

## 9. Trajectories and machine experience

A trajectory binds:

```text
actor
  + objective
  + context cut
  + read set
  → produced atoms
  → optional selected action
  → optional receipt
```

Claude, Codex, Gemini, Kimi, and human trajectories MUST remain distinct even
when they converge.

A synthesis:

- is a new atom;
- names the trajectories it derives from;
- does not rewrite those trajectories;
- states what was discarded or compressed.

### 9.1 Recontextualization, not invented determinism

For an ordinary LLM, BOS can prove:

- which preserved context was supplied;
- which output was captured;
- which actor identity or service was claimed;
- which later decision used the output.

It generally cannot prove that a future invocation will emit the same output.

The word **replay** MUST be reserved for a computation whose model, weights,
runtime, parameters, randomness, and inputs are sufficiently bound to reproduce
the result. Otherwise BOS MUST use **recontextualize**.

Sigma may provide deterministic replay for bounded subclaims. It does not make
the surrounding LLM trajectory deterministic.

## 10. Freedom, authority, and action

### 10.1 Proposal freedom

Within resource and privacy bounds, model actors MAY:

- create claims and hypotheses;
- identify risks;
- propose requirements and actions;
- construct countervectors;
- rank alternatives;
- criticize existing decisions;
- synthesize new strategy vehicles.

### 10.2 Authority boundary

Model actors MUST NOT, solely by producing output:

- mark their atom adopted;
- grant themselves capabilities;
- spend money;
- merge governed branches;
- publish releases;
- delete competing trajectories;
- represent confidence as authority.

### 10.3 Material actions

A material action MUST identify:

1. the target asset;
2. the decision that authorizes it;
3. the actor/capability performing it;
4. acceptance conditions;
5. outcome evidence or a bounded failure receipt.

Warrant is the intended authority and receipt carrier. BOS MUST consume Warrant
results rather than reimplement Warrant settlement semantics.

## 11. Ecosystem integration

### 11.1 Trinity

Trinity is the broader cognitive/process substrate: perception, proposal,
experiment, receipt, formula, crystal, compost, and voice memory.

BOS is the bounded ecosystem/portfolio projection. BOS SHOULD be able to export
its atoms into Trinity-compatible process objects, but BOS-0001 MUST NOT fork a
second general-purpose journal runtime.

### 11.2 Warrant

Warrant answers:

- who signed or authorized a decision;
- under which policy;
- whether the record verifies and settles.

BOS answers:

- which strategic claims and risks informed that decision;
- which model trajectories proposed alternatives;
- what ecosystem asset and objective the decision changed.

### 11.3 Sigma

Sigma executes deterministic, bounded reasons where applicable. BOS records
which claim a Sigma result supports and in which context it was consumed.

Sigma MUST NOT be used as theatre around a reason that remains prose.

### 11.4 Git and external clocks

Git commits are initial repository cuts and history receipts. Bitcoin or other
external anchors MAY strengthen historical ordering. Neither substitutes for
semantic authority.

## 12. Views

All views are derived and disposable.

Initial useful views:

1. **Asset map** — repositories, capabilities, specifications, releases.
2. **Decision spine** — claim/risk → decision → action → outcome.
3. **Model trajectories** — independent colored paths through one decision.
4. **Frontier** — proposed work and explicit blockers.
5. **Staleness view** — claims whose sources or context cuts have expired.
6. **Commercial path** — research hypothesis → product experiment → external
   evidence → revenue/outcome.

A view MUST identify its source set and derivation version. Omitting a rival
trajectory while claiming completeness is a verification failure.

## 13. Validation layers

BOS validation is layered:

### V0 — syntax

- frontmatter parses;
- schema is known;
- closed JSON Schema passes;
- UTF-8 and duplicate-key rules are explicit.

### V1 — graph integrity

- atom IDs are unique;
- all referenced IDs resolve;
- relation domain/range rules hold;
- all state atoms exist on the correct axis;
- vehicles include resolvable atoms.

### V2 — temporal integrity

- repository cuts use full commits;
- dirty cuts carry a working-tree digest;
- evidence observations have time and/or content identity;
- a trajectory reads no atom created outside its cut unless explicitly marked
  as later adjudication.

### V3 — authority integrity

- proposals do not self-promote;
- decisions name authority and reasons;
- actions bind decisions;
- outcomes bind evidence;
- adopted revisions cannot be silently rewritten.

### V4 — external verification

- Warrant verification, Sigma execution, CI reports, and external anchors are
  consumed through their own published verification surfaces.

BOS MUST NOT claim V4 merely because V0–V3 pass.

## 14. Required countervectors

Before BOS-0001 can move beyond research, permanent tests SHOULD demonstrate
rejection or explicit bounded handling of:

1. unknown atom kind;
2. unknown payload field;
3. duplicate atom ID under another filename;
4. unresolved relation;
5. status from the wrong axis;
6. a single `active` value used to imply governance and health;
7. strategic score without method, source, date, and confidence;
8. model output that self-declares adoption;
9. action with no authority decision;
10. decision with no reason atom;
11. dirty repository cut without a working-tree digest;
12. later research silently inserted into an older trajectory;
13. nondeterministic LLM output described as replayable;
14. view that omits a competing model trajectory;
15. accepted atom silently edited in place;
16. WRT/ADR prose containing an implementation-changing `MUST` with no
    addressable requirement atom;
17. graph growth that produces no answer to an active decision query.

## 15. Commercial purpose

BOS begins from the research thesis:

> Build an evidence layer for AI-agent decisions using Warrant × Sigma, sold
> through compliance, insurance, disputes, and eventually verified precedent.

This thesis is not adopted truth. It is a family of model-generated strategic
claims to be decomposed, compared, tested, and revised.

BOS succeeds commercially when it helps produce evidence that exists outside
the graph:

- an external user verifies an Evidence Pack;
- an integration records a real bounded agent decision;
- a design partner changes procurement, audit, or underwriting behavior;
- revenue funds the human steward and model/research compute;
- a rejected commercial hypothesis is preserved early enough to prevent wasted
  implementation.

Graph size, atom count, model-message count, and internal agreement are not
commercial success metrics.

## 16. Phased implementation

### Phase 0 — typed documents

- closed atom schema;
- stable IDs;
- referential-integrity validator;
- read-only graph projection;
- no embedded executable hooks.

### Phase 1 — ecosystem observations

- register `warrant`, `sigma-glyph`, `trinity`, and `BOS` as assets;
- import commit/release/capability observations;
- distinguish implemented, proposed, governed, and stale surfaces.

### Phase 2 — multi-model trajectories

- give multiple models the same sealed context cut and objective;
- preserve independent read/produce paths;
- compare convergence, disagreement, omissions, and countervectors.

### Phase 3 — authority bridge

- bind selected decisions and actions to Warrant verification;
- keep proposal freedom separate from governed mutation.

### Phase 4 — deterministic reason bridge

- attach Sigma checks only to claims that can honestly be executed;
- preserve prose and semantic research as non-executable where necessary.

### Phase 5 — bounded economic autonomy

- define spending and action capabilities;
- fund model work from explicit budgets;
- require receipts and measurable external outcomes;
- retain human and governed veto paths.

Each phase requires a separate adoption decision. Passing an earlier phase does
not authorize the next.

## 17. First proof obligation

A fresh model, given only a bounded BOS projection for one real ecosystem
decision, should answer:

1. What actually exists?
2. What is only proposed or hypothesized?
3. Why is this work prioritized now?
4. What blocks the next transition?
5. What evidence would make the work complete?
6. Which actors proposed different paths, and from which context?
7. Who had authority to select and execute the final path?
8. What outcome followed?

If the model must read the complete chat history and every repository to answer,
BOS has not yet compressed experience usefully.

## 18. Stop rule

BOS work MUST stop and return to an external product or decision experiment
when:

- a schema iteration has no new consumer query;
- a validator only validates another validator without protecting a declared
  decision boundary;
- active atoms grow faster than resolved decisions;
- no external outcome has been observed for the current strategy;
- the ontology begins duplicating a Trinity, Warrant, Sigma, Git, or task-system
  contract rather than referencing it.

This rule is part of the architecture. It is not project-management advice.
