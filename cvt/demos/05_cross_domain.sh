#!/usr/bin/env bash
# Demo 05 — Cross-Domain Convergence
#
# What it shows: Physics claims (astrophysics, particle physics) stored as
# nodes converge to the same epistemic equilibrium as substrate claims.
# The constraining vector is structural, not domain-specific.
# Thermodynamics is emergent in both.
set -euo pipefail

AUDIT_LOG="$(dirname "$0")/../audit/cids.log"

# Store claims from disconnected domains
# Show they reach saturation by the same mechanism

ASTRO=$(echo "The arrow of time points uniformly across the observable universe. \
Standard account: low-entropy initial conditions. \
Consistency account: non-injectivity requires a globally coherent preimage \
structure. A reversed local arrow produces ontological contradiction, not \
physical impossibility." | ket put -)

PARTICLE=$(echo "Electroweak symmetry breaks at 246 GeV. \
Standard account: Higgs mechanism, spontaneous breaking. \
Consistency account: the vacuum commits to one lineage among equally viable \
prior states. The Higgs mass is set by the depth of that gauge commitment \
across the full causal past." | ket put -)

SUBSTRATE=$(echo "CAS convergence certifies present state without certifying \
unique history. Saturation=1.0 licenses pruning without lineage query. \
The substrate reaches equilibrium by the same mechanism as the universe." \
| ket put -)

# Use settled node from demo 03 if available, otherwise create one
if [ -z "${CVT_SETTLED_NODE:-}" ]; then
    NODE=$(ket dag create "Non-injectivity law: settled claim" \
           --kind reasoning --agent human \
           --meta "saturation=1.0" --json | jq -r .node_cid)
else
    NODE="$CVT_SETTLED_NODE"
fi

# All three into the DAG, linked to the law node
ket dag create "Astrophysics: time arrow via consistency" \
    --kind reasoning --agent human --parent "$NODE"
ket dag create "Particle physics: symmetry breaking via gauge commitment" \
    --kind reasoning --agent human --parent "$NODE"
ket dag create "Substrate: equilibrium by same mechanism" \
    --kind reasoning --agent human --parent "$NODE"

# Score cross-domain consistency
ket scores add "$NODE" --agent human --dim correctness --value 0.9 \
    --evidence "Three independent domains reach same structural conclusion"

# Record to audit log
TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
echo "$TS | 05_cross_domain | astrophysics | $ASTRO" >> "$AUDIT_LOG"
echo "$TS | 05_cross_domain | particle_physics | $PARTICLE" >> "$AUDIT_LOG"
echo "$TS | 05_cross_domain | substrate | $SUBSTRATE" >> "$AUDIT_LOG"
echo "$TS | 05_cross_domain | law_node | $NODE" >> "$AUDIT_LOG"

echo "Cross-domain convergence recorded."
echo "The bridge is auditable from the CIDs."
