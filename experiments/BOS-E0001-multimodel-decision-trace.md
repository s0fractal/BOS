# BOS-E0001 — Multi-model decision trace

Status: proposed
Depends on: BOS-0001 Phase 0

## Question

Can a fresh model reconstruct one real ecosystem decision from typed atoms and
trajectories without reading the full chats or every repository?

## Case

Use the real decision boundary around:

- `warrant` release-surface gate;
- its adoption-surface dependency;
- the consciously frozen WRT-002 work;
- the point where continued adversarial review became meta-verification.

This case is useful because it contains:

- multiple independent model actors;
- repeated countervectors;
- architectural changes;
- a human stop boundary;
- a feature that should continue;
- a research branch that should remain frozen.

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
- a `trajectory` atom naming the read and produced sets.

No model may adopt its own recommendation.

## Human selection

The human may:

- select one path;
- synthesize several paths;
- reject all paths;
- request a new context cut.

The selection becomes a `decision` atom. If it authorizes a material action,
the action must bind the decision and later produce outcome evidence.

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

## Pass condition

Pass if the fourth model answers all eight questions using only resolvable BOS
atoms and can distinguish:

- observed fact from strategic claim;
- model recommendation from adopted decision;
- green test evidence from product outcome;
- historical recontextualization from deterministic replay.

## Fail conditions

- It needs the original chats.
- It treats all `active` objects as adopted and healthy.
- It merges model disagreement into one unattributed recommendation.
- It cannot identify the context cut.
- It cannot distinguish a decision from an action.
- It cites a score or conclusion with no provenance.
- Building the experiment requires a general-purpose event-sourcing runtime.

## Stop condition

Run one end-to-end case before adding new atom kinds, UI, autonomous daemons, or
embedded executable rules.
