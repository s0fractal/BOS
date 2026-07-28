# BOS — Business Operating System

BOS is an experimental, typed decision graph for coordinating the s0fractal
ecosystem across repositories and model voices.

Status: **research / genesis candidate / not adopted**.

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
- [`schemas/bos-atom-v0.3.schema.json`](schemas/bos-atom-v0.3.schema.json) —
  current strict machine envelope and payload types; v0.2 remains unchanged
  for revision-2 records.
- [`atoms/`](atoms/) — first-class normative atoms consumed by BOS-0001.
- [`bos:vehicle:bos-e0001`](atoms/vehicle/bos-e0001-multimodel-decision-trace.bos.md)
  — first dogfood experiment.
- [`raw/`](raw/) — research and captures. Raw material is evidence, not
  authority.

## Validate

```bash
uv run python tools/bos_validate.py
uv run python -m unittest -v tests.test_bos_validate
```

The validator covers the implemented mechanical subset of V0/V1/V3 and binds
its JSON report to the exact active-file universe. It does not claim semantic
truth, global completeness, a clean historical cut, or governance adoption.

## Kernel sentence

> A model may propose meaning freely; changing shared reality requires explicit
> authority and leaves a verifiable receipt.
