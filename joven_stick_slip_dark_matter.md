# Stick-Slip Dynamics and the Dark Matter Dual: A Lagrangian Relaxation Interpretation of Low-Acceleration Gravity

**N. Joven** ([ORCID: 0009-0008-0679-0812](https://orcid.org/0009-0008-0679-0812))
March 2026
*Preprint — CC0 1.0*

---

## Abstract

A bowed string can produce a tone below its fundamental frequency through stick-slip dynamics — and it can do so via two independent paths: slow the bow, or press harder. We show that this bidirectional threshold mechanism maps structurally onto the dark matter problem, where the Lagrange multiplier enforcing a geometric constraint in mimetic gravity (Chamseddine & Mukhanov, 2013) admits interpretation as a shadow price in the sense of Lagrangian relaxation. The dark matter halo is the cost the gravitational field pays to satisfy a constraint it cannot meet with visible matter alone. Because the shadow price is local — determined at each radius by the local constraint violation — the framework produces Renzo's Rule (Sancisi, 2004) as a theorem of complementary slackness rather than a correlation requiring explanation. The acceleration scale $a_0 \approx 1.2 \times 10^{-10}$ m/s² is the galactic instance of a medium-dependent threshold; other media (accretion disks, fault zones, Josephson junctions) have their own critical scales, and the same mechanism predicts subharmonic signatures — including QPO frequency ratios — across all of them.

---

## 1. The Mechanism: Two Paths to a Subharmonic

A bowed string can produce a tone one octave below its fundamental frequency. The mechanism is stick-slip: the string alternates between static friction (stick — potential energy accumulates) and kinetic friction (slip — energy releases as the string snaps back). The period of this cycle is twice the natural period, producing the subharmonic.

### 1.1 The Experimental Fact

Kawano et al. (2025) resolved the mechanism experimentally using high-speed imaging and finite element simulation. They mapped the full velocity–pressure parameter space and identified **two independent paths** to subharmonic generation:

1. **Slow bow velocity.** When $v_\text{bow}$ drops below a critical value, kinetic friction cannot be sustained — the string catches before the bow has moved enough to maintain the slip phase. This is the understimulated regime: insufficient drive to sustain smooth sliding.

2. **Increased bow pressure.** When $d_\text{bow}$ exceeds a critical value at moderate velocity, amplified frictional force suppresses the standard Helmholtz vibration mode and allows the subharmonic mode to dominate. This is the overstimulated regime: excessive coupling that the medium cannot dissipate smoothly.

These are not two sides of one ratio. They are two independent causal paths that converge on the same output: stick-slip oscillation at half the fundamental frequency. Both produce the same observable — a tone one octave below the fundamental with the characteristic spectral signature of period doubling. The subharmonic onset region in the phase diagram is a band accessible from either axis.

### 1.2 The Control Surface

The control surface is two-dimensional: a velocity axis and a pressure axis, each with its own independent threshold.

| Parameter | Role | Critical crossing |
|---|---|---|
| Relative velocity | Drive (bow speed relative to string) | Too slow → kinetic friction fails → stick phase from below |
| Bow pressure | Coupling strength (normal force × friction coefficient) | Too high → static friction overwhelms restoring force → stick phase from above |
| Damping | Dissipation (energy absorption by string and body) | Mediates which crossing is accessible |

Whether a particular physical system enters the stick-slip regime via the velocity path or the pressure path depends on which threshold it can reach with its available driving parameters. The direction of entry varies. The mechanism does not.

### 1.3 Validation: Rotor Systems

The same mechanism causes documented mechanical failures in helicopter rotor systems (ground resonance, lead-lag chatter). Engineers address it by adding dampers (modifying dissipation) or changing rotor speed (moving the velocity ratio out of the critical band). Both fixes move the drive/threshold ratio out of the critical band without adding or removing force. The control surface is two-dimensional — (drive/threshold ratio, damping coefficient) — with the critical band accessible from either axis.

---

## 2. The Galactic Instance and Its Generalization

### 2.1 The Acceleration Threshold

Galaxy rotation curves deviate from Newtonian predictions at the outskirts (low acceleration), not at the center (high acceleration). The mass discrepancy–acceleration relation (McGaugh, Lelli & Schombert, 2016) shows that the discrepancy is a function of acceleration alone, with characteristic scale $a_0 \approx 1.2 \times 10^{-10}$ m/s².

Milgrom's MOND interpolating function $\mu(x)$, where $x = a/a_0$, transitions between Newtonian ($\mu \to 1$ for $x \gg 1$) and deep-MOND ($\mu \to x$ for $x \ll 1$). The quantity $(1 - \mu)$ measures excess coupling — high below the threshold, declining to zero above it. This is structurally parallel to the velocity-weakening branch of the Stribeck friction curve.

The galactic case enters the stick-slip band from the velocity side: cosmic expansion is slow, galactic accelerations are small, and the gravitational field enters the critical regime through patience — the slow-drive path of §1.1.

### 2.2 The Two Branches in Astrophysics

The two-path structure of §1 persists at astrophysical scales. The Stribeck curve has both a velocity-weakening branch (friction rises as drive slows) and a velocity-strengthening branch (friction rises as drive intensifies):

- **Velocity-weakening (slow drive):** the galactic dark matter case. Acceleration drops below $a_0$; the gravitational field enters the stick-slip band from below. The subharmonic artifact is the dark matter halo.

- **Velocity-strengthening (excessive drive):** the accretion disk case. Tidal shear and magnetic coupling exceed the medium's dissipative capacity; the system enters the stick-slip band from above. The subharmonic artifacts are quasi-periodic oscillations (QPOs).

An accretion disk may be the only astrophysical system that exhibits both modes simultaneously: slow-drive subharmonics in the outer disk (where the dark matter problem lives) and force-driven subharmonics in the inner disk (where QPOs are observed). If both arise from the same transfer function, the framework is not an analogy — it is the dynamics.

### 2.3 Medium-Dependent Thresholds

The stick-slip framework does not require the threshold to be a universal constant. It requires a threshold to exist in the medium's transfer function. The critical band can be entered from either direction:

| System | Medium | Drive parameter | Threshold | Subharmonic artifact |
|---|---|---|---|---|
| Galaxy | Spacetime geometry | Gravitational acceleration | $a_0$ | Dark matter halo |
| Accretion disk | Ionized plasma + magnetic fields | Orbital shear rate | MRI critical wavelength | Quasi-periodic oscillations |
| Bowed string | Rosin friction layer | Bow velocity | $v_\text{threshold}$ | Subharmonic tone |
| Fault zone | Crustal rock / fault gouge | Tectonic strain rate | Rate-and-state friction | Earthquake recurrence |
| Josephson junction | SIS barrier | AC bias current | Critical current $I_c$ | Shapiro steps ($nhf/2e$) |
| AV node | Cardiac tissue | SA node firing rate | Refractory period$^{-1}$ | 2:1, 3:1 heart block |
| Atmosphere | Scattering particulates | Source spatial frequency | Mean free path × coherence | Optical halo |

The term "stick-slip" was coined by Brace and Byerlee (1966) for seismic fault experiments; the seismic case is the original domain, the galactic case a cross-domain instance. In every system, the subharmonic appears when the drive/threshold ratio enters a critical band. The framework is structural, not numerical — $a_0$ is the galactic instance, not a universal constant.

---

## 3. From Stick-Slip to Lagrangian Relaxation

### 3.1 Stick-Slip as Relaxation Oscillation

The stick-slip cycle is a relaxation oscillation (van der Pol type):

1. **Slow phase (stick)**: the system accumulates potential energy under static friction. The state variable drifts slowly along a constraint surface.
2. **Fast phase (slip)**: the system exceeds the static friction threshold. Energy releases rapidly. The state variable jumps to a new branch.
3. **Reset**: the system re-enters the stick phase. The cycle repeats.

The mathematical structure is a slow-fast dynamical system with two timescales: a slow variable (accumulated elastic deformation) and a fast variable (slip velocity), with the threshold mediating transitions.

### 3.2 Lagrangian Relaxation Has the Same Structure

Lagrangian relaxation (Fisher, 1981; Held & Karp, 1971) solves constrained optimization problems by:

1. **Relaxing** a hard constraint into the objective function with a penalty multiplier $\lambda$
2. **Solving** the unconstrained problem for fixed $\lambda$
3. **Updating** $\lambda$ via subgradient ascent: $\lambda^{k+1} = \lambda^k + \alpha_k (b - g(\mathbf{x}^k))$

The subgradient update is a slow accumulation: $\lambda$ drifts toward the optimal value, overshoots, corrects, overshoots less. The inner solve is a fast phase: given fixed $\lambda$, the system finds its optimum rapidly. The convergence trajectory oscillates around the saddle point — the stick-slip envelope.

The step size $\alpha_k$ must be small enough to converge. Too large and the oscillation diverges. This is the slow-bow condition: the system must be driven gently to produce the desired mode.

### 3.3 The Structural Correspondence

Both systems are instances of iterative saddle-point seeking with two timescales. The correspondence operates at the level of dynamical classification — both are relaxation oscillations — rather than a proven isomorphism between state spaces. What we claim is shared structure:

| Stick-slip component | Lagrangian relaxation component |
|---|---|
| Accumulated elastic energy (stick) | Dual variable $\lambda$ (constraint violation accumulates) |
| Threshold (static → kinetic friction) | Complementary slackness ($\lambda \cdot (b - g(\mathbf{x})) = 0$) |
| Energy release (slip) | Primal update (inner solve snaps to new optimum) |
| Subharmonic mode | Dual oscillation around saddle point |
| Convergence to steady oscillation | Convergence to optimal $\lambda^*$ |
| Divergence (rotor failure) | Step size too large (dual diverges) |

---

## 4. Dark Matter as a Dual Variable

### 4.1 The Mimetic Gravity Precedent

Chamseddine and Mukhanov (2013) demonstrated that imposing

$$g^{\mu\nu} \partial_\mu \phi \partial_\nu \phi = 1$$

on a scalar field $\phi$ via a Lagrange multiplier $\lambda$ produces cold-dark-matter-like behavior: the multiplier contributes a dust-like energy-momentum tensor. The "dark matter" is not a new particle — it is the dynamical consequence of enforcing a geometric constraint on the metric.

This result has been extended to F(R) gravity (Nojiri & Odintsov, 2014), explored extensively in cosmological applications (Sebastiani et al., 2017), and connected to dark energy through related Lagrange multiplier approaches (Capozziello et al., 2010).

**Known stability concerns.** The minimal formulation carries documented pathologies: ghost instability, caustic formation from pressureless dust dynamics, and superluminal propagation of lower helicity modes (Chaichian et al., 2014; Sebastiani et al., 2017). Higher-derivative extensions (Chamseddine & Mukhanov, 2014) resolve these. The interpretation developed here operates in such an extended framework.

### 4.2 The Shadow Price Interpretation

We propose reading mimetic gravity through the lens of Lagrangian relaxation.

**The constraint is explicit.** It is the gradient normalization condition: the gravitational field must find a metric $g_{\mu\nu}$ satisfying both the Einstein equations and the unit-norm requirement, given the observed baryonic source. The dual variable $\lambda$ enforces the normalization; the dark matter contribution is its dynamical shadow.

**The Lagrange multiplier is a shadow price.** In optimization theory, the dual variable $\lambda^*$ at the optimum is the marginal value of relaxing the constraint by one unit. Applied to mimetic gravity: the dark matter field is the cost the gravitational field pays to satisfy the gradient normalization constraint it cannot meet using visible matter alone.

**A caveat on scope.** Shadow prices are rigorously defined in finite-dimensional constrained optimization under convexity and constraint qualification. The field-theoretic extension to infinite dimensions exists (Ekeland & Temam, 1976) but requires additional regularity. We use "shadow price" as an interpretive lens that generates testable predictions; the rigorous infinite-dimensional duality theory for this specific action remains to be established.

**The constraint is geometric; the price is dynamical.** The topology of spacetime is unchanged. No new fields are added to the metric, no extra dimensions compactified, no topological defects introduced. What changes is the cost function: the gravitational field pays a price to maintain geometric consistency where baryonic matter alone is insufficient. The dark matter halo is shaped by the optimization landscape — where the constraint is most binding (galaxy outskirts, low acceleration), the dual variable is largest. This is exactly what is observed: the mass discrepancy–acceleration relation shows that the dark matter fraction increases monotonically as acceleration decreases.

### 4.3 Renzo's Rule as a Theorem

Renzo's Rule (Sancisi, 2004) is the empirical observation that every feature in a galaxy's baryonic luminosity profile has a corresponding feature in its rotation curve. A bump in surface brightness produces a bump in rotational velocity; a dip produces a dip. The correspondence is detailed, galaxy-by-galaxy, radius-by-radius.

This is difficult for particle dark matter. An NFW halo (Navarro, Frenk & White, 1997) is smooth — it has no mechanism to develop fine structure tracking baryonic features. The halo formed first; the baryons fell in later. Reproducing Renzo's Rule requires elaborate feedback models tuned galaxy by galaxy.

In the Lagrangian relaxation framing, Renzo's Rule is a theorem conditional on the optimization structure.

The dual variable at each radius satisfies complementary slackness: $\lambda(r) = 0$ where the constraint is slack ($a_\text{bary}(r) \geq a_\text{obs}(r)$), and $\lambda(r) > 0$ where the constraint binds. In the simplest formulation:

$$\lambda(r) = \max\left(0,\; a_\text{obs}(r) - a_\text{bary}(r)\right)$$

Therefore:

1. If baryonic density increases at radius $r$, the deficit shrinks, $\lambda(r)$ decreases.
2. If baryonic density decreases at radius $r$, the deficit grows, $\lambda(r)$ increases.
3. The total acceleration $a_\text{total}(r) = a_\text{bary}(r) + \lambda(r)$ tracks $a_\text{obs}(r)$ at every radius where the constraint is active.

There are no free parameters. The local coupling is a structural consequence of the optimization — the dual variable *must* track the baryonic distribution because it is defined by the local constraint violation against that distribution.

MOND also reproduces Renzo's Rule, but as an input — the theory is constructed to be baryonically sourced. Here, the local coupling is an output: it follows from complementary slackness applied to a geometric constraint.

### 4.4 When the Constraint Binds

Complementary slackness is symmetric in the drive/threshold ratio:

- **Mid-range acceleration (fast bow):** kinetic friction sustained, no stick phase. Gravity is Newtonian, $\lambda = 0$.
- **Low acceleration (slow bow):** the system enters the stick-slip band from below. The constraint binds, the dual variable activates. This is the galactic dark matter regime.
- **Extreme drive (pressed firmly):** the system enters the stick-slip band from above. The constraint binds via the pressure path. This is the accretion disk QPO regime.

The two entry modes produce dual variables in different media at different scales, but the mechanism — constraint binding, dual activation, subharmonic generation — is one.

---

## 5. Predictions and Distinguishing Tests

### 5.1 Renzo's Rule — Quantitative Predictions

1. **Feature amplitude ratio.** Where the constraint is active ($\lambda > 0$), a local perturbation $\delta a_\text{bary}$ produces $\delta\lambda = -\delta a_\text{bary}$. The rotation curve feature amplitude should equal the baryonic feature amplitude — not merely correlate. Testable with high-resolution HI surveys (THINGS, Walter et al., 2008) paired with photometric profiles.

2. **Transition radius.** The correspondence activates sharply where $a_\text{bary}(r)$ drops below $a_\text{obs}(r)$, coinciding with $a \approx a_0$.

3. **Asymmetry test.** Dips in baryonic density (constraint tightening) should show slightly more scatter than bumps (constraint relaxing), because tightening updates have larger step sizes in subgradient methods.

4. **Morphological independence.** Because the dual variable depends only on the local acceleration deficit, Renzo's Rule should hold identically across galaxy types with no dependence on merger history or feedback physics. This is observed (Sancisi, 2004; Lelli, McGaugh & Schombert, 2016).

### 5.2 Mode Structure

If the dark matter halo is the spatial signature of convergence around the optimization's saddle point, its radial profile should contain residual oscillatory structure at a characteristic scale set by the dual update step size — not a smooth NFW profile. Observations of galaxy rotation curves do show fine structure beyond smooth fits; whether this structure matches dual-variable oscillation is an empirical question.

### 5.3 Strong-Field Subharmonics: QPOs and Nodal Geometry

The bidirectional mechanism (§1.1) predicts subharmonic signatures in any astrophysical medium, not only the low-acceleration regime. Accretion disks are the natural test: differentially rotating, nonlinear, threshold-rich (MRI activation), and they produce QPOs with integer and half-integer frequency ratios (3:2, 2:1, 3:1).

The critical distinction: QPO subharmonics arise from the disk's own threshold parameters, not from $a_0$. The acceleration at QPO-producing radii (~$10^8$ m/s² for stellar-mass black holes) is eighteen orders of magnitude above $a_0$. The framework predicts universal *structure* (threshold → subharmonic) with medium-dependent *threshold values*.

**Why 3:2 is universal.** The string analogy explains not just *that* subharmonics appear but *which* ones dominate. The second harmonic has a node at $1/2$; the third has nodes at $1/3$ and $2/3$. These positions are simultaneously nodes of one harmonic and antinodes of the adjacent one. This geometric collision — where one mode's maximum displacement coincides with another's zero crossing — creates the strongest possible coupling between adjacent harmonics. The 3:2 ratio is not selected dynamically; it is selected geometrically by the nodal structure of the medium.

An accretion disk has radial mode structure. If stick-slip produces subharmonic mode-locking, the locked frequencies reflect the nodal geometry. The 3:2 ratio is universal across black hole masses because nodal positions at $1/3$ and $2/3$ of the relevant radial extent are dimensionless fractions, independent of physical size. The mass-independence that makes 3:2 QPOs puzzling for resonance models is what nodal geometry predicts.

**Spin dependence.** The black hole spin parameter $a^*$ shifts the ISCO radius, changing shear rate and tidal coupling. Retrograde disks ($a^* < 0$) should exhibit QPO onset at different accretion rates than prograde disks of the same mass. X-ray binaries with measured spins and QPOs (e.g., GRS 1915+105, XTE J1550-564) provide existing data for this test.

### 5.4 No Direct Detection

If dark matter is a dual variable rather than a substance, direct detection experiments should find nothing. The dual variable modifies the gravitational field but is not a particle carrying independent energy-momentum. This is consistent with null results from XENON, LUX, and PandaX through 2026.

### 5.5 The Bullet Cluster

The Bullet Cluster (1E 0657-56) requires the gravitational lensing signal to be spatially offset from the baryonic gas after a cluster merger. In the dual-variable framing, this requires that the constraint (and therefore its multiplier) can decouple from the baryonic distribution during violent non-equilibrium events. This is plausible if the constraint is geometric (tied to the metric) rather than material (tied to the matter) — the metric need not track the gas during a rapid merger. However, this prediction needs quantitative simulation to be compelling (see §7.2).

---

## 6. Experimental Strategy

### 6.1 Resonant Detection

The stick-slip mechanism identifies two ways to enter the critical band (slow drive, excessive force) — and a collider does neither for the gravitational subharmonic. It operates at the electroweak scale, which is not the slow regime ($a_0 \sim 10^{-10}$ m/s²) and not the force-driven regime (MRI threshold). Decades of null results at colliders and direct detection experiments are consistent with being off-resonance entirely.

The alternative: match the detector to a medium whose drive/threshold ratio is in the critical band.

**Atom interferometers.** MAGIS-100 (Abe et al., 2021) and AION (Badurina et al., 2020) are sensitive to ultralight dark matter in the $10^{-15}$–$10^{-14}$ eV range — the regime where a low-frequency oscillation in the gravitational dual variable would be detectable.

**Atomic clock networks.** GPS satellite clocks can function as a planet-scale dark matter detector (Derevianko & Pospelov, 2014; Roberts et al., 2017). If the dual variable oscillates at the Lagrangian relaxation convergence frequency, clock networks are the natural instrument.

**Mid-band gravitational wave detectors** (0.01–3 Hz) fill the gap between LIGO and LISA, overlapping with predicted ultralight dark matter oscillation frequencies.

### 6.2 Laboratory Validation

Kawano et al. (2025) confirmed both entry paths for the bowed string. What remains is the full phase-space characterization: mapping the hysteresis loop, measuring energy partition between fundamental and subharmonic as a function of bow velocity and pressure jointly, and extracting the empirical Stribeck curve. The prediction: the subharmonic onset region should be a narrow diagonal band in the velocity–pressure plane, entry should be possible from both sides, and energy partition should follow the complementary slackness structure.

### 6.3 Cylinder Stick-Slip: A Tabletop QPO Analogue

A bowed string is one-dimensional with fixed endpoints. An accretion disk is two-dimensional with periodic boundary conditions. A cylinder bridges them.

A thin-walled cylindrical shell supports circumferential modes indexed by azimuthal order $m$, with $2m$ nodal meridians equally spaced. The node-antinode collision of §5.3 transfers directly: between adjacent $m = 2$ nodes (90° apart), the $m = 3$ mode places nodes at 1/3 and 2/3 of the interval — the $m = 2$ antinodes. The 3:2 ratio survives promotion from one dimension to two.

The cylinder adds something the string cannot: **traveling waves**. A standing wave $\cos(m\theta)$ decomposes into counter-rotating traveling waves $e^{\pm im\theta}$. A stick-slip subharmonic on a cylinder is, structurally, a QPO: a rotating density pattern at a frequency different from the material's orbital frequency.

**Experimental proposal.** Mount a thin-walled metal tube on bearings. Press a rosined pad tangentially. Rotate the tube at variable speed. At normal speed, the tube should sing in the $m = 2$ mode (wine-glass regime). Below a critical speed (or above a critical pressure), the prediction is that the $m = 3$ mode activates, the spectrum shows 3:2 peaks, and the mode pattern is a traveling wave. This constitutes a tabletop QPO generator.

The accretion disk adds differential rotation: angular velocity falls as $r^{-3/2}$, so the shear rate (drive) varies with radius, and the stick-slip threshold is crossed at a specific radius. But the mode numbers are integers, and the ratio of integers does not depend on the mass of the black hole. This is why 3:2 is mass-independent.

---

## 7. Open Questions

### 7.1 Cosmological Scaling

The paper operates at galaxy and cluster scales. Particle CDM earns its strongest results at cosmological scales — CMB acoustic peaks, baryon acoustic oscillations, the matter power spectrum — with sub-percent precision. The honest position: this framework has not been applied at cosmological scales. Mimetic gravity's Lagrange multiplier does admit cosmological solutions (Sebastiani et al., 2017; Nojiri & Odintsov, 2014), but "not ruled out" is not "predicts the right peak positions." Until the dual-variable framework reproduces these, it should be understood as a framework for galactic-scale phenomenology, not a complete ΛCDM alternative.

*Partial progress:* The [harmonics](https://github.com/nickjoven/harmonics) synchronization cost framework connects to cosmological parameters ($H_0$, $\Lambda$) via the [a₀ threshold derivation](https://github.com/nickjoven/harmonics/blob/main/sync_cost/derivations/03_a0_threshold.md) and derives spectral tilt from cost scaling ([`04_spectral_tilt.md`](https://github.com/nickjoven/harmonics/blob/main/sync_cost/derivations/04_spectral_tilt.md)). Sub-percent CMB/BAO accuracy remains undemonstrated.

### 7.2 Spatial Decoupling

The Bullet Cluster requires quantitative simulation showing that the constraint's spatial profile evolves independently of the baryonic distribution during a violent merger. Collisionless particle dark matter explains the offset naturally; the dual-variable interpretation needs a simulation demonstrating the same. This remains the strongest single objection to any non-particle framework.

### 7.3 Cluster Convergence

Galaxy clusters are where MOND underperforms — predicting less dark matter than observed. In the Lagrangian relaxation framing, this may indicate convergence failure: the multi-constraint optimization in clusters (hot gas, ram pressure, merger history) prevents single-constraint relaxation from finding the correct dual value. This predicts that cluster dark matter requires a multi-constraint formulation.

*Partial progress:* The harmonics [golden ratio selection mechanism](https://github.com/nickjoven/harmonics/blob/main/sync_cost/derivations/05_golden_ratio.md) may explain why single-constraint relaxation fails at cluster scales — the multi-mode structure requires a different convergence path.

### 7.4 From Schematic to Quantitative

The companion notebook (`stick_slip_lagrangian.ipynb`) demonstrates the mechanism schematically: threshold produces subharmonic, dual-variable iteration converges or diverges. But the primal variables are held fixed, each shell is independent, and the dual variable converges to the known deficit by construction. The gap between this and genuine Lagrangian relaxation of a gravitational action has been partially closed: the companion paper (Joven, 2026, "Gravity as Synchronization in a Frictional Medium") identifies the constraint as the Einstein-Hilbert action in ADM form, with the Hamiltonian constraint providing the locally-defined optimization. What remains is solving the coupled problem on observed baryonic mass profiles to produce rotation curves without free parameters.

### 7.5 The Square Wave Limit

The idealized stick-slip waveform is a square wave — instantaneous alternation between stuck and slipping states. Its Fourier series contains only odd harmonics ($f$, $3f$, $5f$, ...) with $1/n$ amplitude decay. If the gravitational stick-slip has cascaded through period-doublings toward this limit, the halo's radial profile should contain the odd-harmonic signature. The companion notebook (`08_square_wave_bifurcation.ipynb`) explores this numerically.

---

## 8. Conclusion

The dark matter problem may be an optimization problem. The hypothesis requires no new particles, no new forces, and no modifications to general relativity at the level of the action. What changes is interpretation: the Lagrange multiplier of mimetic gravity is a shadow price, and the dark matter halo is the cost the gravitational field pays where baryonic matter is insufficient to satisfy a geometric constraint.

The framework's sharpest prediction is Renzo's Rule: because the shadow price is local, every feature in the baryonic luminosity profile must be mirrored in the rotation curve — not as a correlation but as a theorem. High-resolution surveys already contain the data; the prediction is feature-for-feature amplitude matching in the low-acceleration regime with no free parameters.

The framework's deepest structural claim is the bidirectional threshold. A bowed string produces its subharmonic via slow velocity or high pressure. Galaxies enter the critical band from the slow side; inner accretion disks enter from the force side. If both cases produce subharmonic artifacts derivable from the same Stribeck-type transfer function — rotation curves in one regime, QPO frequency ratios in the other — the mechanism is not an analogy. It is the dynamics.

---

## Summary

**Claim.** Dark matter effects are dual variables of a constrained optimization — shadow prices the gravitational field pays to enforce a geometric constraint (mimetic gravity's gradient normalization) where baryonic matter alone is insufficient.

**Mechanism.** Stick-slip dynamics: a threshold-mediated relaxation oscillation that can be entered by slow drive (galactic outskirts, $a < a_0$) or by excessive drive (inner accretion disks, QPOs). Two paths, one mechanism.

**Key predictions.** (1) Renzo's Rule follows from complementary slackness: feature-for-feature amplitude matching between baryonic profiles and rotation curves, no free parameters. (2) QPO frequency ratios (especially 3:2) are determined by the nodal geometry of the medium, not by independent resonance modes. (3) No direct detection of dark matter particles. (4) Medium-dependent thresholds: the structural form is universal, the threshold value is not.

**Open.** Cosmological scaling, Bullet Cluster quantitative simulation, coupled primal-dual solution on observed mass profiles.

---

## References

- Abe, M. et al. (MAGIS-100 Collaboration) (2021). Matter-wave Atomic Gradiometer Interferometric Sensor (MAGIS-100). *Quantum Sci. Technol.*, 6, 044003. arXiv:2104.02835.
- Badurina, L. et al. (2020). AION: An Atom Interferometer Observatory and Network. *JCAP*, 05, 011. arXiv:1911.11755.
- Berezhiani, L., & Khoury, J. (2015). Theory of dark matter superfluidity. *Phys. Rev. D*, 92(10), 103510.
- Brace, W. F., & Byerlee, J. D. (1966). Stick-slip as a mechanism for earthquakes. *Science*, 153(3739), 990-992.
- Capozziello, S., Matsumoto, J., Nojiri, S., & Odintsov, S. D. (2010). Dark energy from modified gravity with Lagrange multipliers. arXiv:1004.3691v2.
- Chaichian, M., Klusoň, J., Oksanen, M., & Tureanu, A. (2014). Mimetic dark matter, ghost instability and a mimetic tensor-vector-scalar gravity. *JHEP*, 2014(12), 102. arXiv:1404.4008.
- Chamseddine, A. H., & Mukhanov, V. (2013). Mimetic dark matter. *JHEP*, 2013(11), 135.
- Chamseddine, A. H., & Mukhanov, V. (2014). Cosmology with mimetic matter. *JCAP*, 2014(6), 017. arXiv:1403.3961.
- Derevianko, A., & Pospelov, M. (2014). Hunting for topological dark matter with atomic clocks. *Nature Physics*, 10, 933-936. arXiv:1311.1244.
- Ekeland, I., & Temam, R. (1976). *Convex Analysis and Variational Problems*. North-Holland.
- Fisher, M. L. (1981). The Lagrangian relaxation method for solving integer programming problems. *Management Science*, 27(1), 1-18.
- Held, M., & Karp, R. M. (1971). The traveling-salesman problem and minimum spanning trees: Part II. *Math. Programming*, 1(1), 6-25.
- Joven, N. (2026). Gravity as synchronization in a frictional medium. *Preprint*.
- Kawano, S., Kobayashi, K., Suzuki, T., & Ichiji, N. (2025). Experimental Validation of String Oscillation in Subharmonic Generation. arXiv:2502.11902.
- Lelli, F., McGaugh, S. S., & Schombert, J. M. (2016). SPARC: Mass models for 175 disk galaxies with Spitzer photometry and accurate rotation curves. *AJ*, 152(6), 157. arXiv:1606.09251.
- McGaugh, S. S., Lelli, F., & Schombert, J. M. (2016). Radial acceleration relation in rotationally supported galaxies. *Phys. Rev. Lett.*, 117(20), 201101.
- Milgrom, M. (1983). A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis. *ApJ*, 270, 365-370.
- Navarro, J. F., Frenk, C. S., & White, S. D. M. (1997). A universal density profile from hierarchical clustering. *ApJ*, 490(2), 493-508.
- Nojiri, S., & Odintsov, S. D. (2014). Mimetic F(R) gravity: inflation, dark energy and bounce. *Mod. Phys. Lett. A*, 29(40), 1450211. arXiv:1408.3561.
- Roberts, B. M. et al. (2017). Search for domain wall dark matter with atomic clocks on board global positioning system satellites. *Nature Communications*, 8, 1195. arXiv:1704.06844.
- Sancisi, R. (2004). The visible matter – dark matter coupling. *IAU Symposium*, 220, 233-240. arXiv:astro-ph/0311348.
- Sebastiani, L., Vagnozzi, S., & Myrzakulov, R. (2017). Mimetic gravity: a review of recent developments and applications to cosmology and astrophysics. *Advances in High Energy Physics*, 2017.
- Verlinde, E. (2016). Emergent gravity and the dark universe. *SciPost Phys.*, 2(3), 016.
- Walter, F. et al. (2008). THINGS: The HI Nearby Galaxy Survey. *AJ*, 136(6), 2563-2647. arXiv:0810.2125.

---

*Companion notebooks: `stick_slip_lagrangian.ipynb`, `08_square_wave_bifurcation.ipynb`, `09_cylinder_stick_slip.ipynb`*
