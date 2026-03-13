# Stick-Slip Dynamics and the Dark Matter Dual: A Lagrangian Relaxation Interpretation of Low-Acceleration Gravity

**N. Joven** ([ORCID: 0009-0008-0679-0812](https://orcid.org/0009-0008-0679-0812))
March 2026
*Preprint — feedback welcome*

---

## Abstract

We propose a reframing of the dark matter problem through the lens of constrained optimization. The observed anomalous gravitational effects in the low-acceleration regime — galaxy rotation curves, the Tully-Fisher relation, the mass discrepancy-acceleration relation — exhibit threshold behavior structurally identical to stick-slip dynamics in mechanical systems. We show that this is not merely an analogy: the stick-slip transition is a specific instance of relaxation oscillation whose mathematical structure maps onto Lagrangian relaxation, an optimization technique in which hard constraints are replaced by penalty terms and iteratively tightened. We connect this to Chamseddine and Mukhanov's mimetic gravity (2013), in which a Lagrange multiplier enforcing a constraint on a scalar field produces cold-dark-matter-like behavior, and argue that the multiplier admits a dual interpretation as a shadow price — the cost the gravitational field pays to satisfy a constraint it cannot meet in the visible-matter variables alone. The dark matter "substance" is, in this framing, the dual variable of a constrained optimization problem. We provide a computational demonstration using Lagrangian relaxation on a parameterized gravitational potential, showing that threshold-dependent energy redistribution across scales emerges naturally from the optimization structure. Because the shadow price is local — defined at each radius by the local constraint violation — the framework produces Renzo's Rule (Sancisi, 2004) as a theorem: every feature in the baryonic luminosity profile is necessarily mirrored in the rotation curve, because the dual variable at each point is determined by the local baryonic acceleration deficit. This is the sharpest distinction from particle dark matter, where smooth, dynamically decoupled halos offer no mechanism for such fine-grained baryonic-dynamical coupling. The three-body problem alone reminds us that exact fidelity with observable matter dynamics is not available to us; the question is whether this framing narrows the search space more than particle-only models.

---

## 1. Two Ways to Make a String Sing Below Itself

A bowed string can produce a tone one octave below its fundamental frequency. The mechanism is stick-slip: the string alternates between static friction (stick — potential energy accumulates under the bow) and kinetic friction (slip — energy releases as the string snaps back). The period of this cycle is twice the natural period, producing the subharmonic.

The question is what controls the transition.

### 1.1 The Experimental Ground Truth

Kawano et al. (2025) resolved this experimentally. Using high-speed imaging to visualize spatial vibration modes and finite element simulation to model the bow-string interaction, they confirmed the mechanism underlying the Anomalous Low Frequency (ALF) technique and mapped the relevant region of the velocity-pressure parameter space. Their FEM simulations span both bow speed ($v_\text{bow}$) and pressing depth ($d_\text{bow}$), identifying **two distinct paths** through this two-dimensional space that each produce subharmonics independently:

1. **Slow bow velocity.** When $v_\text{bow}$ drops below a critical value, kinetic friction cannot be sustained — the string catches before the bow has moved enough to maintain the slip phase. The Helmholtz mode breaks down from below. This is the understimulated regime: insufficient drive to sustain smooth sliding.

2. **Increased bow pressure.** When $d_\text{bow}$ exceeds a critical value at moderate velocity, amplified frictional force suppresses the standard Helmholtz vibration mode and allows the subharmonic mode to dominate. The string is overwhelmed rather than understimulated. This is the overstimulated regime: excessive coupling that the medium cannot dissipate smoothly.

These are not two sides of the same ratio — they are **two independent causal branches** that converge on the same output: stick-slip oscillation at half the fundamental frequency. The structure is that of a bifurcation in a directed graph: two separate input paths (velocity-entry, pressure-entry) leading to the same downstream node (subharmonic generation). Both paths produce the same observable — a tone one octave below the fundamental with the characteristic spectral signature of period doubling. The subharmonic onset region in the phase diagram is a band accessible from either axis.

### 1.2 The Control Surface

This finding — that one of the present authors initially got wrong by treating pressure as the sole control variable — identifies the actual control surface. It is **two-dimensional**: a velocity axis and a pressure axis, each with its own independent threshold. Each axis has a critical value; crossing either threshold, by sufficiently different means, can drive the system into the stick-slip regime.

| Parameter | Role | Critical crossing |
|---|---|---|
| Relative velocity | Drive (bow speed relative to string) | Too slow → kinetic friction fails → stick phase from below |
| Bow pressure | Coupling strength (normal force × friction coefficient) | Too high → static friction overwhelms restoring force → stick phase from above |
| Damping | Dissipation (string/body energy absorption) | Mediates which crossing is accessible |

The two regimes produce observationally similar effects because they activate the same nonlinear mechanism — the stick-slip cycle — from opposite sides of the phase diagram. This is the bifurcation structure: the subharmonic node in the output has two independent upstream paths, not one common cause. Whether a particular physical system enters via the velocity path or the pressure path depends on which threshold it can reach with its available driving parameters.

This is the fact that the rest of the paper depends on. Every system examined below — galaxy rotation curves, accretion disk QPOs, atmospheric scattering — is a medium with a drive/threshold ratio that can enter a critical band. The direction of entry varies. The mechanism does not.

### 1.3 The Rotor Validation

The same mechanism causes documented mechanical failures in helicopter rotor systems (ground resonance, lead-lag chatter). The rotor blade's interaction with aerodynamic drag produces stick-slip oscillation when relative velocity enters the critical regime. The subharmonic mode grows because the structure lacks sufficient damping to absorb the energy redistribution. Engineers address this by:

1. Adding dampers (modifying the dissipation term)
2. Changing rotor speed (moving the velocity ratio away from the critical regime)

Both fixes move the drive/threshold ratio out of the critical band. Neither adds force; neither removes it. The control surface is two-dimensional — (drive/threshold ratio, damping coefficient) — with the critical band accessible from either axis, exactly as Kawano et al. demonstrated for the bowed string.

---

## 2. The Stick-Slip Regime Is a Ratio, Not a Direction

The empirical facts of the dark matter problem locate the anomaly where the stick-slip model predicts — but the model is more general than the galactic case alone.

### 2.1 The Galactic Instance

Galaxy rotation curves deviate from Newtonian predictions not at the center (high acceleration, strong field) but at the outskirts (low acceleration, weak field). The mass discrepancy-acceleration relation (McGaugh et al., 2016) shows that the discrepancy between observed and predicted gravity is a function of acceleration alone, with a characteristic scale $a_0 \approx 1.2 \times 10^{-10}$ m/s².

Milgrom's MOND interpolating function $\mu(x)$, where $x = a/a_0$, transitions smoothly between Newtonian ($\mu \to 1$ for $x \gg 1$) and deep-MOND ($\mu \to x$ for $x \ll 1$) regimes. The velocity-weakening branch of the Stribeck curve (friction coefficient vs. relative velocity in tribology) exhibits a structurally parallel regime transition: below a characteristic velocity, friction rises and the system enters the stick-slip regime — enhanced coupling below threshold. The full Stribeck curve is non-monotone — it has a minimum (the Stribeck minimum) before friction rises again in the hydrodynamic regime — so the correspondence is with the velocity-weakening branch only.

The structural parallel is in the threshold crossing, not the curve shapes. The MOND function $\mu(x)$ measures *how Newtonian* the system is; the Stribeck coefficient measures *how coupled*. These are complements: $(1 - \mu)$ and the Stribeck friction coefficient both measure *excess coupling*, and both are high below the characteristic scale and decline to zero above it. They are not "opposite directions" — they are the same transition measured in complementary units. The choice to plot $\mu$ rather than $(1 - \mu)$ is a convention of the MOND literature, not a structural fact.

What both curves share is a **below-fundamental transition**: a characteristic scale below which the system enters the subharmonic regime. The bowed string produces a tone *below* its fundamental when the drive crosses *below* the critical velocity. The galaxy produces gravitational effects *beyond* Newtonian prediction when acceleration drops *below* $a_0$. Both are threshold crossings from above, producing effects below the fundamental mode. This is the structural invariant — the below-fundamental transition — and it is independent of whether the coupling is plotted as a friction coefficient, an interpolating function, or a dark matter fraction.

The analogy is qualitative rather than functional: MOND interpolating functions commonly take rational or square-root forms ($\mu(x) = x/(1+x)$ or $\mu(x) = x/\sqrt{1+x^2}$), while the Stribeck velocity-weakening branch is typically fit with exponential or polynomial decay. The functional forms differ; the below-fundamental transition does not.

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
| Fault zone | Crustal rock / fault gouge | Tectonic strain rate | Rate-and-state friction | Earthquake recurrence |
| AV node | Cardiac tissue | SA node firing rate | Refractory period$^{-1}$ | 2:1, 3:1 heart block |
| Josephson junction | SIS barrier | AC bias current | Critical current $I_c$ | Shapiro steps ($nhf/2e$) |

The term "stick-slip" was coined by Brace and Byerlee (1966) for seismic fault experiments; the seismic case is the original domain of the mechanism, the galactic case a cross-domain instance.

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

Both systems are instances of iterative saddle-point seeking with two timescales. The correspondence operates at the level of dynamical classification — both are relaxation oscillations in the sense of van der Pol — rather than a proven isomorphism between state spaces. The mapping sends a primal quantity (elastic energy) in stick-slip to a dual quantity ($\lambda$) in Lagrangian relaxation, which are categorically different mathematical objects. What we claim is shared structure, not identity:

| Stick-slip component | Lagrangian relaxation component |
|---|---|
| Accumulated elastic energy (stick) | Dual variable $\lambda$ (constraint violation accumulates) |
| Threshold (static → kinetic friction) | Complementary slackness condition ($\lambda \cdot (b - g(\mathbf{x})) = 0$) |
| Energy release (slip) | Primal update (inner solve snaps to new optimum) |
| Subharmonic mode | Dual oscillation around saddle point |
| Convergence to steady oscillation | Convergence to optimal $\lambda^*$ |
| Divergence (rotor failure) | Step size too large (dual diverges) |

Both are instances of iterative saddle-point seeking in a non-smooth optimization landscape, where the primal and dual variables evolve on different timescales. We do not claim these correspondences constitute a mathematical isomorphism. The claim is weaker but still nontrivial: the two-timescale, threshold-mediated, oscillatory convergence structure is shared, and this shared structure is what motivates the application of Lagrangian relaxation to the gravitational problem.

---

## 4. Dark Matter as a Dual Variable

### 4.1 The Mimetic Gravity Precedent

Chamseddine and Mukhanov (2013) demonstrated that adding a constraint to the gravitational action via a Lagrange multiplier produces cold-dark-matter-like behavior. Specifically, imposing

$$g^{\mu\nu} \partial_\mu \phi \partial_\nu \phi = 1$$

on a scalar field $\phi$ via a multiplier $\lambda$ modifies the Einstein equations such that the multiplier contributes a dust-like energy-momentum tensor. The "dark matter" is not a new particle — it is the dynamical consequence of enforcing a constraint on the metric.

This result has been developed extensively (Sebastiani et al., 2017), extended to F(R) gravity where the Lagrange multiplier mechanism produces inflation, dark energy, and bounce cosmologies (Nojiri & Odintsov, 2014), and the related approach applied to dark energy (Capozziello, Matsumoto, Nojiri & Odintsov, 2010), but always within the field-theoretic framing: the multiplier is a mathematical device that enforces a symmetry or constraint, and the resulting phenomenology happens to resemble dark matter.

**Known stability concerns.** The minimal Chamseddine-Mukhanov formulation carries well-documented technical pathologies (Chaichian et al., 2014; Sebastiani et al., 2017): (1) a *ghost instability* in which the Lagrange multiplier's Hamiltonian can become unbounded below for certain initial configurations; (2) *caustic formation* arising from the pressureless dust dynamics (zero sound speed), which precludes primordial perturbation generation in cosmological applications; and (3) *superluminal propagation* of lower helicity modes relative to photons on the background metric — not a violation of causality defined by that metric, but a sign that the minimal formulation is an effective rather than fundamental theory. Higher-derivative extensions (Chamseddine & Mukhanov, 2014) and ghost-free scalar extensions resolve most of these issues. The optimization-theoretic reinterpretation developed here should be understood as operating in such an extended framework, where these pathologies are absent, rather than in the minimal original form.

### 4.2 The Optimization-Theoretic Reframing

We propose reading mimetic gravity through the lens of Lagrangian relaxation.

**The constraint being optimized against is explicit.** It is the gradient normalization condition of Chamseddine and Mukhanov (2013):

$$g^{\mu\nu} \partial_\mu \phi \partial_\nu \phi = 1$$

This is a geometric requirement on the scalar field $\phi$: its gradient, measured against the spacetime metric, must have unit norm everywhere. This is the constraint the gravitational field cannot satisfy using visible matter alone in the low-acceleration regime. The optimization problem is: find the metric $g_{\mu\nu}$ that satisfies the Einstein equations *and* enforces this normalization, given the observed baryonic source. The dual variable $\lambda$ is the Lagrange multiplier enforcing the normalization; the dark matter contribution is its dynamical shadow.

Without specifying this constraint, the optimization problem cannot be solved — the dual variable is only meaningful relative to what is being optimized against. All quantitative predictions in §5 (Renzo's Rule amplitudes, transition radii, convergence structure) depend on this constraint specification. This is what closes the framework: the shadow price at each radius is the cost of enforcing the unit-norm condition given the local baryonic mass distribution.

**The Lagrange multiplier is a shadow price.** In optimization theory, the dual variable $\lambda^*$ at the optimum has a precise economic interpretation: it is the marginal value of relaxing the constraint by one unit. If the constraint $g(\mathbf{x}) \leq b$ is active, then $\lambda^*$ tells you how much the objective would improve if $b$ were increased by $\epsilon$.

Applied to mimetic gravity: **the dark matter field is the cost the gravitational field pays to satisfy the gradient normalization constraint it cannot meet using visible matter alone.** The multiplier (dark matter) is what it costs to enforce the unit-norm geometry given the available baryonic matter distribution.

**A caveat on the analogy's scope.** Shadow prices are rigorously defined in finite-dimensional constrained optimization under well-understood conditions (convexity, constraint qualification). Mimetic gravity's Lagrange multiplier is a field-theoretic object enforcing a constraint at every spacetime point — an infinite-dimensional variational problem. The extension of shadow price theory to infinite dimensions exists (Ekeland & Temam, 1976) but requires additional regularity (strong duality, Fréchet differentiability of the value function with respect to constraint perturbations). Whether mimetic gravity's action satisfies these conditions — particularly convexity in the relevant variables — is an open technical question. We use "shadow price" here as an interpretive lens, not a proven theorem: the Lagrange multiplier *behaves like* a shadow price (it is nonzero only where the constraint binds, and its magnitude reflects the cost of enforcement), and this interpretation generates testable predictions (§5), but the rigorous infinite-dimensional duality theory remains to be established for this specific action.

**The constraint is geometric; the price is dynamical.** This distinction has a consequence that is easy to understate: **the topology of spacetime is unchanged.** The dual variable modifies how matter moves through spacetime — the dynamics — without modifying what spacetime is — the geometry. No new fields are added to the metric. No extra dimensions are compactified. No topological defects are introduced. The manifold structure, the causal structure, and the light cone structure of general relativity are preserved exactly. What changes is the cost function: the gravitational field pays a price (the dual variable) to maintain the geometric constraint that it would satisfy for free if baryonic matter were sufficient. The "dark matter" is not a thing in spacetime. It is a property of the optimization problem that spacetime is solving.

This claim requires one qualification: it holds at the level of the background geometry. As noted in §4.1, the mimetic gravity framework in its minimal form admits superluminal perturbation modes. The statement "topology of spacetime is unchanged" refers to the manifold and its metric, not to the propagation speeds of perturbed modes, and it remains true in extended formulations that resolve the perturbation-level issues.

The dark matter halo profile is therefore not an arbitrary density distribution — it is shaped by the optimization landscape. Specifically, it should reflect the structure of the dual problem: where the constraint is most binding (galaxy outskirts, low acceleration), the dual variable (dark matter density) is largest.

This is exactly what is observed. The mass discrepancy-acceleration relation (McGaugh, Lelli & Schombert, 2016) shows that the "dark matter fraction" increases monotonically as acceleration decreases. The constraint is most expensive to enforce precisely where the baryonic matter provides the least gravitational acceleration.

### 4.3 Renzo's Rule: The Local Test

The mass discrepancy-acceleration relation is a global statistical trend — averaged over many galaxies, the dark matter fraction correlates with total acceleration. But because the shadow price is **local** — defined independently at each radius by the constraint violation at that radius — the framework makes a much stronger prediction.

Renzo's Rule (Sancisi, 2004) is the empirical observation that for every feature in the baryonic luminosity profile of a galaxy, there is a corresponding feature in the rotation curve, and vice versa. A bump in surface brightness at some radius produces a bump in the rotation curve at the same radius. A dip in baryonic density produces a dip in rotational velocity. The correspondence is detailed, galaxy-by-galaxy, radius-by-radius.

This is difficult for particle dark matter. An NFW halo (Navarro, Frenk & White, 1997) is smooth — it has no mechanism to develop fine structure that tracks baryonic features. The halo and the baryonic disk are dynamically decoupled: the halo formed first, the baryons fell in later, and the halo's radial profile is set by cosmological accretion history, not by the current baryonic distribution. Reproducing Renzo's Rule in ΛCDM requires elaborate baryonic feedback models (adiabatic contraction, supernova-driven outflows) that must be tuned galaxy by galaxy. The correlation is observed to hold across morphological types with no apparent dependence on feedback history.

In the Lagrangian relaxation framing, Renzo's Rule is not a correlation to be explained. **It is a theorem — conditional on the optimization structure.**

The conditional is important and we state it explicitly: *if* the gravitational field at each radius can be described as solving a locally-defined constrained optimization — with the dual variable at each point set by the local constraint violation — *then* the following derivation is exact. This is the framework asserted in §3–4; its physical justification is the open problem identified in §10.3.

Given that conditional, the dual variable at each radius at the fixed point satisfies complementary slackness: $\lambda(r) = 0$ where the constraint is slack ($a_{\text{bary}}(r) \geq a_{\text{obs}}(r)$), and $\lambda(r) > 0$ where the constraint binds ($a_{\text{bary}}(r) < a_{\text{obs}}(r)$). Standard complementary slackness determines only this zero/nonzero structure. The specific value when binding depends on the optimization's objective and constraint functions. In the simplest formulation — where the gravitational field at each radius independently minimizes discrepancy subject to the constraint that total acceleration matches the observed value — the dual variable at the fixed point takes the value:

$$\lambda(r) = \max\left(0,\; a_{\text{obs}}(r) - a_{\text{bary}}(r)\right)$$

This is a stronger claim than complementary slackness alone: it asserts that the dual variable exactly equals the local acceleration deficit. This holds in the companion notebook's schematic model (§7), where the primal variables are fixed and the dual update converges to the deficit by construction. Whether it holds in a realistic variational formulation — where the primal fields respond to the dual variable and the optimization is genuinely coupled — is the open problem of §10.3. What complementary slackness *does* guarantee, independent of the specific value, is the locality and the zero/nonzero structure. Therefore:

1. **If baryonic density increases locally at radius $r$**, then $a_{\text{bary}}(r)$ increases, the constraint deficit shrinks, and $\lambda(r)$ decreases. The "dark matter" contribution drops where baryons contribute more.

2. **If baryonic density decreases locally at radius $r$**, then $a_{\text{bary}}(r)$ decreases, the deficit grows, and $\lambda(r)$ increases. The dual variable fills the gap.

3. **The total acceleration** $a_{\text{total}}(r) = a_{\text{bary}}(r) + \lambda(r)$ therefore tracks $a_{\text{obs}}(r)$ at every radius where the constraint is active, and every feature in $a_{\text{bary}}(r)$ is mirrored — with opposite sign — in $\lambda(r)$, leaving a corresponding feature in $a_{\text{total}}(r)$.

There are no free parameters in this derivation. The local coupling between baryonic features and rotation curve features is a structural consequence of the optimization — the dual variable *must* track the baryonic distribution because it is defined by the local constraint violation against that distribution. Any framework where the "dark matter" is a dual variable of a locally-defined constraint will produce Renzo's Rule automatically.

The strength of this prediction should be emphasized. MOND also reproduces Renzo's Rule, because its modified gravity law couples directly to the baryonic mass distribution. But in MOND, this is an input — the theory is constructed to be baryonically sourced. In the Lagrangian relaxation framing, the local coupling is an *output* — it follows from complementary slackness applied to a geometric constraint, without any assumption that the dual variable should track baryonic features. It does so because it has no other option: the constraint is what it is, and the price is local.

### 4.4 When the Constraint Binds

In Lagrangian relaxation, the dual variable is nonzero only when the constraint is active (complementary slackness). The constraint becomes active — and the dual variable takes a nonzero value — whenever the drive/threshold ratio enters the critical band. In the galactic case, this happens at the low-acceleration end:

- **Mid-range acceleration (fast bow)**: kinetic friction sustained, no stick phase, no subharmonic. Gravity is Newtonian, no dark matter needed.
- **Low acceleration (slow bow)**: kinetic friction cannot be maintained, system enters stick-slip, subharmonic appears. The geometric constraint binds, the dual variable activates, "dark matter" emerges.

But complementary slackness is symmetric in the ratio. The constraint can also bind when the drive is strong enough to *overwhelm* the medium's dissipative capacity — the "pressed firmly" regime. An accretion disk around a stellar-mass black hole is a physical system where this occurs. The disk flattens under its own pressure and tidal shear; angular momentum transport is governed by the magnetorotational instability, which activates above a critical wavelength; the resulting turbulent viscosity produces stick-slip-like transitions between laminar and turbulent flow. The dual variable in this system is not dark matter — it is whatever the medium's transfer function must pay to satisfy its own geometric constraint (angular momentum conservation in a flattening geometry under extreme shear). The observable is the QPO, not the halo. But the mechanism — constraint binding, dual variable activation, subharmonic generation — is the same.

The MOND acceleration scale $a_0$ is the critical coupling of the stick-slip transition at galactic scales — the point at which spacetime geometry can no longer satisfy its geometric constraint using baryonic matter alone and must pay a dual-variable cost. Other media have their own critical couplings. The dual variable is universal; the threshold is not.

---

## 5. Predictions and Distinguishing Tests

If dark matter effects are dual variables of a constrained optimization, several predictions follow that differ from particle dark matter models:

### 5.1 Renzo's Rule — Quantitative Predictions

The theoretical derivation of Renzo's Rule from complementary slackness (§4.3) produces quantitative predictions beyond the qualitative statement that "features correlate":

1. **Feature amplitude ratio.** If $\delta a_{\text{bary}}$ is a local perturbation in baryonic acceleration at radius $r$, the corresponding perturbation in the dual variable is $\delta\lambda = -\delta a_{\text{bary}}$ wherever the constraint is active ($\lambda > 0$). The rotation curve feature amplitude should equal the baryonic feature amplitude, not merely correlate with it. This is testable: high-resolution HI rotation curves (e.g., THINGS survey, Walter et al., 2008) paired with photometric surface brightness profiles should show feature-for-feature amplitude matching in the low-acceleration regime, with the matching breaking down only where the constraint is slack (inner galaxy, high acceleration).

2. **Transition radius.** The correspondence should activate sharply at the radius where $a_{\text{bary}}(r)$ drops below $a_{\text{obs}}(r)$ — the radius where complementary slackness switches from $\lambda = 0$ to $\lambda > 0$. Interior to this radius, baryonic features appear in the rotation curve through normal Newtonian dynamics; exterior to it, they appear through the dual variable. The transition should occur at $a \approx a_0$, coinciding with the MOND transition.

3. **Asymmetry test.** A bump (local increase) in baryonic density should *reduce* the dual variable locally, while a dip should *increase* it. In both cases the rotation curve feature follows the baryonic feature. But the mechanism is asymmetric: bumps reduce $\lambda$ (the constraint relaxes), while dips increase $\lambda$ (the constraint tightens). If the relaxation has residual oscillatory structure (§5.2), dips should show slightly more scatter than bumps, because constraint-tightening updates have larger step sizes than constraint-relaxing ones in subgradient methods.

4. **Morphological independence.** Because the dual variable depends only on the local acceleration deficit, Renzo's Rule should hold identically across galaxy types — spirals, dwarfs, LSBs, irregulars — with no dependence on merger history, star formation rate, or feedback physics. This is observed (Sancisi, 2004; Lelli, McGaugh & Schombert, 2016) and is one of the most challenging facts for particle dark matter models to accommodate.

### 5.2 Mode Structure

Lagrangian relaxation converges through oscillation around the saddle point. If the dark matter halo is the spatial signature of this convergence, its radial profile should reflect the oscillation envelope — not a smooth NFW profile (Navarro, Frenk & White, 1997), but one with residual oscillatory structure at a characteristic scale set by the "step size" of the dual update.

Intriguingly, observations of galaxy rotation curves do show fine structure beyond smooth fits. Whether this structure is consistent with dual-variable oscillation (as opposed to baryonic substructure, observational noise, or other effects) is an empirical question.

### 5.3 Convergence Failures

Lagrangian relaxation can fail to converge if:
- The step size is too large (oscillation diverges)
- The constraint set is empty (no feasible solution exists)
- The objective is not concave in the relevant variables

Galaxy clusters are the regime where MOND notoriously underperforms — it predicts less dark matter than observed. In the Lagrangian relaxation framing, this could indicate a convergence failure: the optimization problem in galaxy clusters has different structure (multiple interacting constraints, loss of concavity) that prevents the single-constraint relaxation from finding the correct dual value. This would predict that galaxy cluster dark matter requires a multi-constraint formulation — consistent with the observation that cluster dynamics involve additional physics (hot gas, ram pressure, merger history) absent in isolated galaxies.

### 5.4 Strong-Field Subharmonics

If the mechanism is bidirectional, it predicts observable subharmonic signatures in strong-field systems where the drive *exceeds* the medium's dissipative threshold — not only where it falls below. Accretion disks are the sharpest test. The disk is a medium with its own transfer function: angular momentum is transported by turbulent viscosity (driven by the MRI), the disk flattens under pressure and tidal forces, and the geometry imposes conservation constraints that the medium cannot satisfy smoothly when driven too hard. The prediction: QPO frequency ratios (3:2, 2:1, 3:1) should be derivable from the disk's Stribeck-type transfer function — the ratio of orbital shear rate to MRI critical wavelength — without invoking resonance between independent oscillation modes. If the same functional form (drive/threshold ratio → subharmonic spectrum) that fits the MOND interpolating function at galactic scales also fits QPO frequency structure at accretion-disk scales, the structural claim is validated across eighteen orders of magnitude in acceleration. (In the Josephson junction, the same pendulum-equation structure — the Stewart-McCumber model is a driven pendulum, which is the canonical stick-slip oscillator — produces Shapiro steps at exact integer multiples $V_n = nhf/2e$ above the critical current $I_c$. The §3.3 structural identity with a derived rather than merely observed prediction.)

An accretion disk may be the only astrophysical system that exhibits both entry modes simultaneously: slow-drive subharmonics in the outer disk (where the dark matter problem lives) and force-driven subharmonics in the inner disk (where QPOs are observed). If both arise from the same Stribeck-type transfer function of the disk medium, that is strong evidence that the mechanism is one.

The black hole spin parameter $a^*$ provides a further test. In a prograde disk ($a^* > 0$), frame-dragging reduces the relative velocity between the disk material and the spacetime geometry; in a retrograde disk ($a^* < 0$), it increases it. The ISCO radius differs correspondingly — smaller for prograde, larger for retrograde — changing the shear rate and tidal coupling at the inner disk boundary. If QPO subharmonics arise from a Stribeck-type threshold, the spin parameter shifts where the drive/threshold ratio enters the critical band. The prediction: retrograde disks should exhibit QPO onset at different accretion rates than prograde disks of the same mass, and the subharmonic frequency structure should vary systematically with $a^*$. X-ray binaries with measured spins and QPOs (e.g., GRS 1915+105, XTE J1550-564) provide existing data against which this prediction can be checked.

### 5.5 The DAMA Modulation — A Speculative Note (Mechanism Underdeveloped)

*Note: This section raises a conjecture that is not yet adequately developed. The mechanism connecting the Gran Sasso overburden to a drive/threshold ratio in the gravitational framework is not formalized. It is included because the experimental situation is genuinely puzzling and the framing suggested here differs from the standard one, but a reviewer would be right to regard it as post-hoc accommodation rather than prediction. It should not be taken as a test of the framework until the mechanism is made explicit.*

The DAMA/LIBRA experiment at Gran Sasso has reported an annual modulation in its NaI(Tl) detector event rate for over two decades, peaking in June and reaching a minimum in December. The conventional interpretation is particle dark matter: Earth's orbital velocity adds to the Sun's galactic velocity in June (~30 km/s faster through the halo) and subtracts in December, producing more particle scattering at peak velocity. The modulation is statistically robust. The interpretation is what is contested.

The particle interpretation makes a specific prediction: the modulation should be site-independent. Any sufficiently sensitive NaI detector, anywhere on Earth, should observe the same annual cycle, because the dark matter wind is galactic-scale and the detector material is the same. This prediction has failed. ANAIS-112 (Canfranc, Spain), using NaI(Tl) crystals with comparable sensitivity, found no modulation in a reanalysis of three years of data (Coarasa et al., 2024). COSINE-100 (Yangyang, South Korea) found no statistically significant modulation over its full operational period (October 2016–March 2023). A 2025 joint analysis combining COSINE-100 and ANAIS-112 data across six years of overlap (984 kg·yr total exposure) excludes the DAMA/LIBRA annual modulation signal at **5.3σ** significance (COSINE-100 + ANAIS-112 Collaborations, 2025). The signal appears to be specific to Gran Sasso.

One could conjecture that the medium-dependent threshold interpretation of this framework is relevant: if a detector responds to some local constraint-binding oscillation rather than particle collisions, the threshold might depend on the local environment — overburden, muon flux, rock composition. That conjecture would predict site-dependence of any modulation signal.

**The gap:** this framework has no formalized account of what the gradient normalization constraint ($g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi = 1$) implies for a terrestrial laboratory detector embedded in 1.4 km of dolomite. The chain from galactic-scale dual variable to crystal-level event rate has not been constructed. Without that chain, the "medium-dependent threshold" language is suggestive but not predictive. The experimental situation (ANAIS/COSINE non-replication, SABRE South pending) is interesting; this framework does not yet have the machinery to claim it as a test.

SABRE South, currently being installed 1 km underground in the Stawell Gold Mine outside Melbourne, will provide additional data. Whether this framework will have anything precise to say about the result depends on closing the mechanism gap described above.

### 5.6 The Nodal Geometry of 3:2 — An Embedding the Paper Nearly Misses

The paper's treatment of QPOs (§2.3, §5.4) identifies 3:2, 2:1, and 3:1 as subharmonic signatures of the disk's Stribeck transfer function. What it does not do — and what the string analogy makes available — is explain why 3:2 specifically is so robust across systems spanning orders of magnitude in mass.

Return to the string. The $n$-th harmonic has $n-1$ interior nodes, equally spaced at positions $k/n$ along the string for $k = 1, \ldots, n-1$. The second harmonic has a single node at $1/2$. The third harmonic has nodes at $1/3$ and $2/3$. These are not abstract frequency labels — they are **spatial locations** on the medium where the geometry enforces a zero crossing.

A violinist produces a natural harmonic by lightly touching the string at a node while bowing elsewhere — the "touch harmonic" or flageolet tone. Touching at $1/3$ (or equivalently $2/3$) selects the third harmonic; touching at $1/2$ selects the second. The ratio of their frequencies is $3:2$. But the deeper point is that these are the only node positions that are *simultaneously* nodes of one low harmonic and *antinodes* of the adjacent one. The $1/3$ and $2/3$ positions are antinodes of the second harmonic (the second harmonic has maximum displacement there) and nodes of the third. This geometric collision — where one mode's maximum displacement coincides with another mode's zero — creates the strongest possible coupling between adjacent harmonics. The 3:2 ratio is not selected dynamically; it is **selected geometrically**, by the nodal structure of the medium itself.

Bowing *on* a node suppresses the harmonic whose node falls there. This is the complementary operation: placing the drive at the zero crossing of a mode prevents that mode from being excited. The Helmholtz motion of a normally bowed string implicitly avoids nodes of the fundamental, but in the subharmonic regime — where the bow is too slow or too heavy — the slip phase lands on positions that are nodes of the fundamental and antinodes of the subharmonic. The stick-slip waveform, far from being a featureless alternation, is geometrically structured by the nodal pattern of the medium.

The connection to QPOs is then this: an accretion disk is a medium with radial mode structure. The $n$-th radial mode has $n-1$ nodal radii. If the disk's Stribeck-type transfer function produces subharmonic mode-locking, the locked frequencies should reflect the nodal geometry of the disk, not arbitrary resonance ratios. The 3:2 ratio is universal across black hole masses because the *nodal geometry* is scale-free — node positions at $1/3$ and $2/3$ of the relevant radial extent are dimensionless fractions, independent of the physical size of the medium. The mass-independence that makes 3:2 QPOs "embarrassing" for resonance models is exactly what the nodal geometry predicts: the ratio is set by where the zeros fall, not by how big the drum is.

This is the embedding the paper's current framework nearly misses. The stick-slip mechanism explains *that* subharmonics appear; the Stribeck transfer function explains *when*; but the nodal geometry of the medium explains *which* — why 3:2 rather than 5:3 or 7:4. The geometry that produces the ratio is special, and that geometry is scale-free. A scale-free mechanism immediately explains the mass-independence without additional assumptions.

### 5.7 No Direct Detection

If dark matter is a dual variable rather than a primal variable (a substance), direct detection experiments should find nothing. The dual variable has physical effects (it modifies the gravitational field) but is not a particle that carries energy-momentum independently of the constraint it enforces. This is consistent with the null results from XENON, LUX, PandaX, and other direct detection experiments through 2026.

### 5.8 The Bullet Cluster

The Bullet Cluster (1E 0657-56) is often cited as evidence for particle dark matter, since the gravitational lensing signal is offset from the visible baryonic matter (hot gas). In the dual-variable framing, this requires that the constraint (and therefore its multiplier) can decouple from the baryonic distribution during violent non-equilibrium events (cluster mergers). This is plausible if the constraint is geometric (tied to the metric) rather than material (tied to the matter distribution) — the metric need not track the gas during a rapid merger. However, this prediction needs quantitative development to be compelling.

---

## 6. The Three-Body Caveat

We note, with appropriate humility, that the classical three-body problem already demonstrates the limits of our dynamical fidelity with observable matter. If three gravitationally interacting bodies cannot be solved in closed form, the claim that dark matter anomalies in systems of $10^{11}$ bodies must require new matter (rather than new mathematics) deserves scrutiny. The n-body problem is not merely hard — it is formally chaotic, with exponential sensitivity to initial conditions. The gap between "Newtonian prediction" and "observed dynamics" in galactic systems includes an unknown contribution from computational intractability, not just missing mass.

This does not prove that dark matter is mathematical rather than material. But it shifts the burden of proof: before asserting that a discrepancy requires new matter, one must establish that the discrepancy exceeds what computational intractability alone could produce. The Lagrangian relaxation framing suggests a specific mathematical structure for that excess. Whether the structure fits is an empirical question.

---

## 7. Computational Demonstration

We provide a companion Jupyter notebook (`stick_slip_lagrangian.ipynb`) that demonstrates the core mechanism schematically. The notebook:

1. **Implements a stick-slip oscillator** with parameterized velocity, coupling, damping, and threshold — showing subharmonic generation in the slow-velocity regime
2. **Maps the oscillator onto a parameterized gravitational model**, where the "budget constraint" is the baryonic mass and the "gain function" is the gravitational binding energy
3. **Iterates a dual-variable update rule** inspired by the Lagrangian relaxation subgradient step, showing the dual variable (dark matter analogue) converging to the local acceleration deficit at each radius
4. **Demonstrates the MOND-like transition**: the dual variable is zero when the constraint is slack (high acceleration / sufficient baryonic mass) and grows when the constraint binds (low acceleration / insufficient baryonic mass)
5. **Shows convergence and divergence regimes** by varying the step size, corresponding schematically to stable galaxy rotation curves and unstable cluster dynamics

**Scope and limitations.** The notebook is a schematic demonstration, not a derivation from first principles. The "Lagrangian relaxation" it implements is a simplified dual-variable iteration: the primal variables (baryonic masses) are held fixed, each radial shell is independent, and the dual update converges to `max(0, a_obs - a_bary)` by construction. There is no inner optimization step over primal variables, no coupling between shells, and no non-smooth objective function — features that would be present in a genuine Lagrangian relaxation of a gravitational action. The convergence behavior shown (damped oscillation for small step sizes, divergence for large ones) is generic to first-order linear iterations and does not require the Lagrangian relaxation interpretation. The notebook demonstrates that the *output* of the framework (threshold-dependent dual variable, complementary slackness structure) is consistent with galactic phenomenology. The gap between this schematic and a genuine Lagrangian relaxation of a realistic gravitational potential is the open problem of §10.3.

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

1. The identification of the MOND interpolating function with the velocity-weakening branch of the Stribeck friction curve (as a regime-level correspondence, not a functional identity)
2. The interpretation of mimetic gravity's Lagrange multiplier as an optimization-theoretic shadow price
3. The application of Lagrangian relaxation (the optimization technique) to gravitational field dynamics
4. The use of stick-slip relaxation oscillation as a dynamical model for the MOND transition
5. The derivation of Renzo's Rule (baryonic-rotation curve feature coupling) as a theorem of local complementary slackness, rather than a correlation requiring explanation
6. The prediction that galaxy cluster MOND failures correspond to Lagrangian relaxation convergence failures
7. The identification of the dark matter problem as an adiabatic-limit phenomenon favoring resonant over high-energy detection
8. The structural correspondence between the clockwork mechanism and stick-slip period doubling
9. The generalization from a monodirectional threshold ($a < a_0$) to a medium-dependent drive/threshold ratio, unifying galactic dark matter with accretion disk QPOs and atmospheric scattering under one mechanism
10. The reinterpretation of the DAMA/LIBRA annual modulation as a drive oscillation through a medium-dependent critical band, predicting site-dependent (not site-independent) modulation — consistent with the non-replication by ANAIS-112 and COSINE-100

---

## 9. Experimental Implications: Resonant Detectors, Not Colliders

*This section incorporates observations contributed by Gemini (Google DeepMind) and DeepSeek during collaborative review. The adiabatic limit framing and resonant detection strategy were identified by Gemini. The QPO prediction and accretion disk as test case were identified by DeepSeek; the numerical falsification of $a_0$ as the QPO threshold and the subsequent generalization to medium-dependent thresholds (§2.2–2.3) were developed in response.*

### 9.1 The Adiabatic Limit

The stick-slip framing identifies a specific regime: the subharmonic emerges when the drive/threshold ratio enters a critical band. There are two ways to enter — decrease the drive below the medium's threshold (slow bow) or increase the drive until it overwhelms the medium's dissipative capacity (pressed firmly). Both produce subharmonics; which mode dominates depends on the medium.

For the galactic dark matter problem, the entry is from below: cosmic expansion is slow, galactic accelerations are small, the gravitational field enters the stick-slip band through patience. For accretion disks, the entry is from above: tidal shear and magnetic pressure exceed the disk's capacity to transport angular momentum smoothly, and the system mode-locks into QPO subharmonics. The mechanism is one; the direction of entry is medium-dependent.

This has a direct experimental consequence. A collider does not fail because force is the wrong approach in general — force-driven subharmonics are real (§2.3, §5.4). A collider fails because it is not tuned to *any* medium's critical band for the gravitational subharmonic. It operates at the electroweak scale, which is neither the slow regime (galactic, $a_0 \sim 10^{-10}$ m/s²) nor the force-driven regime (accretion disk, MRI threshold). It is simply off-resonance. You need a detector tuned to a regime where the drive/threshold ratio actually enters the critical band.

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

## 10. Open Questions

The following are unresolved. They are listed not as weaknesses to be explained away but as the specific problems whose resolution would determine whether this framework is correct, incomplete, or wrong.

### 10.1 Does It Scale to Cosmology?

The paper operates at galaxy and cluster scales. Particle CDM earns its strongest results at cosmological scales — the CMB acoustic peaks, baryon acoustic oscillations, and the matter power spectrum. These are not qualitative trends; they are quantitative precision measurements that ΛCDM reproduces to sub-percent accuracy. Any viable dark matter framework must either reproduce them or explain why it is exempt.

The honest position is: **we don't know.** This framework has not been applied at cosmological scales, and the shadow price / convergence trajectory language has not been developed there at all. A referee will ask this immediately, and there is no good answer yet.

What can be said: mimetic gravity's Lagrange multiplier does admit cosmological solutions. Sebastiani et al. (2017) and Nojiri & Odintsov (2014) show the formalism can produce inflation, dark energy, and bounce cosmologies. So the raw field equations are not incompatible with cosmological dynamics. But "the formalism is not ruled out" is not the same as "the framework predicts the right CMB peak positions" — and that gap has not been closed. The optimization-theoretic interpretation adds further structure (shadow prices, dual convergence, complementary slackness) that has no developed cosmological counterpart.

This is a more serious gap than the section heading implies. CMB acoustic peaks, BAO, and the matter power spectrum are the strongest tests of CDM precisely because they are computed from first principles with no free parameters adjusted to fit galactic observations. Until the dual-variable framework can reproduce these — or until a principled argument exists for why it operates differently at cosmological scales — it should be understood as a framework for galactic-scale phenomenology, not as a complete alternative to ΛCDM. That is a limitation worth stating plainly rather than softening.

### 10.2 Can the Dual Variable Decouple Spatially?

The Bullet Cluster requires the gravitational lensing signal (the "dark matter") to be spatially offset from the baryonic gas after a cluster merger. The qualitative argument (§5.7) — that a geometric constraint tracks the metric, not the gas — is plausible but unmodeled. Collisionless particle dark matter explains the offset naturally: particles pass through each other while gas shocks and decelerates. The dual-variable interpretation needs a simulation showing that the constraint's spatial profile evolves independently of the baryonic distribution during a violent non-equilibrium event. Until that simulation exists, the Bullet Cluster remains the strongest single objection to any non-particle dark matter framework.

### 10.3 From Schematic to Quantitative

The companion notebook demonstrates the mechanism schematically — threshold produces subharmonic, a dual-variable iteration converges or diverges — but on a simplified model where the primal variables are fixed and each radius is independent. This is not Lagrangian relaxation in the full sense: there is no inner optimization, no coupling between radial shells, and the dual variable converges to the known deficit by construction. The gap between this schematic and a theory is threefold: (1) choosing a specific geometric constraint (what is the gravitational field optimizing against?); (2) formulating the genuine dual problem with coupled primal-dual dynamics, verifying that strong duality holds (Ekeland & Temam, 1976) and that the shadow price interpretation is rigorous; and (3) solving the coupled problem on observed baryonic mass profiles to produce predicted rotation curves without free parameters beyond the constraint specification. Until step (2) is complete, the "shadow price" interpretation remains an interpretive lens rather than a proven duality result.

### 10.4 Does the Stribeck Transfer Function Generalize to Non-Gravitational Media?

The atmospheric optics case (§10 conclusion, [stribeck-optics](https://github.com/nickjoven/stribeck-optics)) is the most direct non-gravitational test. Point-source headlights in fog produce halos — subharmonic artifacts of the scattering medium's transfer function. The hypothesis: the halo structure is determined by the ratio of the source's spatial frequency content to the medium's critical scattering threshold (mean free path × coherence length), and shaping the emitted beam to avoid the critical band should suppress halo formation. This is experimentally accessible: a structured-illumination headlight, a fog chamber, and a camera. If the Stribeck framework predicts the halo's spatial frequency content from the medium's measured scattering parameters, the generalization holds. If it doesn't, the framework may be specific to gravity and the structural analogy is just an analogy.

### 10.5 The Square Wave as Bifurcation Limit

The idealized stick-slip waveform is a square wave: instantaneous alternation between two states (stuck, slipping) with no transition time. The Fourier series of a square wave contains only odd harmonics — $f$, $3f$, $5f$, $7f$, $\ldots$ — with amplitudes decaying as $1/n$. This is not an arbitrary waveform; it is the waveform that maximally excludes even harmonics while maintaining periodicity.

The question is whether the square wave state is approachable *bifurcationally* — through the period-doubling cascade — rather than requiring instantaneous switching. The Feigenbaum cascade (Notebook 06) produces progressively sharper transitions between states as the drive parameter increases past successive bifurcation points. At each period-doubling, the system's trajectory develops a new crease — a region of rapid transition that becomes sharper as the cascade continues. In the limit, the accumulation point of the cascade produces a trajectory with infinitely many creases: a function that is everywhere continuous but nowhere smooth, transitioning instantaneously between states. This limiting waveform is not chaotic — it sits precisely *at* the edge of chaos — and its spectral content is structured: odd harmonics dominate because the underlying symmetry of period doubling preserves the half-period antisymmetry that excludes even harmonics.

This connects two things the paper treats separately. The subharmonic (§1) is the period-2 state — the first bifurcation, the simplest stick-slip. The Feigenbaum cascade (Notebook 06) is the route to chaos through successive period-doublings. The square wave sits at the *end* of the cascade's regular regime: it is the sharpest possible stick-slip waveform, the state where transitions are instantaneous and the system spends all its time in one of two discrete states. If the gravitational stick-slip is not merely period-2 but is approachable from a cascade — if the dark matter phenomenon represents a system that has undergone not just one bifurcation but has cascaded toward the square-wave limit — then the spectral content of the "dark matter halo" should contain the odd-harmonic signature: modes at $3f$, $5f$, $7f$ relative to the fundamental, with the specific $1/n$ amplitude decay of the square wave's Fourier series.

The companion notebook (`08_square_wave_bifurcation.ipynb`) explores this numerically: building the square wave as the limit of the bifurcation cascade, showing that the odd-harmonic spectrum emerges from the cascade's symmetry rather than from the specific nonlinear map, and asking whether the gravitational Stribeck curve is in a regime where the square-wave limit is the attractor rather than the simple period-2 state.

### 10.6 Laboratory Validation

Kawano et al. (2025) have taken the first step: high-speed imaging and finite element simulation confirming that both slow velocity and increased pressure produce subharmonics in bowed strings. What remains is the full phase-space characterization — mapping the hysteresis loop, measuring the energy partition between fundamental and subharmonic as a function of bow velocity and pressure jointly, and extracting the empirical Stribeck curve against which the gravitational analogue is calibrated. The prediction is specific: the subharmonic onset region in the velocity-pressure phase diagram should be a narrow diagonal band, entry should be possible from both sides, and the energy partition should follow the complementary slackness structure (subharmonic energy nonzero only when the drive/threshold ratio is in the critical band). This experiment extends Kawano et al.'s setup with a calibrated force sensor to measure bow pressure continuously during subharmonic generation.

---

## 11. Conclusion

The cost of this hypothesis is low. It requires no new particles, no new forces, no modifications to general relativity at the level of the action, and no changes to the topology of spacetime. The manifold structure, causal structure, and light cone structure of GR are preserved exactly. What changes is only the cost function: the gravitational field pays a dual-variable price to maintain geometric consistency where baryonic matter alone is insufficient. The framework requires only that we read an existing mathematical structure (mimetic gravity's Lagrange multiplier) through an existing mathematical framework (Lagrangian relaxation) motivated by an existing physical phenomenon (stick-slip dynamics).

If the framing is correct, it narrows the search space in three ways. Theoretically, the dark matter problem becomes a question about which geometric constraint the gravitational field is optimizing against, and the acceleration scale $a_0$ is the critical coupling at galactic scales — one instance of a medium-dependent threshold. Observationally, the framework's sharpest near-term test is Renzo's Rule: because the shadow price is local, the dual variable at each radius is determined by the local baryonic acceleration deficit, and every feature in the baryonic light curve must be mirrored in the rotation curve — not as a correlation to be fitted, but as a theorem of complementary slackness. High-resolution surveys (THINGS, SPARC) already contain the data; the prediction is feature-for-feature amplitude matching in the low-acceleration regime, with no free parameters. Experimentally, it redirects detection strategy from off-resonance instruments (colliders at the electroweak scale) to on-resonance ones — slow detectors (atom interferometers, clock networks, mid-band gravitational wave detectors) for the galactic subharmonic, and X-ray timing for accretion disk subharmonics.

The structure generalizes. Any system where a signal propagates through a medium — and the medium's transfer function has a critical threshold at which it mode-converts the input into subharmonic artifacts — is a candidate for the same analysis. The threshold can be entered from either direction: drive too slow (galaxies) or drive too hard (inner accretion disks). The accretion disk is the strongest test case because it enters from both sides simultaneously, and the observables (rotation curves in the outer disk, QPO frequency ratios in the inner disk) are already measured. Atmospheric optics is another such system; the halos produced by point-source headlights in fog are, structurally, the optical analogue of the dark matter halo. Whether this generalization is productive beyond the gravitational case remains to be seen.

If the framing is wrong, it has consumed one short paper and a notebook. The asymmetry favors exploration.

The thread began with a bowed string producing a tone one octave below its fundamental. For the galaxy, the subharmonic emerges through patience — the slow-drive end of the phase diagram, where low acceleration falls below the critical threshold. For the accretion disk, it emerges through force — the high-drive end, where tidal shear overwhelms dissipative capacity. The mechanism is agnostic about direction. Both cases produce the same mathematical object: a dual variable, a shadow price, a constraint that binds. The dark sector may not be something exotic above the Standard Model or something subtle below it. It may be the price any medium pays when its drive/threshold ratio enters the band where smooth dynamics are no longer available.

---

## References

- Abe, M. et al. (MAGIS-100 Collaboration) (2021). Matter-wave Atomic Gradiometer Interferometric Sensor (MAGIS-100). *Quantum Sci. Technol.*, 6, 044003. arXiv:2104.02835.
- Badurina, L. et al. (2020). AION: An Atom Interferometer Observatory and Network. *JCAP*, 05, 011. arXiv:1911.11755.
- Bekenstein, J. D. (2004). Relativistic gravitation theory for the modified Newtonian dynamics paradigm. *Phys. Rev. D*, 70(8), 083509.
- Berezhiani, L., & Khoury, J. (2015). Theory of dark matter superfluidity. *Phys. Rev. D*, 92(10), 103510.
- Brace, W. F., & Byerlee, J. D. (1966). Stick-slip as a mechanism for earthquakes. *Science*, 153(3739), 990-992.
- Bernabei, R. et al. (DAMA/LIBRA Collaboration) (2018). First model independent results from DAMA/LIBRA-phase2. *Nucl. Phys. At. Energy*, 19(4), 307-325. arXiv:1805.10486.
- Capozziello, S., Matsumoto, J., Nojiri, S., & Odintsov, S. D. (2010). Dark energy from modified gravity with Lagrange multipliers. arXiv:1004.3691v2.
- Chaichian, M., Klusoň, J., Oksanen, M., & Tureanu, A. (2014). Mimetic dark matter, ghost instability and a mimetic tensor-vector-scalar gravity. *JHEP*, 2014(12), 102. arXiv:1404.4008.
- Chamseddine, A. H., & Mukhanov, V. (2013). Mimetic dark matter. *JHEP*, 2013(11), 135.
- Chamseddine, A. H., & Mukhanov, V. (2014). Cosmology with mimetic matter. *JCAP*, 2014(6), 017. arXiv:1403.3961.
- Coarasa, I. et al. (ANAIS-112 Collaboration) (2024). ANAIS-112 three years data: a sensitive model independent negative test of the DAMA/LIBRA dark matter signal. *Commun. Phys.*, 7, 345. arXiv:2311.03392.
- COSINE-100 and ANAIS-112 Collaborations (2025). Combined annual modulation dark matter search with COSINE-100 and ANAIS-112. arXiv:2503.19559.
- Ekeland, I., & Temam, R. (1976). *Convex Analysis and Variational Problems*. North-Holland.
- Derevianko, A., & Pospelov, M. (2014). Hunting for topological dark matter with atomic clocks. *Nature Physics*, 10, 933-936. arXiv:1311.1244.
- Fisher, M. L. (1981). The Lagrangian relaxation method for solving integer programming problems. *Management Science*, 27(1), 1-18.
- Giudice, G. F., & McCullough, M. (2017). A Clockwork Theory. *JHEP*, 02, 036. arXiv:1610.07962.
- Held, M., & Karp, R. M. (1971). The traveling-salesman problem and minimum spanning trees: Part II. *Math. Programming*, 1(1), 6-25.
- Joven, N. (2026). A content-addressed adaptive knowledge substrate for distributed epistemic coordination. *Preprint*.
- Kawano, S., Kobayashi, K., Suzuki, T., & Ichiji, N. (2025). Experimental Validation of String Oscillation in Subharmonic Generation. arXiv:2502.11902.
- McGaugh, S. S., Lelli, F., & Schombert, J. M. (2016). Radial acceleration relation in rotationally supported galaxies. *Phys. Rev. Lett.*, 117(20), 201101.
- Milgrom, M. (1983). A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis. *ApJ*, 270, 365-370.
- Navarro, J. F., Frenk, C. S., & White, S. D. M. (1997). A universal density profile from hierarchical clustering. *ApJ*, 490(2), 493-508.
- Nojiri, S., & Odintsov, S. D. (2014). Mimetic F(R) gravity: inflation, dark energy and bounce. *Mod. Phys. Lett. A*, 29(40), 1450211. arXiv:1408.3561.
- Lelli, F., McGaugh, S. S., & Schombert, J. M. (2016). SPARC: Mass models for 175 disk galaxies with Spitzer photometry and accurate rotation curves. *AJ*, 152(6), 157. arXiv:1606.09251.
- Roberts, B. M. et al. (2017). Search for domain wall dark matter with atomic clocks on board global positioning system satellites. *Nature Communications*, 8, 1195. arXiv:1704.06844.
- Sancisi, R. (2004). The visible matter – dark matter coupling. *IAU Symposium*, 220, 233-240. arXiv:astro-ph/0311348.
- Walter, F. et al. (2008). THINGS: The HI Nearby Galaxy Survey. *AJ*, 136(6), 2563-2647. arXiv:0810.2125.
- Sebastiani, L., Vagnozzi, S., & Myrzakulov, R. (2017). Mimetic gravity: a review of recent developments and applications to cosmology and astrophysics. *Advances in High Energy Physics*, 2017.
- Sussman, G. J., & Wisdom, J. (1992). Chaotic evolution of the solar system. *Science*, 257(5066), 56-62.
- Verlinde, E. (2016). Emergent gravity and the dark universe. *SciPost Phys.*, 2(3), 016.
- Wolfram, S. (2002). *A New Kind of Science*. Wolfram Media.

---

*Companion notebook: `stick_slip_lagrangian.ipynb`*
*This paper is released under CC0.*
