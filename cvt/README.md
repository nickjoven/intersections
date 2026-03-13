# cvt — Consistency Vector Theory

One constraining vector. Dimensionally different systems. Emergent thermodynamics.

## What this repository is

This is not a paper about consistency vector theory. It is a running of the
theory. Each demonstration uses the `ket` binary directly. The CIDs produced
are the audit trail. The git log is the lineage. The repository is itself a
non-injective system that converges — it demonstrates by being.

Separate from [`jfk-dsa`](https://github.com/nickjoven/jfk-dsa) (which holds
formal hypotheses) and [`ket`](https://github.com/nickjoven/ket) (which is the
substrate). This repo is the bridge: ket operations as mechanical proof.

## What it proves

1. **CAS convergence** — Two independent reasoning chains about the same fact
   produce the same CID when their content converges. The store has no record
   of which path was taken. (`demos/01_cas_convergence.sh`)

2. **Genealogical gauge choice** — Two lineages lead to the same terminal node.
   Lineage is gauge, not ground truth. (`demos/02_gauge_choice.sh`)

3. **Equilibrium and pruning** — Saturated nodes are pruned by the optimizer
   without consulting lineage. This is what equilibrium looks like operationally.
   (`demos/03_equilibrium.sh`)

4. **Boundary entropy as gauge-invariant time** — Nodes with more independent
   lineages persist longer under MM decay. The temporal measure is a function of
   the boundary. (`demos/04_temporal_boundary.sh`)

5. **Cross-domain convergence** — Physics claims converge to the same epistemic
   equilibrium as substrate claims. The constraining vector is structural, not
   domain-specific. (`demos/05_cross_domain.sh`)

## Structure

```
cvt/
├── README.md
├── .ket/                   # Live ket substrate (committed)
├── laws/
│   └── noninjectivity.md   # Formal statement of the law
├── demos/
│   01_cas_convergence.sh
│   02_gauge_choice.sh
│   03_equilibrium.sh
│   04_temporal_boundary.sh
│   05_cross_domain.sh
├── audit/
│   └── cids.log            # Append-only log of every CID produced
└── synthesis.md            # What resolves, what remains open
```

## Audit protocol

Every demo appends to `audit/cids.log`:

```
timestamp | demo | label | cid
```

The log is append-only. Running the demos twice produces different CIDs for
content that includes timestamps, identical CIDs for pure content. The
difference is itself informative — it tells you which claims are time-indexed
and which are not.

The repo is auditable if and only if: given only `audit/cids.log` and the ket
binary, every claim can be verified by `ket get <cid>` without running the
demos again.

## Prerequisites

- [`ket`](https://github.com/nickjoven/ket) binary in PATH
- `jq` for JSON parsing in demo scripts
- bash 4+

## Related

- [intersections](https://github.com/nickjoven/intersections) — stick-slip dynamics and the dark matter dual
- [jfk-dsa](https://github.com/nickjoven/jfk-dsa) — formal hypotheses
- [ket](https://github.com/nickjoven/ket) — content-addressed substrate
