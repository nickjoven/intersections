#!/usr/bin/env bash
# Demo 03 — Equilibrium and Pruning
#
# What it shows: Nodes declared at saturation=1.0 are pruned by the WQS
# optimizer without consulting lineage. The optimizer has abandoned history
# as relevant. This is what equilibrium looks like operationally.
set -euo pipefail

AUDIT_LOG="$(dirname "$0")/../audit/cids.log"

# Mark the shared conclusion as a settled claim
# Optimizer assigns Tier::Skip without touching the scores table
NODE=$(ket dag create "Non-injectivity law: settled claim" \
       --kind reasoning --agent human \
       --meta "saturation=1.0" --json | jq -r .node_cid)

# Score it across dimensions to confirm convergence
ket scores add "$NODE" --agent human --dim correctness --value 1.0 \
    --evidence "Proven by CAS convergence in demo 01"
ket scores add "$NODE" --agent human --dim completeness --value 1.0 \
    --evidence "Boundary conditions established in demo 02"

# Run calibration from this node as root
# Expect: Tier::Skip assigned immediately
# The optimizer does not ask how we got here
ket calibrate run "$NODE" --max-cost 10

# Record to audit log
TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
echo "$TS | 03_equilibrium | settled_node | $NODE" >> "$AUDIT_LOG"

echo "Node $NODE: optimizer prunes without lineage query."
echo "Equilibrium is not a claim. It is a structural state."

# Export for use by downstream demos
export CVT_SETTLED_NODE="$NODE"
