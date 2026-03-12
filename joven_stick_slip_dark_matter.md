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

## 2. The Stick-Slip Regime Is a Ratio, Not a Direction

The empirical facts of the dark matter problem locate the anomaly where the stick-slip model predicts — but the model is more general than the galactic case alone.

### 2.1 The Galactic Instance

Galaxy rotation curves deviate from Newtonian predictions not at the center (high acceleration, strong field) but at the outskirts (low acceleration, weak field). The mass discrepancy-acceleration relation (McGaugh et al., 2016) shows that the discrepancy between observed and predicted gravity is a function of acceleration alone, with a characteristic scale $a_0 \approx 1.2 \times 10^{-10}$ m/s².

Milgrom's MOND interpolating function $\mu(x)$, where $x = a/a_0$, transitions smoothly between Newtonian ($\mu \to 1$ for $x \gg 1$) and deep-MOND ($\mu \to x$ for $x \ll 1$) regimes. This smooth transition is characteristic of stick-slip: the Stribeck curve (friction vs. velocity in tribology) shows exactly this shape — a smooth, monotonic transition between static-friction-dominated and kinetic-friction-dominated regimes with a characteristic velocity scale.

### 2.2 The Threshold Is Medium-Dependent

The stick-slip framework does not require the threshold to be a universal constant. It requires a threshold to exist in the medium's transfer function. The Stribeck curve is parameterized by the ratio of drive to threshold — not by the absolute value of either. The critical band can be entered from either direction:

1. **Drive decreases below threshold** (galaxy outskirts: acceleration drops below $a_0$)
2. **Threshold increases above drive** (a medium with different critical parameters shifts the transition to a new scale)

The value $a_0 \approx 1.2 \times 10^{-10}$ m/s² is the threshold for spacetime geometry at galactic scales. Other media have their own thresholds:

| System | Medium | Drive parameter | Threshold | Subharmonic artifact |
|---|---|---|---|---|
| Galaxy | Spacetime geometry | Gravitational acceleration | $a_0$ | Dark matter halo |
| Accretion disk | Ionized plasma + magnetic fields | Orbital shear rate | MRI critical wavelength | Quasi-periodic oscillations |
| Atmosphere | Scattering particulates | Source spatial frequency | Mean free path × coherence | Optical halo |
| Bowed string | Rosin friction layer | Bow velocity | $v_{threshold}$ | Subharmonic tone |

In every case, the subharmonic appears when the drive/threshold ratio enters a critical band. The band is narrow and diagonal in the parameter space (see §2 of the companion visualization): you can enter it by slowing the drive or by changing the medium's coupling. The framework is structural, not numerical — $a_0$ is the galactic instance of a universal mechanism, not a universal constant.

### 2.3 Consequences for Strong-Field Systems

This generalization makes a specific prediction: nonlinear threshold dynamics should produce subharmonic signatures in *any* astrophysical medium, not only in the low-acceleration galactic regime. Accretion disks around compact objects are a natural test case. They are differentially rotating, nonlinear (viscosity, turbulence, magnetic fields), and threshold-rich (the magnetorotational instability activates at a critical wavelength). Quasi-periodic oscillations (QPOs) in black hole X-ray binaries show integer and half-integer frequency ratios — 3:2, 2:1, 3:1 — that are exactly the subharmonic signatures the stick-slip model produces.

The critical distinction: QPO subharmonics arise from the accretion disk's own threshold parameters (MRI activation, viscous-to-thermal timescale ratio, ISCO geometry), not from $a_0$. The acceleration at QPO-producing radii (~$10^8$ m/s² for stellar-mass black holes) is eighteen orders of magnitude above $a_0$. The framework predicts that the *structure* (threshold → subharmonic) is universal while the *threshold value* is medium-dependent. If QPO frequency ratios can be derived from the disk's Stribeck-type transfer function — its own critical drive/threshold ratio — that would validate the structural claim without requiring $a_0$ to appear where it has no business appearing.

This restores a symmetry that §1's correction appeared to break. The sonic correction established that the viola's subharmonic emerges from slow velocity, not extreme pressure — and the galactic dark matter case follows the same path (low acceleration, not strong field). But the inner accretion disk enters the stick-slip band from the *opposite* direction: extreme tidal shear, extreme magnetic coupling, extreme radiation pressure. This is genuinely the "pressed firmly" regime. The same phase diagram that shows the subharmonic band as a narrow diagonal admits entry from both sides. The viola correction was right for the viola and right for galaxies, but the mechanism itself is bidirectional. An accretion disk, uniquely, may exhibit both modes simultaneously — slow-drive subharmonics in the outer disk (where the dark matter problem lives) and force-driven subharmonics in the inner disk (where QPOs are observed). If both can be shown to arise from the same Stribeck-type transfer function of the disk medium, that would be strong evidence that the mechanism is one.

### 2.4 The Mapping

| Stick-slip parameter | Gravitational analogue |
|---|---|
| Relative velocity | Drive/threshold ratio in the relevant medium |
| Critical velocity | Medium-dependent threshold ($a_0$ at galactic scale) |
| Static friction (stick) | Enhanced coupling (deep-MOND, MRI-locked) |
| Kinetic friction (slip) | Standard dynamics (Newtonian, Keplerian) |
| Subharmonic energy | Anomalous mode (DM halo, QPO, optical halo) |
| Damping coefficient | Dissipation in the medium |

The subharmonic — energy appearing at a scale the linear theory does not predict — is the halo. The specific halo (dark matter, quasi-periodic oscillation, optical glare) depends on the medium. The mechanism is one.

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

### 4.3 When the Constraint Binds

In Lagrangian relaxation, the dual variable is nonzero only when the constraint is active (complementary slackness). The constraint becomes active — and the dual variable takes a nonzero value — whenever the drive/threshold ratio enters the critical band. In the galactic case, this happens at the low-acceleration end:

- **Mid-range acceleration (fast bow)**: kinetic friction sustained, no stick phase, no subharmonic. Gravity is Newtonian, no dark matter needed.
- **Low acceleration (slow bow)**: kinetic friction cannot be maintained, system enters stick-slip, subharmonic appears. The geometric constraint binds, the dual variable activates, "dark matter" emerges.

But complementary slackness is symmetric in the ratio. The constraint can also bind when the drive is strong enough to *overwhelm* the medium's dissipative capacity — the "pressed firmly" regime. An accretion disk around a stellar-mass black hole is a physical system where this occurs. The disk flattens under its own pressure and tidal shear; angular momentum transport is governed by the magnetorotational instability, which activates above a critical wavelength; the resulting turbulent viscosity produces stick-slip-like transitions between laminar and turbulent flow. The dual variable in this system is not dark matter — it is whatever the medium's transfer function must pay to satisfy its own geometric constraint (angular momentum conservation in a flattening geometry under extreme shear). The observable is the QPO, not the halo. But the mechanism — constraint binding, dual variable activation, subharmonic generation — is the same.

The MOND acceleration scale $a_0$ is the critical coupling of the stick-slip transition at galactic scales — the point at which spacetime geometry can no longer satisfy its geometric constraint using baryonic matter alone and must pay a dual-variable cost. Other media have their own critical couplings. The dual variable is universal; the threshold is not.

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

### 5.3 Strong-Field Subharmonics

If the mechanism is bidirectional, it predicts observable subharmonic signatures in strong-field systems where the drive *exceeds* the medium's dissipative threshold — not only where it falls below. Accretion disks are the sharpest test. The disk is a medium with its own transfer function: angular momentum is transported by turbulent viscosity (driven by the MRI), the disk flattens under pressure and tidal forces, and the geometry imposes conservation constraints that the medium cannot satisfy smoothly when driven too hard. The prediction: QPO frequency ratios (3:2, 2:1, 3:1) should be derivable from the disk's Stribeck-type transfer function — the ratio of orbital shear rate to MRI critical wavelength — without invoking resonance between independent oscillation modes. If the same functional form (drive/threshold ratio → subharmonic spectrum) that fits the MOND interpolating function at galactic scales also fits QPO frequency structure at accretion-disk scales, the structural claim is validated across eighteen orders of magnitude in acceleration.

An accretion disk may be the only astrophysical system that exhibits both entry modes simultaneously: slow-drive subharmonics in the outer disk (where the dark matter problem lives) and force-driven subharmonics in the inner disk (where QPOs are observed). If both arise from the same Stribeck-type transfer function of the disk medium, that is strong evidence that the mechanism is one.

### 5.4 No Direct Detection

If dark matter is a dual variable rather than a primal variable (a substance), direct detection experiments should find nothing. The dual variable has physical effects (it modifies the gravitational field) but is not a particle that carries energy-momentum independently of the constraint it enforces. This is consistent with the null results from XENON, LUX, PandaX, and other direct detection experiments through 2026.

### 5.5 The Bullet Cluster

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
6. The identification of the dark matter problem as an adiabatic-limit phenomenon favoring resonant over high-energy detection
7. The structural correspondence between the clockwork mechanism and stick-slip period doubling
8. The generalization from a monodirectional threshold ($a < a_0$) to a medium-dependent drive/threshold ratio, unifying galactic dark matter with accretion disk QPOs and atmospheric scattering under one mechanism

---

## 9. Experimental Implications: Resonant Detectors, Not Colliders

*This section incorporates observations contributed by Gemini (Google DeepMind) and DeepSeek during collaborative review. The adiabatic limit framing and resonant detection strategy were identified by Gemini. The QPO prediction and accretion disk as test case were identified by DeepSeek; the numerical falsification of $a_0$ as the QPO threshold and the subsequent generalization to medium-dependent thresholds (§2.2–2.3) were developed in response.*

### 9.1 The Adiabatic Limit

The stick-slip framing identifies a specific regime: the subharmonic emerges when the drive/threshold ratio enters a critical band. There are two ways to enter — decrease the drive below the medium's threshold (slow bow) or increase the drive until it overwhelms the medium's dissipative capacity (pressed firmly). Both produce subharmonics; which mode dominates depends on the medium.

For the galactic dark matter problem, the entry is from below: cosmic expansion is slow, galactic accelerations are small, the gravitational field enters the stick-slip band through patience. For accretion disks, the entry is from above: tidal shear and magnetic pressure exceed the disk's capacity to transport angular momentum smoothly, and the system mode-locks into QPO subharmonics. The mechanism is one; the direction of entry is medium-dependent.

This has a direct experimental consequence. A collider does not fail because force is the wrong approach in general — force-driven subharmonics are real (§2.3, §5.3). A collider fails because it is not tuned to *any* medium's critical band for the gravitational subharmonic. It operates at the electroweak scale, which is neither the slow regime (galactic, $a_0 \sim 10^{-10}$ m/s²) nor the force-driven regime (accretion disk, MRI threshold). It is simply off-resonance. You need a detector tuned to a regime where the drive/threshold ratio actually enters the critical band.

### 9.2 From High-Energy to Resonant Detection

The shift in detection strategy follows directly from the model:

**Off-resonance (current approach):** Build larger colliders (LHC, proposed FCC) to force interactions at higher energies. This searches for dark matter as a particle at the electroweak scale — neither the slow regime where the galactic subharmonic lives nor the force-driven regime where accretion disk subharmonics live. Decades of null results at colliders and direct detection experiments (XENON, LUX, PandaX) are consistent with this being the wrong critical band entirely.

**On-resonance (proposed approach):** Match the detector to a medium whose drive/threshold ratio is in the critical band. For the galactic subharmonic, this means slow detectors — instruments that measure quantities drifting over time at the gravitational convergence frequency. For the accretion disk subharmonic, the detectors already exist: X-ray timing instruments observing QPO frequency ratios.

Three classes of slow detectors are directly relevant:

**Atom interferometers** measure differential acceleration between quantum superpositions of atomic states with extraordinary precision. MAGIS-100, a 100-meter atom interferometer at Fermilab (Abe et al., 2021), and AION, a staged UK programme using cold strontium atoms (Badurina et al., 2020), are sensitive to ultralight dark matter in the $10^{-15}$–$10^{-14}$ eV mass range — precisely the regime where a low-frequency oscillation in the gravitational dual variable would produce a detectable signal.

**Atomic clock networks** detect oscillations in fundamental constants caused by dark matter fields passing through the network. Derevianko and Pospelov (2014) proposed using GPS satellite clocks as a planet-scale dark matter detector, subsequently realized using 16 years of GPS archival data (Roberts et al., 2017). If the dual variable oscillates at the Lagrangian relaxation convergence frequency, clock networks are the natural instrument: they measure the slow drift of a quantity (the fine-structure constant, clock transition frequencies) against a reference, exactly as the subgradient update measures constraint violation against a target.

**Gravitational wave detectors in the mid-band** (0.01–3 Hz) fill the gap between LIGO (high frequency) and LISA (low frequency). Both MAGIS and AION target this band, which overlaps with the oscillation frequencies predicted by ultralight dark matter models.

### 9.3 The Clockwork Connection

The Clockwork mechanism (Giudice & McCullough, 2017) provides a specific field-theoretic realization of the "slow gearing" intuition. In a clockwork model, a chain of $N$ fields with nearest-neighbor interactions produces an exponential hierarchy: the lightest mode has coupling suppressed by $q^N$ relative to the fundamental scale, where $q$ is the gear ratio. This is literally a system of interlocking gears that converts high-frequency driving into low-frequency output — the same frequency-reduction mechanism as stick-slip period doubling, implemented in field space rather than mechanical space.

The structural correspondence:

| Stick-slip | Clockwork |
|---|---|
| Fundamental frequency | UV scale coupling |
| Subharmonic (period doubling) | IR zero mode (exponentially suppressed) |
| Gear ratio (static/kinetic friction) | Clockwork ratio $q$ |
| Number of stick-slip cycles | Number of sites $N$ |
| "Slow bow" condition | Adiabatic limit of the gear chain |
| "Pressed firmly" condition | Overdriven gear chain (mode-locking) |

If dark matter is the dual variable of a constrained optimization problem, the clockwork mechanism provides a candidate UV completion: the constraint arises from a chain of fields whose collective low-frequency mode is the subharmonic we observe as the dark matter effect. The exponential suppression explains why the galactic threshold $a_0 \approx 1.2 \times 10^{-10}$ m/s² is so far below the Planck or electroweak scales — it is a clockworked-down version of a fundamental-scale coupling, exactly as the subharmonic is a geared-down version of the string's natural frequency. Other media's thresholds (e.g., the MRI critical wavelength in accretion disks) would correspond to different gear ratios $q$ or chain lengths $N$ in the clockwork — the same mechanism producing different critical scales.

### 9.4 Below the Fundamental, and Beyond It

It has long seemed unsatisfying that dark matter — the dominant gravitational component of the universe — should require explanation as something *additional* to known physics. An extra particle, an extra field, an extra sector. The stick-slip framing offers a different perspective: the dark sector is not above the fundamental. It is below it — a lower mode of the gravitational field itself, accessed when the drive/threshold ratio enters the critical band.

For galaxies, the entry is from below. The universe's expansion rate during structure formation is slow. The gravitational accelerations in galaxy outskirts are small. These are the conditions under which a bowed string produces its subharmonic — driven more patiently than the system's natural dissipation timescale. The dark matter halo is the gravitational octave that emerged when the cosmos moved slowly enough for the stick phase to dominate.

For accretion disks, the entry is from above. The inner disk is compressed, sheared, and magnetically coupled beyond the medium's capacity for smooth transport. The disk flattens — a geometric constraint asserting itself through pressure — and the system mode-locks into subharmonic oscillation. The QPO is the acoustic octave that emerges when the disk is driven harder than its viscous dissipation can absorb.

The two cases are not separate phenomena requiring separate explanations. They are the same phase diagram entered from opposite corners. The accretion disk is the critical test precisely because it may exhibit both simultaneously: the outer disk, where accelerations are low, enters from the slow side; the inner disk, where pressures are extreme, enters from the force side. One medium, two entry modes, one mechanism. If the Stribeck transfer function of the disk produces both the outer-disk mass discrepancy and the inner-disk QPO spectrum, the framework is not an analogy. It is the dynamics.

---

## 10. Conclusion

The cost of this hypothesis is low. It requires no new particles, no new forces, and no modifications to general relativity at the level of the action. It requires only that we read an existing mathematical structure (mimetic gravity's Lagrange multiplier) through an existing mathematical framework (Lagrangian relaxation) motivated by an existing physical phenomenon (stick-slip dynamics).

If the framing is correct, it narrows the search space in two ways. Theoretically, the dark matter problem becomes a question about which geometric constraint the gravitational field is optimizing against, and the acceleration scale $a_0$ is the critical coupling at galactic scales — one instance of a medium-dependent threshold. Experimentally, it redirects detection strategy from off-resonance instruments (colliders at the electroweak scale) to on-resonance ones — slow detectors (atom interferometers, clock networks, mid-band gravitational wave detectors) for the galactic subharmonic, and X-ray timing for accretion disk subharmonics.

The structure generalizes. Any system where a signal propagates through a medium — and the medium's transfer function has a critical threshold at which it mode-converts the input into subharmonic artifacts — is a candidate for the same analysis. The threshold can be entered from either direction: drive too slow (galaxies) or drive too hard (inner accretion disks). The accretion disk is the strongest test case because it enters from both sides simultaneously, and the observables (rotation curves in the outer disk, QPO frequency ratios in the inner disk) are already measured. Atmospheric optics is another such system; the halos produced by point-source headlights in fog are, structurally, the optical analogue of the dark matter halo. Whether this generalization is productive beyond the gravitational case remains to be seen.

If the framing is wrong, it has consumed one short paper and a notebook. The asymmetry favors exploration.

The thread began with a bowed string producing a tone one octave below its fundamental. The subharmonic emerged not through force but through patience — and that is how the galaxy enters the critical band. But the mechanism itself is agnostic about direction. An accretion disk, flattened under its own pressure, enters from the opposite side: too much force, too much shear, the medium overwhelmed rather than understimulated. Both produce the same mathematical object — a dual variable, a shadow price, a constraint that binds. The dark sector may not be something exotic above the Standard Model or something subtle below it. It may be the price any medium pays when its drive/threshold ratio enters the band where smooth dynamics are no longer available.

---

## References

- Abe, M. et al. (MAGIS-100 Collaboration) (2021). Matter-wave Atomic Gradiometer Interferometric Sensor (MAGIS-100). *Quantum Sci. Technol.*, 6, 044003. arXiv:2104.02835.
- Badurina, L. et al. (2020). AION: An Atom Interferometer Observatory and Network. *JCAP*, 05, 011. arXiv:1911.11755.
- Bekenstein, J. D. (2004). Relativistic gravitation theory for the modified Newtonian dynamics paradigm. *Phys. Rev. D*, 70(8), 083509.
- Berezhiani, L., & Khoury, J. (2015). Theory of dark matter superfluidity. *Phys. Rev. D*, 92(10), 103510.
- Capozziello, S., Matsumoto, J., Nojiri, S., & Odintsov, S. D. (2010). Dark energy from modified gravity with Lagrange multipliers. arXiv:1004.3691v2.
- Chamseddine, A. H., & Mukhanov, V. (2013). Mimetic dark matter. *JHEP*, 2013(11), 135.
- Derevianko, A., & Pospelov, M. (2014). Hunting for topological dark matter with atomic clocks. *Nature Physics*, 10, 933-936. arXiv:1311.1244.
- Fisher, M. L. (1981). The Lagrangian relaxation method for solving integer programming problems. *Management Science*, 27(1), 1-18.
- Giudice, G. F., & McCullough, M. (2017). A Clockwork Theory. *JHEP*, 02, 036. arXiv:1610.07962.
- Held, M., & Karp, R. M. (1971). The traveling-salesman problem and minimum spanning trees: Part II. *Math. Programming*, 1(1), 6-25.
- Joven, N. (2026). A content-addressed adaptive knowledge substrate for distributed epistemic coordination. *Preprint*.
- McGaugh, S. S., Lelli, F., & Schombert, J. M. (2016). Radial acceleration relation in rotationally supported galaxies. *Phys. Rev. Lett.*, 117(20), 201101.
- Milgrom, M. (1983). A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis. *ApJ*, 270, 365-370.
- Navarro, J. F., Frenk, C. S., & White, S. D. M. (1997). A universal density profile from hierarchical clustering. *ApJ*, 490(2), 493-508.
- Nojiri, S., & Odintsov, S. D. (2014). Mimetic F(R) gravity: inflation, dark energy and bounce. *Mod. Phys. Lett. A*, 29(40), 1450211. arXiv:1408.3561.
- Roberts, B. M. et al. (2017). Search for domain wall dark matter with atomic clocks on board global positioning system satellites. *Nature Communications*, 8, 1195. arXiv:1704.06844.
- Sebastiani, L., Vagnozzi, S., & Myrzakulov, R. (2017). Mimetic gravity: a review of recent developments and applications to cosmology and astrophysics. *Advances in High Energy Physics*, 2017.
- Sussman, G. J., & Wisdom, J. (1992). Chaotic evolution of the solar system. *Science*, 257(5066), 56-62.
- Verlinde, E. (2016). Emergent gravity and the dark universe. *SciPost Phys.*, 2(3), 016.
- Wolfram, S. (2002). *A New Kind of Science*. Wolfram Media.

---

*Companion notebook: `stick_slip_lagrangian.ipynb`*
*This paper is released under CC0.*
