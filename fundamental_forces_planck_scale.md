# Fundamental Forces at Planck Scale — Harmonic Connections

**N. Joven**
ORCID: 0009-0008-0679-0812
March 2026. CC0.

**Abstract.** The stick-slip / Stribeck / Lagrangian-relaxation framework developed in the companion paper (Joven, 2026, "Stick-Slip Dynamics and the Dark Matter Dual") operates at galactic scales. This note asks: do the strong and weak nuclear forces, or Planck-scale physics, exhibit mathematical structures that align with the framework's harmonics? We identify several connections — some rigorously established, others conjectural — and separate them accordingly. Part I presents established mathematics with published references. Part III presents pure speculation.

---

## Part I — Established Mathematics

### 1. QCD Running Coupling as a Stribeck Curve

The 1-loop QCD running coupling at momentum transfer $Q$ with $n_f$ active quark flavors is

$$\alpha_s(Q^2) = \frac{12\pi}{(33 - 2n_f) \ln(Q^2/\Lambda^2_{\text{QCD}})}$$

where $\Lambda_{\text{QCD}} \approx 200$ MeV is the QCD scale parameter (Gross & Wilczek, 1973; Politzer, 1973). This function:

- Diverges as $Q^2 \to \Lambda^2_{\text{QCD}}$ (strong coupling / confinement)
- Decays as $1/\ln Q^2$ for $Q^2 \gg \Lambda^2$ (weak coupling / asymptotic freedom)
- Interpolates smoothly between the two regimes with a single characteristic scale $\Lambda_{\text{QCD}}$

The Stribeck friction curve (Stribeck, 1902) is

$$\mu(v) = \mu_k + (\mu_s - \mu_k) \exp\left(-(v/v_{\text{th}})^2\right)$$

This function:

- Approaches $\mu_s$ as $v \to 0$ (strong coupling / static friction)
- Approaches $\mu_k$ as $v \to \infty$ (weak coupling / kinetic friction)
- Interpolates smoothly between the two regimes with a single characteristic scale $v_{\text{th}}$

Both are members of the class of smooth, monotone transfer functions with a single inflection point separating two asymptotic regimes. The companion notebook `10_qcd_stribeck_comparison.ipynb` fits the Stribeck functional form to $\alpha_s(Q^2)$ and computes residuals. The question is not whether the curves are "similar" — it is whether they belong to the same universality class of monotone threshold-mediated transfer functions.

The structural correspondence:

| Stribeck curve | QCD running coupling |
|---|---|
| $\mu_s$ (static friction, strong coupling) | Confinement regime ($Q \to \Lambda$) |
| $\mu_k$ (kinetic friction, weak coupling) | Asymptotic freedom ($Q \to \infty$) |
| $v_{\text{th}}$ (velocity threshold) | $\Lambda_{\text{QCD}}$ (energy threshold) |
| Below threshold: excess coupling | Below threshold: confinement |
| Above threshold: smooth flow | Above threshold: perturbative QCD |

**What this establishes:** The mathematical shape is shared. Both functions solve the same qualitative problem: smooth interpolation between strong and weak coupling separated by a single characteristic scale.

**What this does not establish:** That the shared shape implies a shared mechanism. The Stribeck curve is phenomenological; $\alpha_s$ derives from the QCD beta function via renormalization group flow.

**References:**
- Gross, D. J. & Wilczek, F. (1973). Ultraviolet behavior of non-abelian gauge theories. *Phys. Rev. Lett.*, 30, 1343.
- Politzer, H. D. (1973). Reliable perturbative results for strong interactions? *Phys. Rev. Lett.*, 30, 1346.
- Particle Data Group (2024). Review of Particle Physics: QCD. *Phys. Rev. D*, 110, 030001.
- Stribeck, R. (1902). Die wesentlichen Eigenschaften der Gleit- und Rollenlager. *Z. Ver. Dtsch. Ing.*, 46, 1341.

---

### 2. Flux Tube Breaking as Stick-Slip

QCD confinement produces a linear potential between separated quarks:

$$V(r) = \sigma r$$

where $\sigma \approx 1$ GeV/fm $\approx 0.18$ GeV$^2$ is the QCD string tension (Wilson, 1974; Bali, 2001). As quarks separate, energy accumulates linearly in the chromoelectric flux tube until the stored energy exceeds the pair-production threshold $2m_q$. The tube then snaps, producing a quark-antiquark pair. The process repeats iteratively during jet fragmentation.

This is mechanically identical to stick-slip oscillation in a bowed string:

| Bowed string | QCD flux tube |
|---|---|
| Elastic energy $E = \frac{1}{2}kx^2$ in rosin layer | Chromoelectric energy $V(r) = \sigma r$ in tube |
| Threshold: static friction force exceeded | Threshold: pair-production energy $2m_q$ reached |
| Release: bow slips, energy converts to kinetic | Release: tube snaps, energy converts to hadron pair |
| Cycle repeats at frequency $f$ | Cycle repeats during jet fragmentation |
| Subharmonic artifacts below threshold | Hadron spectrum below free-quark scale |

The energy-accumulation-threshold-release cycle is the same mathematical structure in both systems. The difference is the force law: quadratic elastic ($\frac{1}{2}kx^2$) for the bowed string versus linear confinement ($\sigma r$) for QCD. Both have the property that energy is stored continuously until a threshold is crossed discontinuously.

In the language of the stick-slip framework: the flux tube is in a permanent "stick" phase (quarks cannot separate), with "slip" events (pair production) as the mechanism by which the system relaxes. The hadron mass spectrum — bound states at energy scales the free quark theory does not predict — is the subharmonic artifact of confinement, analogous to the dark matter halo being the subharmonic artifact of the gravitational stick-slip transition.

**References:**
- Wilson, K. G. (1974). Confinement of quarks. *Phys. Rev. D*, 10, 2445.
- Bali, G. S. (2001). QCD forces and heavy quark bound states. *Phys. Rep.*, 343, 1.
- Casher, A., Kogut, J. & Susskind, L. (1974). Vacuum polarization and the absence of free quarks. *Phys. Rev. D*, 10, 732.
- Helmholtz, H. von (1863). *Die Lehre von den Tonempfindungen als physiologische Grundlage für die Theorie der Musik*. Vieweg.

---

### 3. Quadratic Maximum and Period Doubling

Feigenbaum's universality theorem (Feigenbaum, 1978, 1979): for any smooth unimodal map $f$ with a quadratic maximum ($f''(x_{\max}) \neq 0$), the period-doubling cascade converges with ratio

$$\delta = \lim_{n \to \infty} \frac{r_n - r_{n-1}}{r_{n+1} - r_n} = 4.66920\ldots$$

This constant is universal — it depends only on the order of the maximum, not on the specific map.

**The question:** Is quadratic scaling an inversion of period doubling?

**Answer:** No. The quadratic maximum is the *prerequisite* that determines the universality class. Period doubling is the *consequence* — the dynamical cascade that occurs within maps of that class. They are not inverse operations. One is a geometric property of the map ($f \sim f_{\max} - a(x - x_{\max})^2$ near the peak); the other is a dynamical phenomenon the geometry produces ($f \to f/2 \to f/4 \to \ldots$).

Maps with higher-order maxima (cubic: $f \sim x^3$, quartic: $f \sim x^4$) give different Feigenbaum constants:

| Maximum order $z$ | Feigenbaum $\delta_z$ |
|---|---|
| 2 (quadratic) | 4.6692... |
| 4 (quartic) | 7.2846... |
| 6 (sextic) | 9.2962... |

(Strogatz, 2015, Table 10.1.)

**Verification for the gravitational Stribeck curve:** The MOND interpolating function $\mu(x) = x/(1+x)$ has

$$\mu'(x) = \frac{1}{(1+x)^2}, \quad \mu''(x) = \frac{-2}{(1+x)^3}$$

At the transition $x = a/a_0 = 1$: $\mu''(1) = -2/8 = -1/4 \neq 0$. The maximum of the composite map formed from the Stribeck curve is quadratic. This guarantees the gravitational cascade belongs to the $\delta = 4.669$ universality class, as computed in `cvt/notebooks/06_feigenbaum_cascade.ipynb`.

**Connection to QCD:** The QCD beta function at 1-loop is $\beta(\alpha_s) = -\frac{\beta_0}{2\pi}\alpha_s^2$ where $\beta_0 = 11 - \frac{2}{3}n_f$. This has a quadratic zero at $\alpha_s = 0$ (the UV fixed point). In the variable $g^2 = \alpha_s$, the beta function's behavior near the fixed point is quadratic. If QCD dynamics near the deconfinement transition can be mapped to a unimodal iteration with this quadratic structure, it belongs to the same Feigenbaum universality class as the gravitational cascade. The constant $\delta = 4.669$ would govern the spacing of any period-doubling thresholds.

**References:**
- Feigenbaum, M. J. (1978). Quantitative universality for a class of nonlinear transformations. *J. Stat. Phys.*, 19, 25.
- Feigenbaum, M. J. (1979). The universal metric properties of nonlinear transformations. *J. Stat. Phys.*, 21, 669.
- Strogatz, S. H. (2015). *Nonlinear Dynamics and Chaos*, 2nd ed. Westview Press.
- Milgrom, M. (1983). A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis. *ApJ*, 270, 365.

---

### 4. Clockwork Chain Lengths — Multiple Thresholds from Planck Scale

The clockwork mechanism (Giudice & McCullough, 2017) produces an exponential hierarchy: a chain of $N$ fields with nearest-neighbor interactions yields a lightest mode with coupling suppressed by $q^N$ relative to the UV scale, where $q$ is the gear ratio.

The stick-slip paper's §9.3 (now removed in revision; the argument is preserved here) applies this to explain why $a_0 \approx 1.2 \times 10^{-10}$ m/s$^2$ is so far below the Planck scale. The same mechanism can be applied to any threshold. The question: if multiple thresholds (gravitational $a_0$, QCD $\Lambda_{\text{QCD}}$) all arise from clockwork suppression of a Planck-scale coupling, do the chain lengths reveal structure?

**Known scales:**

| Threshold | Energy | $\log_{10}(M_{\text{Planck}}/\text{scale})$ |
|---|---|---|
| $M_{\text{Planck}}$ | $1.22 \times 10^{19}$ GeV | 0 |
| $\Lambda_{\text{QCD}}$ | $0.2$ GeV | 19.79 |
| $v_{\text{EW}}$ (Higgs VEV) | $246$ GeV | 16.70 |
| $a_0$ (natural units: $a_0/c^2$) | $\sim 10^{-28}$ m$^{-1}$ $\sim 10^{-47}$ GeV | 65.9 |

For gear ratio $q$, the required chain length is $N = \log_{10}(M_{\text{Planck}}/\text{scale}) / \log_{10}(q)$.

The companion notebook computes these exactly for $q \in \{2, 3, 5, 7\}$ and checks the ratios $N_{\text{QCD}}/N_{\text{MOND}}$, $N_{\text{EW}}/N_{\text{QCD}}$, and their differences for integer or simple-fraction relationships. This is arithmetic — the result either reveals structure or it doesn't.

**References:**
- Giudice, G. F. & McCullough, M. (2017). A clockwork theory. *JHEP*, 02, 036.
- Choi, K. & Im, S. H. (2016). Realizing the relaxion from multiple axions and its UV completion with high scale supersymmetry. *JHEP*, 01, 149.
- Kaplan, D. E. & Rattazzi, R. (2016). Large field excursions and cosmological attractors. *Phys. Rev. D*, 93, 085007.

---

### 5. Field Equations as Constrained Optimization

The Einstein field equations follow from extremizing the Einstein-Hilbert action

$$S_{\text{EH}} = \frac{1}{16\pi G} \int R \sqrt{-g} \, d^4x$$

subject to the constraint that $g_{\mu\nu}$ is a Lorentzian metric (Hilbert, 1915). The field equations are the Euler-Lagrange equations of this constrained optimization. Dark matter, in the mimetic gravity formulation (Chamseddine & Mukhanov, 2013), arises from adding an additional constraint $g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi = 1$ whose Lagrange multiplier contributes a dust-like energy-momentum tensor.

The Yang-Mills field equations

$$\partial_\mu F^{a,\mu\nu} + g f^{abc} A^b_\mu F^{c,\mu\nu} = J^{a,\nu}$$

follow from extremizing the Yang-Mills action

$$S_{\text{YM}} = -\frac{1}{4} \int F^a_{\mu\nu} F^{a,\mu\nu} \, d^4x$$

subject to local gauge invariance under SU(3) (Yang & Mills, 1954). The constraint is gauge invariance. The threshold is $\Lambda_{\text{QCD}}$. The medium is the QCD vacuum with its gluon condensate.

**Minimum rules:** Both systems — gravity and the strong force — require exactly three ingredients to derive their field equations:

1. An **action functional** (what is optimized)
2. A **symmetry constraint** (what is preserved)
3. **Medium parameters** (what determines the threshold)

This is the same structure as the stick-slip framework: a system (the action), a constraint (the symmetry), and a medium-dependent threshold (the coupling scale).

**The gap:** The mimetic gravity framework writes one specific additional constraint ($g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi = 1$) beyond the action principle and derives dark matter as its Lagrange multiplier. The analogous program for QCD would be: identify a specific constraint on the gauge field — beyond gauge invariance itself — whose Lagrange multiplier produces confinement. This is a well-posed mathematical problem. Its solution would extend the framework from gravity to the strong force.

**References:**
- Hilbert, D. (1915). Die Grundlagen der Physik. *Nachr. Ges. Wiss. Göttingen*, 395.
- Yang, C. N. & Mills, R. L. (1954). Conservation of isotopic spin and isotopic gauge invariance. *Phys. Rev.*, 96, 191.
- Chamseddine, A. H. & Mukhanov, V. (2013). Mimetic dark matter. *JHEP*, 11, 135.
- Ekeland, I. & Temam, R. (1976). *Convex Analysis and Variational Problems*. North-Holland.

---

### 6. Constraint Violation at Black Hole Singularities

In Schwarzschild geometry with metric

$$ds^2 = -\left(1 - \frac{2M}{r}\right)dt^2 + \left(1 - \frac{2M}{r}\right)^{-1}dr^2 + r^2 d\Omega^2$$

the inverse metric component $g^{rr} = 1 - 2M/r$ changes sign at the horizon $r = 2M$ and diverges (in magnitude) as $r \to 0$. The Kretschner scalar $K = R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma} = 48M^2/r^6$ diverges at the singularity.

The mimetic constraint $g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi = 1$ involves these inverse metric components. For a radially-dependent scalar field $\phi = \phi(r)$, the constraint reads

$$g^{rr}(\phi')^2 = \left(1 - \frac{2M}{r}\right)(\phi')^2 = 1$$

Inside the horizon ($r < 2M$), $g^{rr} < 0$, and the constraint $g^{rr}(\phi')^2 = 1$ requires $(\phi')^2 < 0$ — which is impossible for a real scalar field. The constraint becomes unsatisfiable.

In the Lagrangian relaxation language (Boyd & Vandenberghe, 2004): when the constraint set is empty — no field configuration satisfies the constraint — the dual variable (Lagrange multiplier) diverges. This is the standard result when Slater's condition fails: the dual problem is unbounded. The singularity, in this framework, is not a point of infinite density but a point where the **cost of enforcing the geometric constraint becomes infinite** — constraint infeasibility.

The companion notebook computes $g^{rr}(\phi')^2$ as a function of $r/r_s$ and shows the divergence explicitly.

**References:**
- Chamseddine, A. H. & Mukhanov, V. (2013). Mimetic dark matter. *JHEP*, 11, 135.
- Sebastiani, L., Vagnozzi, S. & Myrzakulov, R. (2017). Mimetic gravity: a review. *Adv. High Energy Phys.*, 2017, 3156915.
- Boyd, S. & Vandenberghe, L. (2004). *Convex Optimization*. Cambridge University Press.
- Penrose, R. (1965). Gravitational collapse and space-time singularities. *Phys. Rev. Lett.*, 14, 57.

---

## Part II — Calculations

See companion notebook: `10_qcd_stribeck_comparison.ipynb`.

1. **QCD running coupling vs Stribeck fit** — 1-loop $\alpha_s$ for $n_f = 3, 4, 5$, overlaid with best-fit Stribeck function. Residuals and $R^2$.
2. **Clockwork chain lengths** — exact $N$ values for $q \in \{2, 3, 5, 7\}$ across all thresholds. Ratio analysis.
3. **Quadratic maximum verification** — Taylor expansion of MOND $\mu(x)$ at $x = 1$ and QCD $\beta(\alpha_s)$ at $\alpha_s = 0$. Universality class confirmation.
4. **Schwarzschild constraint violation** — $g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi$ vs $r/r_s$. Divergence at singularity.

---

## Part III — Pure Speculation

The following are mathematically precise conjectures for which no proof or experimental verification exists. They are included because they are falsifiable and because their resolution — positive or negative — would be informative.

### A. QCD Beta Function as Stribeck Gradient

The QCD beta function $\beta(g) = -\beta_0 g^3 - \beta_1 g^5 - \ldots$ determines how the coupling runs with energy. Can it be rewritten as the gradient of a Stribeck-type potential $V(g)$ such that $\beta = -dV/dg$?

If so, confinement is the "static friction" minimum of $V$ and asymptotic freedom is the "kinetic friction" plateau. The running coupling would be gradient descent on a potential landscape whose shape is the Stribeck curve.

Integrating $\beta(g) = -dV/dg$ gives $V(g) = \frac{\beta_0}{4}g^4 + \frac{\beta_1}{6}g^6 + \ldots$, which is a quartic potential with higher-order corrections. Whether this quartic can be approximated by the Stribeck exponential form over the physically relevant range of $g$ is a numerical question addressed in the companion notebook.

**Status:** Mathematically precise conjecture. No proof exists. *Partial progress:* The harmonics [Planck scale derivation](https://github.com/nickjoven/harmonics/blob/main/sync_cost/derivations/06_planck_scale.md) shows $N = 3$ (QCD color count) emerges as a threshold from synchronization cost geometry, connecting to QCD structure. The direct verification $\beta = -dV/dg$ remains open.

### B. QCD Feigenbaum Cascade

If the QCD running coupling and the gravitational Stribeck curve share the same Feigenbaum universality class (both have quadratic structure near their respective transition points, as shown in §3), then QCD should exhibit period-doubling cascades near the deconfinement transition at $T_c \approx 155$ MeV (Aoki et al., 2006).

The predicted sub-thresholds would be at temperatures determined by the logistic map bifurcation ratios:

$$T_1 = T_c, \quad T_2 = T_c \cdot \frac{r_1}{r_2} \approx 0.87 \, T_c, \quad T_3 = T_c \cdot \frac{r_1}{r_3} \approx 0.85 \, T_c$$

where $r_1 = 3.0$, $r_2 = 3.449$, $r_3 = 3.544$ are the logistic map bifurcation points.

**Status:** Prediction, untested. Lattice QCD at finite baryon chemical potential is limited by the sign problem — one of the major open problems in computational physics. If the sign problem is resolved, this prediction becomes testable.

**Reference:** Aoki, Y., Endrődi, G., Fodor, Z., Katz, S. D. & Szabó, K. K. (2006). The order of the quantum chromodynamics transition predicted by the standard model of particle physics. *Nature*, 443, 675.

### C. Yang-Mills Dual Variable as Confinement

If the Yang-Mills field equations can be formulated as a Lagrangian relaxation problem (action + an additional constraint beyond gauge invariance), the dual variable (Lagrange multiplier) would be the "price" of enforcing that constraint at each spacetime point. Confinement would be the regime where this price dominates the dynamics — the constraint is binding, in the language of complementary slackness.

The specific constraint has not been identified. Candidates include:
- A norm condition on the field strength: $F^a_{\mu\nu} F^{a,\mu\nu} = \text{const}$ (analogous to mimetic $g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi = 1$)
- A topological constraint related to the Pontryagin index $\int F \wedge F$
- A center symmetry constraint (relevant for the deconfinement transition)

**Status:** Research program, not a result. The specific constraint whose Lagrange multiplier produces confinement has not been written down.

### D. Superposition from Non-Injectivity

The CVT Law of Genealogical Non-Injectivity (Joven, 2026) states: "No present state certifies a unique history." If the forward map of physical law is non-injective at equilibrium, then quantum superposition — multiple states contributing to a measurement outcome — is the preimage degeneracy of a non-injective evolution operator.

Precisely: if the evolution operator $U: \mathcal{H} \to \mathcal{H}$ is non-injective, then for a given final state $|\psi_f\rangle$, the preimage $U^{-1}(|\psi_f\rangle)$ is an equivalence class of initial states. What we call "superposition" is the structure of this equivalence class. The Born rule ($P = |\langle\psi|\phi\rangle|^2$) would follow from a uniform measure over the preimage equivalence class.

**Status:** Open conjecture. Whether the Born rule is the uniform measure over the preimage equivalence class remains to be derived, not assumed. *Partial progress:* The harmonics [Born rule derivation](https://github.com/nickjoven/harmonics/blob/main/sync_cost/derivations/01_born_rule.md) approaches this from a different direction — deriving the Born rule from basin-of-attraction measure in the synchronization landscape, where probability emerges from the geometry of the cost surface rather than from non-injectivity. The two approaches may be complementary (basin measure as the mechanism, non-injectivity as the structural reason basins exist).

### E. Information at the Horizon

If non-injectivity holds for gravitational evolution, then "information loss" at a black hole horizon is not paradoxical. It is the expected behavior of a non-injective forward map: multiple pre-horizon histories map to the same post-horizon state. The "paradox" (Hawking, 1975) assumes the evolution operator is injective (unitary). If it is not, the paradox dissolves — but unitarity of quantum mechanics is sacrificed. Whether the cost is acceptable depends on whether non-injectivity can reproduce the successes of unitary quantum mechanics elsewhere.

**Status:** Reframing of the problem, not a resolution. No calculation demonstrates that gravitational evolution near a horizon is non-injective.

**References:**
- Hawking, S. W. (1975). Particle creation by black holes. *Commun. Math. Phys.*, 43, 199.
- 't Hooft, G. (1993). Dimensional reduction in quantum gravity. *Conf. Proc. C*, 930308, 284.

### F. Weak Force — Electroweak Symmetry Breaking

The Higgs potential $V(\phi) = -\mu^2|\phi|^2 + \lambda|\phi|^4$ undergoes a bifurcation at $T_{\text{EW}} \approx 159$ GeV (D'Onofrio & Rummukainen, 2016). Below $T_{\text{EW}}$, the symmetric vacuum is unstable and the system transitions to a broken-symmetry state with $\langle\phi\rangle = v = 246$ GeV. This is structurally a stick-slip transition: energy accumulates in the symmetric phase (stick), then releases into the broken phase (slip) with Goldstone modes converted into massive gauge boson degrees of freedom.

The Higgs potential is quartic, not the exponential Stribeck form. Whether the quartic shape constitutes a "different Stribeck curve" (belonging to the same broad class of threshold-mediated transfer functions) or a fundamentally different mechanism is unresolved. The quartic maximum has order $z = 2$ at the hilltop ($V''(0) = -2\mu^2 \neq 0$), so it would belong to the quadratic Feigenbaum universality class — but the potential is not a one-dimensional iterated map, and Feigenbaum theory does not directly apply to field-theoretic phase transitions without additional work.

**Status:** Structural analogy only. The functional form differs. The universality class argument requires a mapping to a one-dimensional iterated map that has not been constructed.

**References:**
- D'Onofrio, M. & Rummukainen, K. (2016). Standard model cross-over on the lattice. *Phys. Rev. D*, 93, 025003.
- Weinberg, S. (1967). A model of leptons. *Phys. Rev. Lett.*, 19, 1264.

---

## Summary Table

| Connection | Part | Mathematical status | Test / falsification |
|---|---|---|---|
| $\alpha_s$ shape $\sim$ Stribeck shape | I.1 | Established (both are monotone threshold functions) | Residual of Stribeck fit to $\alpha_s$ — see notebook |
| Flux tube breaking $=$ stick-slip | I.2 | Established (identical energy-threshold-release cycle) | Compare energy profiles quantitatively |
| Quadratic max $\to$ Feigenbaum $\delta$ | I.3 | Established (Feigenbaum, 1978) | Taylor expand $\mu(x)$ — verified |
| Clockwork multi-threshold | I.4 | Arithmetic (chain length ratios) | Compute and check — see notebook |
| Field equations from constrained optimization | I.5 | Established (Hilbert, 1915; Yang & Mills, 1954) | N/A — known result |
| Singularity as constraint infeasibility | I.6 | Calculation (mimetic constraint in Schwarzschild) | Compute $g^{rr}(\phi')^2$ — see notebook |
| QCD $\beta$ as Stribeck gradient | III.A | Conjecture | Integrate $\beta$, compare to Stribeck |
| QCD Feigenbaum cascade | III.B | Prediction | Lattice QCD at finite $\mu_B$ (sign problem) |
| Yang-Mills dual variable | III.C | Research program | Identify the constraint |
| Superposition from non-injectivity | III.D | Open conjecture | Derive Born rule from non-injectivity |
| Information at horizon | III.E | Reframing | Show gravitational non-injectivity |
| Electroweak as stick-slip | III.F | Structural analogy | Construct iterated map from Higgs potential |

---

*Companion notebook: `10_qcd_stribeck_comparison.ipynb`. Uses only Python standard library. CC0.*
