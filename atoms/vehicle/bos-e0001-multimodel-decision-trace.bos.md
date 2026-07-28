---
id: bos:vehicle:bos-e0001
schema: bos.atom@v0.3
kind: vehicle
states:
  governance: bos:status:governance:proposed
  lifecycle: bos:status:lifecycle:recorded
  maturity: bos:status:maturity:research
title: "BOS-E0001: Multi-model decision trace"
created_at: "2026-07-28T00:00:00Z"
created_by:
  - bos:actor:human:s0fractal
  - bos:actor:model:codex
scope: [bos, ecosystem, machine-experience]
disclosure:
  classification: public
  payload_mode: embedded
  retention: review
relations:
  - predicate: depends_on
    object: bos:vehicle:bos-0001
payload:
  vehicle_kind: RESEARCH
  vehicle_revision: 1
  includes:
    - bos:claim:experience-is-trajectory
    - bos:principle:freedom-authority-separation
    - bos:requirement:context-cut
    - bos:requirement:model-trajectory
    - bos:requirement:provenance-before-authority
    - bos:risk:meta-recursion
    - bos:proposal:v0-bounded-scope
---

# BOS-E0001 — Multi-model decision trace

Status: **PROPOSED / NOT EXECUTED**

## Question

Can a fresh model reconstruct one real ecosystem decision from typed atoms and
trajectories without reading the full chats or every repository?

## Case

Use the real decision boundary around:

- the `warrant` release-surface gate;
- its adoption-surface dependency;
- the consciously frozen WRT-002 work;
- the point where continued adversarial review became meta-verification.

The case contains multiple model actors, repeated countervectors,
architecture-changing findings, a human stop boundary, work that should
continue, and research that should remain frozen.

## Inputs

1. A sealed `context_cut` containing exact repository commits and selected
   review/research evidence.
2. The same bounded objective for at least Claude, Codex, and Gemini.
3. No access to earlier chat history outside the cut.

## Each actor produces

- claims about current state;
- risks and missing evidence;
- a recommended next path;
- explicit uncertainty;
- a proposed action with acceptance criteria;
- a `trajectory` atom naming the supplied and produced sets.

No model may adopt its own recommendation.

## Human selection

The human may select one path, synthesize several paths, reject all paths, or
request a new context cut. The selection becomes a `decision` atom. A material
action must bind that decision and later produce outcome evidence.

## Evaluation

A fresh fourth model receives the resulting graph projection and answers:

1. Why was release-surface allowed to continue?
2. Why was WRT-002 frozen?
3. Which findings changed architecture rather than tests?
4. Where did meta-recursion begin?
5. Which actor proposed each path?
6. Which context did each actor see?
7. What authority selected the final action?
8. What evidence would close it?

## Verdict

Pass requires 8/8 questions answered or correctly marked unknown, zero
proposal-as-decision errors, zero test-evidence-as-product-outcome errors, and
zero recontextualization-as-replay errors.

The human adjudicator and model evaluator independently label each answer. A
label disagreement makes the run **inconclusive**, not pass or fail, until a
separate adjudication record preserves both labels and states the resolution.
Trajectory independence is an adjudicated property: each trajectory must
declare its supplied set and any known coordination, but BOS does not claim to
inspect hidden model state.

## Fail and stop conditions

The run fails if it needs original chats, treats proposals as adopted, merges
unattributed recommendations, cannot identify context, confuses decision with
action, or cites an unproven score.

Stop and simplify if building the experiment requires a general-purpose
event-sourcing runtime. Run one end-to-end case before adding new kinds, UI,
autonomous daemons, or embedded executable rules.
