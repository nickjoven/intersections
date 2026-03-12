# Stick-Slip Dynamics and the Dark Matter Dual: A Lagrangian Relaxation Interpretation of Low-Acceleration Gravity

**N. Joven** ([ORCID: 0009-0008-0679-0812](https://orcid.org/0009-0008-0679-0812))
March 2026
*Preprint — feedback welcome*

---

## Abstract

We propose a reframing of the dark matter problem through the lens of constrained optimization. The observed anomalous gravitational effects in the low-acceleration regime — galaxy rotation curves, the Tully-Fisher relation, the mass discrepancy-acceleration relation — exhibit threshold behavior structurally identical to stick-slip dynamics in mechanical systems. We show that this is not merely an analogy: the stick-slip transition is a specific instance of relaxation oscillation whose mathematical structure maps onto Lagrangian relaxation, an optimization technique in which hard constraints are replaced by penalty terms and iteratively tightened. We connect this to Chamseddine and Mukhanov's mimetic gravity (2013), in which a Lagrange multiplier enforcing a constraint on a scalar field produces cold-dark-matter-like behavior, and argue that the multiplier admits a dual interpretation as a shadow price — the cost the gravitational field pays to satisfy a constraint it cannot meet in the visible-matter variables alone. The dark matter "substance" is, in this framing, the dual variable of a constrained optimization problem. We provide a computational demonstration using Lagrangian relaxation on a parameterized gravitational potential, showing that threshold-dependent energy redistribution across scales emerges naturally from the optimization structure. The three-body problem alone reminds us that exact fidelity with observable matter dynamics is not available to us; the question is whether this framing narrows the search space more than particle-only models.

---

## 1. The Sonic Correction

The stick-slip phenomenon that produces sub-octave tones on a bowed string has been widely mischaracterized — including by one of the present authors — as requiring extreme bow pressure. Working string players (notably at NYU) have clarified the actual mechanism: the subharmonic emerges from **slow bow velocity with light contact pressure**, not from force.

This correction is not pedantic. It identifies which parameter governs the transition:

- **Incorrect model**: the threshold is a force threshold. Exceeding a critical pressure drives the system into non-linear response.
- **Correct model**: the threshold is a *velocity ratio*. Below a critical bow speed, kinetic friction cannot be maintained. The string alternates between static friction (stick — potential energy accumulates) and kinetic friction (slip — energy releases). The period of this cycle is twice the natural period, producing the octave-below subharmonic.

The operative parameters are:
1. **Relative velocity** (bow speed relative to string)
2. **Coupling strength** (rosin friction coefficient)
3. **Damping** (string/body energy absorption)
4. **Threshold**: the critical velocity below which static friction dominates

The subharmonic is not forced from above. It emerges from below — from conditions too slow, too quiet, too weakly driven to sustain continuous motion.

### 1.1 The Rotor Validation

The same mechanism causes documented mechanical failures in helicopter rotor systems (ground resonance, lead-lag chatter). The rotor blade's interaction with aerodynamic drag produces stick-slip oscillation when relative velocity enters the critical regime. The subharmonic mode grows because the structure lacks sufficient damping to absorb the energy redistribution. Engineers address this by:

1. Adding dampers (modifying the dissipation term)
2. Changing rotor speed (moving the velocity ratio away from the critical regime)

Neither fix involves changing force. Both modify the relationship between velocity and coupling. This confirms that the control surface is two-dimensional — (velocity ratio, damping coefficient) — not one-dimensional (force).

---

## 2. The Dark Matter Regime Is the Slow-Bow Regime

The empirical facts of the dark matter problem locate the anomaly precisely where the stick-slip model predicts:

**The anomalous effects appear in the low-acceleration regime.** Galaxy rotation curves deviate from Newtonian predictions not at the center (high acceleration, strong field) but at the outskirts (low acceleration, weak field). The mass discrepancy-acceleration relation (McGaugh et al., 2016) shows that the discrepancy between observed and predicted gravity is a function of acceleration alone, with a characteristic scale $a_0 \approx 1.2 \times 10^{-10}$ m/s².

**The anomaly does not appear in strong-field systems.** Solar system dynamics, binary pulsars, and strong gravitational lensing near massive objects are well-described by GR without modification. The "dark matter effect" vanishes where acceleration is high — exactly as a stick-slip subharmonic vanishes when bow velocity exceeds the critical threshold.

**The transition has a characteristic scale, not a sharp boundary.** Milgrom's MOND interpolating function $\mu(x)$, where $x = a/a_0$, transitions smoothly between Newtonian ($\mu \to 1$ for $x \gg 1$) and deep-MOND ($\mu \to x$ for $x \ll 1$) regimes. This smooth transition is characteristic of stick-slip: the Stribeck curve (friction vs. velocity in tribology) shows exactly this shape — a smooth, monotonic transition between static-friction-dominated and kinetic-friction-dominated regimes with a characteristic velocity scale.

The mapping:

| Stick-slip parameter | Gravitational analogue |
|---|---|
| Relative velocity | Local gravitational acceleration $a$ |
| Critical velocity | MOND acceleration scale $a_0$ |
| Static friction (stick) | Enhanced gravitational coupling (deep-MOND) |
| Kinetic friction (slip) | Standard Newtonian gravity |
| Subharmonic energy | "Dark matter" gravitational effect |
| Damping coefficient | Baryonic matter density / distribution |

The subharmonic — energy appearing at a scale the linear theory does not predict — is the dark matter halo.

---

## 3. From Stick-Slip to Lagrangian Relaxation

### 3.1 Stick-Slip as Relaxation Oscillation

The stick-slip cycle is a relaxation oscillation (van der Pol type):

1. **Slow phase (stick)**: the system accumulates potential energy under static friction. The state variable drifts slowly along a constraint surface.
2. **Fast phase (slip)**: the system exceeds the static friction threshold. Energy releases rapidly. The state variable jumps to a new branch.
3. **Reset**: the system re-enters the stick phase. The cycle repeats.

The mathematical structure is a slow-fast dynamical system with two timescales. The slow variable (accumulated elastic deformation) evolves on one timescale; the fast variable (slip velocity) evolves on another. The threshold mediates the transition between branches.

### 3.2 Lagrangian Relaxation Has the Same Structure

Lagrangian relaxation (Fisher, 1981; Held & Karp, 1971) solves constrained optimization problems by:

1. **Relaxing** a hard constraint into the objective function with a penalty multiplier $\lambda$
2. **Solving** the unconstrained (or easier) problem for fixed $\lambda$
3. **Updating** $\lambda$ via subgradient ascent: $\lambda^{k+1} = \lambda^k + \alpha_k (b - g(\mathbf{x}^k))$

where $b$ is the constraint bound and $g(\mathbf{x}^k)$ is the constraint function evaluated at the current solution.

The subgradient update is a slow accumulation: $\lambda$ drifts toward the optimal value, overshoots, corrects, overshoots less. The inner solve is a fast phase: given fixed $\lambda$, the system finds its optimum rapidly. The convergence trajectory oscillates around the saddle point with decreasing amplitude — exactly the stick-slip envelope.

Critical property: the step size $\alpha_k$ must be **small enough** to converge. Too large and the oscillation diverges. This is the "slow bow" condition — the system must be driven gently to produce the desired mode.

### 3.3 The Structural Identity

The correspondence is not analogical. It is structural:

| Stick-slip component | Lagrangian relaxation component |
|---|---|
| Accumulated elastic energy (stick) | Dual variable $\lambda$ (constraint violation accumulates) |
| Threshold (static → kinetic friction) | Complementary slackness condition ($\lambda \cdot (b - g(\mathbf{x})) = 0$) |
| Energy release (slip) | Primal update (inner solve snaps to new optimum) |
| Subharmonic mode | Dual oscillation around saddle point |
| Convergence to steady oscillation | Convergence to optimal $\lambda^*$ |
| Divergence (rotor failure) | Step size too large (dual diverges) |

Both are instances of the same mathematical object: iterative saddle-point seeking in a non-smooth optimization landscape, where the primal and dual variables evolve on different timescales.

---

## 4. Dark Matter as a Dual Variable

### 4.1 The Mimetic Gravity Precedent

Chamseddine and Mukhanov (2013) demonstrated that adding a constraint to the gravitational action via a Lagrange multiplier produces cold-dark-matter-like behavior. Specifically, imposing

$$g^{\mu\nu} \partial_\mu \phi \partial_\nu \phi = 1$$

on a scalar field $\phi$ via a multiplier $\lambda$ modifies the Einstein equations such that the multiplier contributes a dust-like energy-momentum tensor. The "dark matter" is not a new particle — it is the dynamical consequence of enforcing a constraint on the metric.

This result has been developed extensively (Sebastiani et al., 2017), extended to F(R) gravity where the Lagrange multiplier mechanism produces inflation, dark energy, and bounce cosmologies (Nojiri & Odintsov, 2014), and the related approach applied to dark energy (Capozziello, Matsumoto, Nojiri & Odintsov, 2010), but always within the field-theoretic framing: the multiplier is a mathematical device that enforces a symmetry or constraint, and the resulting phenomenology happens to resemble dark matter.

### 4.2 The Optimization-Theoretic Reframing

We propose reading mimetic gravity through the lens of Lagrangian relaxation:

**The Lagrange multiplier is a shadow price.** In optimization theory, the dual variable $\lambda^*$ at the optimum has a precise economic interpretation: it is the marginal value of relaxing the constraint by one unit. If the constraint $g(\mathbf{x}) \leq b$ is active, then $\lambda^*$ tells you how much the objective would improve if $b$ were increased by $\epsilon$.

Applied to mimetic gravity: **the dark matter field is the cost the gravitational field pays to satisfy a constraint it cannot meet using visible matter alone.** The constraint (normalization of the scalar field gradient) is a geometric requirement. The multiplier (dark matter) is what it costs to enforce that geometry given the available baryonic matter distribution.

**The constraint is geometric; the price is dynamical.** The dark matter halo profile is not an arbitrary density distribution — it is shaped by the optimization landscape. Specifically, it should reflect the structure of the dual problem: where the constraint is most binding (galaxy outskirts, low acceleration), the dual variable (dark matter density) is largest.

This is exactly what is observed. The mass discrepancy-acceleration relation shows that the "dark matter fraction" increases monotonically as acceleration decreases. The constraint is most expensive to enforce precisely where the baryonic matter provides the least gravitational acceleration.

### 4.3 Why the Low-Acceleration Regime

In Lagrangian relaxation, the dual variable is nonzero only when the constraint is active (complementary slackness). In the high-acceleration regime, the gravitational field satisfies the geometric constraint using baryonic matter alone — the constraint is slack, and the dual variable (dark matter) is zero. In the low-acceleration regime, the baryonic matter is insufficient to satisfy the constraint — it becomes active, and the dual variable takes a nonzero value proportional to the violation.

This is the stick-slip transition:
- **High acceleration (fast bow)**: kinetic friction sustained, no stick phase, no subharmonic. Gravity is Newtonian, no dark matter needed.
- **Low acceleration (slow bow)**: kinetic friction cannot be maintained, system enters stick-slip, subharmonic appears. The geometric constraint binds, the dual variable activates, "dark matter" emerges.

The MOND acceleration scale $a_0$ is the critical velocity of the stick-slip transition — the point at which the gravitational field can no longer satisfy its geometric constraint using baryonic matter alone and must pay a dual-variable cost.

---

## 5. Predictions and Distinguishing Tests

If dark matter effects are dual variables of a constrained optimization, several predictions follow that differ from particle dark matter models:

### 5.1 Mode Structure

Lagrangian relaxation converges through oscillation around the saddle point. If the dark matter halo is the spatial signature of this convergence, its radial profile should reflect the oscillation envelope — not a smooth NFW profile (Navarro, Frenk & White, 1997), but one with residual oscillatory structure at a characteristic scale set by the "step size" of the dual update.

Intriguingly, observations of galaxy rotation curves do show fine structure beyond smooth fits. Whether this structure is consistent with dual-variable oscillation (as opposed to baryonic substructure, observational noise, or other effects) is an empirical question.

### 5.2 Convergence Failures

Lagrangian relaxation can fail to converge if:
- The step size is too large (oscillation diverges)
- The constraint set is empty (no feasible solution exists)
- The objective is not concave in the relevant variables

Galaxy clusters are the regime where MOND notoriously underperforms — it predicts less dark matter than observed. In the Lagrangian relaxation framing, this could indicate a convergence failure: the optimization problem in galaxy clusters has different structure (multiple interacting constraints, loss of concavity) that prevents the single-constraint relaxation from finding the correct dual value. This would predict that galaxy cluster dark matter requires a multi-constraint formulation — consistent with the observation that cluster dynamics involve additional physics (hot gas, ram pressure, merger history) absent in isolated galaxies.

### 5.3 No Direct Detection

If dark matter is a dual variable rather than a primal variable (a substance), direct detection experiments should find nothing. The dual variable has physical effects (it modifies the gravitational field) but is not a particle that carries energy-momentum independently of the constraint it enforces. This is consistent with the null results from XENON, LUX, PandaX, and other direct detection experiments through 2026.

### 5.4 The Bullet Cluster

The Bullet Cluster (1E 0657-56) is often cited as evidence for particle dark matter, since the gravitational lensing signal is offset from the visible baryonic matter (hot gas). In the dual-variable framing, this requires that the constraint (and therefore its multiplier) can decouple from the baryonic distribution during violent non-equilibrium events (cluster mergers). This is plausible if the constraint is geometric (tied to the metric) rather than material (tied to the matter distribution) — the metric need not track the gas during a rapid merger. However, this prediction needs quantitative development to be compelling.

---

## 6. The Three-Body Caveat

We note, with appropriate humility, that the classical three-body problem already demonstrates the limits of our dynamical fidelity with observable matter. If three gravitationally interacting bodies cannot be solved in closed form, the claim that dark matter anomalies in systems of $10^{11}$ bodies must require new matter (rather than new mathematics) deserves scrutiny. The n-body problem is not merely hard — it is formally chaotic, with exponential sensitivity to initial conditions. The gap between "Newtonian prediction" and "observed dynamics" in galactic systems includes an unknown contribution from computational intractability, not just missing mass.

This does not prove that dark matter is mathematical rather than material. But it shifts the burden of proof: before asserting that a discrepancy requires new matter, one must establish that the discrepancy exceeds what computational intractability alone could produce. The Lagrangian relaxation framing suggests a specific mathematical structure for that excess. Whether the structure fits is an empirical question.

---

## 7. Computational Demonstration

We provide a companion Jupyter notebook (`stick_slip_lagrangian.ipynb`) that demonstrates the core mechanism using the Lagrangian relaxation framework from Joven (2026). The notebook:

1. **Implements a stick-slip oscillator** with parameterized velocity, coupling, damping, and threshold — showing subharmonic generation in the slow-velocity regime
2. **Maps the oscillator onto a constrained gravitational potential**, where the "budget constraint" is the baryonic mass and the "gain function" is the gravitational binding energy
3. **Solves the Lagrangian relaxation**, showing the dual variable (dark matter analogue) as a function of the constraint tightness (baryonic mass available)
4. **Demonstrates the MOND-like transition**: the dual variable is zero when the constraint is slack (high acceleration / sufficient baryonic mass) and grows when the constraint binds (low acceleration / insufficient baryonic mass)
5. **Shows convergence and divergence regimes**, corresponding to stable galaxy rotation curves and unstable cluster dynamics

The notebook uses only Python standard library, following the convention established in Joven (2026).

---

## 8. Relation to Existing Work

This proposal draws on and extends several existing research programs:

**MOND (Milgrom, 1983)**: provides the empirical acceleration threshold $a_0$ and the interpolating function $\mu(x)$ that we identify with the Stribeck curve of the stick-slip transition. Our contribution is a mechanism (constrained optimization) rather than a phenomenological fit.

**Mimetic gravity (Chamseddine & Mukhanov, 2013)**: provides the Lagrange multiplier formalism that produces dark-matter-like behavior from a geometric constraint. Our contribution is the optimization-theoretic interpretation of the multiplier as a shadow price, connecting mimetic gravity to MOND via duality theory.

**Superfluid dark matter (Berezhiani & Khoury, 2015)**: provides the phase transition (superfluid → normal fluid) with a critical velocity that maps onto the stick-slip threshold. Our contribution is identifying the Lagrangian relaxation structure as the common mathematical framework underlying both the phase transition and the MOND phenomenology.

**Emergent gravity (Verlinde, 2016)**: derives dark-matter-like effects from entropy extremization. Our approach is complementary: Verlinde extremizes entropy; we relax a geometric constraint. Both produce apparent dark matter from optimization, but over different objectives.

**The three-body problem and computational irreducibility (Wolfram, 2002; Sussman & Wisdom, 1992)**: establishes that the gap between theory and observation in gravitational n-body systems includes an irreducible computational component. Our contribution is proposing a specific mathematical structure (Lagrangian relaxation) for the "excess" beyond this gap.

### 8.1 What Is New

To our knowledge, the following specific connections have not appeared in the literature:

1. The identification of the MOND interpolating function with the Stribeck friction curve
2. The interpretation of mimetic gravity's Lagrange multiplier as an optimization-theoretic shadow price
3. The application of Lagrangian relaxation (the optimization technique) to gravitational field dynamics
4. The use of stick-slip relaxation oscillation as a dynamical model for the MOND transition
5. The prediction that galaxy cluster MOND failures correspond to Lagrangian relaxation convergence failures

---

## 9. Conclusion

The cost of this hypothesis is low. It requires no new particles, no new forces, and no modifications to general relativity at the level of the action. It requires only that we read an existing mathematical structure (mimetic gravity's Lagrange multiplier) through an existing mathematical framework (Lagrangian relaxation) motivated by an existing physical phenomenon (stick-slip dynamics in the slow-velocity regime).

If the framing is correct, it narrows the search space: the dark matter problem becomes a question about which geometric constraint the gravitational field is optimizing against, and the acceleration scale $a_0$ is the critical coupling at which the constraint becomes active. If the framing is wrong, it has consumed one short paper and a notebook. The asymmetry favors exploration.

The thread began with a bowed string producing a tone one octave below its fundamental — not through force, but through patience. The gravitational field may be doing the same thing.

---

## References

- Bekenstein, J. D. (2004). Relativistic gravitation theory for the modified Newtonian dynamics paradigm. *Phys. Rev. D*, 70(8), 083509.
- Berezhiani, L., & Khoury, J. (2015). Theory of dark matter superfluidity. *Phys. Rev. D*, 92(10), 103510.
- Capozziello, S., Matsumoto, J., Nojiri, S., & Odintsov, S. D. (2010). Dark energy from modified gravity with Lagrange multipliers. arXiv:1004.3691v2.
- Chamseddine, A. H., & Mukhanov, V. (2013). Mimetic dark matter. *JHEP*, 2013(11), 135.
- Fisher, M. L. (1981). The Lagrangian relaxation method for solving integer programming problems. *Management Science*, 27(1), 1-18.
- Held, M., & Karp, R. M. (1971). The traveling-salesman problem and minimum spanning trees: Part II. *Math. Programming*, 1(1), 6-25.
- Huang, J., et al. (2024). Large language models cannot self-correct reasoning yet. *ICLR 2024*.
- Joven, N. (2026). A content-addressed adaptive knowledge substrate for distributed epistemic coordination. *Preprint*.
- McGaugh, S. S., Lelli, F., & Schombert, J. M. (2016). Radial acceleration relation in rotationally supported galaxies. *Phys. Rev. Lett.*, 117(20), 201101.
- Milgrom, M. (1983). A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis. *ApJ*, 270, 365-370.
- Nojiri, S., & Odintsov, S. D. (2014). Mimetic F(R) gravity: inflation, dark energy and bounce. *Mod. Phys. Lett. A*, 29(40), 1450211. arXiv:1408.3561.
- Navarro, J. F., Frenk, C. S., & White, S. D. M. (1997). A universal density profile from hierarchical clustering. *ApJ*, 490(2), 493-508.
- Sebastiani, L., Vagnozzi, S., & Myrzakulov, R. (2017). Mimetic gravity: a review of recent developments and applications to cosmology and astrophysics. *Advances in High Energy Physics*, 2017.
- Sussman, G. J., & Wisdom, J. (1992). Chaotic evolution of the solar system. *Science*, 257(5066), 56-62.
- Verlinde, E. (2016). Emergent gravity and the dark universe. *SciPost Phys.*, 2(3), 016.
- Wolfram, S. (2002). *A New Kind of Science*. Wolfram Media.

---

*Companion notebook: `stick_slip_lagrangian.ipynb`*
*This paper is released under CC0.*
