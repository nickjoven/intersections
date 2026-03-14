# Synthesis — What Resolves, What Remains Open

## Resolves immediately

- **α₀ without calibration**: thermal time sets the critical threshold.
  Substrate temperature (activation distribution uniformity) determines
  the MM decay transition point. Not a design parameter.

- **WQS stationarity**: if time's structure dominates node-level variation,
  stationarity holds from the outside in. The grid search fallback becomes
  unnecessary when the temporal structure is well-defined.

- **The floor**: drops to exactly zero in the 1/f case. The hyperbolic
  tail provides physical persistence without a hard lower bound.

- **λ as substrate-level**: decay rate is the inverse substrate temperature,
  not a per-node declaration. Collapses heterogeneous decay to one parameter
  readable from the Dolt commit log's power spectrum.

## Remains open

- Whether the substrate's temporal spectrum is genuinely 1/f (requires
  measurement from git log, not assumption).

- Whether CAS convergence is the substrate's version of thermal equilibrium
  in the modular Hamiltonian sense (requires formal proof).

- Whether the Born rule is the uniform measure over the preimage equivalence
  class (requires deriving from the non-injectivity law, not assuming).

- Whether the Higgs mass and electroweak scale are determined by the depth
  of gauge commitment across the causal past (requires physical derivation,
  not analogy). See `fundamental_forces_planck_scale.md` §III.F for the
  structural analogy to stick-slip and the obstacles to making it rigorous.

## The math needed

Intersection of:

- **Category theory**: structure of the forward map
- **Ergodic theory**: conditions on equilibrium
- **Information geometry**: measure over preimage equivalence classes

All three exist. The combination with this target does not yet exist.
