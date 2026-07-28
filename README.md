# BOS — Business Operating System

BOS is an experimental, typed decision graph for coordinating the s0fractal
ecosystem across repositories and model voices.

It is not another task tracker and not a replacement source of truth for the
repositories it observes. BOS records:

- assets and capabilities;
- claims, hypotheses, requirements, and risks;
- evidence and historical context cuts;
- decisions, actions, and outcomes;
- the different trajectories taken by human and model actors.

The long-term purpose is to let a model see not only the current state of the
ecosystem, but also how another actor understood a historical context, why it
proposed a path, what authority allowed an action, and what happened next.

## Start here

- [`spec/BOS-0001-core.bos.md`](spec/BOS-0001-core.bos.md) — draft core
  specification.
- [`schemas/bos-atom-v0.2.schema.json`](schemas/bos-atom-v0.2.schema.json) —
  strict machine envelope and payload types.
- [`atoms/`](atoms/) — first-class normative atoms consumed by BOS-0001.
- [`experiments/BOS-E0001-multimodel-decision-trace.md`](experiments/BOS-E0001-multimodel-decision-trace.md)
  — first dogfood experiment.
- [`raw/`](raw/) — research and captures. Raw material is evidence, not
  authority.
- [`archive/gemini-nodes-prototype/`](archive/gemini-nodes-prototype/) — the
  initial Gemini prototype; preserved as design archaeology, not active
  BOS-0001 data.

## Validate

```bash
uv run python tools/bos_validate.py
uv run python -m unittest -v tests.test_bos_validate
```

The validator covers mechanical V0/V1 syntax and active-graph integrity. It
does not claim semantic truth, global completeness, or governance adoption.

## Kernel sentence

> A model may propose meaning freely; changing shared reality requires explicit
> authority and leaves a verifiable receipt.
