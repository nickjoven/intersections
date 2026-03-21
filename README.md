# intersections

**Purpose:** Companion repository to [201](https://github.com/nickjoven/201) exploring the local physical mechanism (stick-slip friction) that produces the synchronization-gravity correspondence, the optimization-theoretic interpretation of dark matter as a Lagrange multiplier, and the Consistency Vector Theory (CVT) epistemological framework.

---

## Paper

[Stick-Slip Dynamics and the Dark Matter Dual: A Lagrangian Relaxation Interpretation of Low-Acceleration Gravity](joven_stick_slip_dark_matter.md)
N. Joven ([ORCID](https://orcid.org/0009-0008-0679-0812)), March 2026 — CC0

## Interactive Visualization

[Live demo](https://nickjoven.github.io/intersections/) — six-panel interactive explorer (Plotly.js + Canvas, zero build step):

1. String + galaxy stick-slip animation
2. Velocity x pressure phase diagram (1,200 precomputed sims)
3. Stribeck / MOND / complementary slackness curves
4. Convergence vs divergence
5. Rotation curve decomposition
6. Mass discrepancy-acceleration relation

## Companion Notebook

[stick_slip_lagrangian.ipynb](stick_slip_lagrangian.ipynb) — stdlib-only Python. Stick-slip oscillator, galaxy rotation model, Lagrangian relaxation gravity solver, convergence demonstration.

## Key Claims

1. The MOND interpolating function is a Stribeck friction curve
2. Mimetic gravity's Lagrange multiplier is an optimization-theoretic shadow price
3. The stick-slip critical band is bidirectional — entered by slow drive (galaxies) or overwhelming force (inner accretion disks)
4. QPO frequency ratios should derive from the disk's Stribeck transfer function, varying with black hole spin
5. The DAMA/LIBRA annual modulation is a drive oscillation through a medium-dependent threshold, predicting site-dependent (not site-independent) replication
6. Galaxy cluster MOND failures correspond to Lagrangian relaxation convergence failures

## Structure

```
intersections/
├── joven_stick_slip_dark_matter.md    ← Companion paper
├── stick_slip_lagrangian.ipynb        ← Lagrangian relaxation gravity solver
├── cone_topology.ipynb                ← Flat rotation curves from conical geometry
├── stick_slip_galaxy.ipynb            ← Stick-slip dynamics applied to galaxies
├── 08_square_wave_bifurcation.ipynb   ← Square-wave bifurcation analysis
├── 09_cylinder_stick_slip.ipynb       ← Cylindrical stick-slip mode coupling
├── dispersion_rolling.ipynb           ← Dispersion and rolling analysis
├── cvt/                               ← Consistency Vector Theory
│   ├── synthesis.md                       CVT synthesis document
│   ├── laws/noninjectivity.md             Law of Genealogical Non-Injectivity
│   └── notebooks/                         7 computational notebooks
├── index.html                         ← Interactive landing page (GitHub Pages)
└── README.md
```

## Related

- [201](https://github.com/nickjoven/201) — parent framework (Kuramoto synchronization, sparc_x API, SPARC galaxies)
- [proslambenomenos](https://github.com/nickjoven/proslambenomenos) — proslambenomenos frequency, Lyapunov uniqueness, Renzo's Rule from Kuramoto
- [stribeck-optics](https://github.com/nickjoven/stribeck-optics) — atmospheric scattering as a stick-slip transfer function (stub)

## License

[CC0 1.0 Universal](LICENSE) — No rights reserved.
