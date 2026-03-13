#!/usr/bin/env bash
# Demo 02 — Genealogical Gauge Choice
#
# What it shows: Two lineages lead to the same terminal node. ket dag
# lineage returns different paths. The CID is identical. Lineage is gauge.
set -euo pipefail

AUDIT_LOG="$(dirname "$0")/../audit/cids.log"

# Build two independent lineages toward a shared conclusion
ROOT_A=$(echo "Premise A: symmetry breaking is gauge selection" | ket put -)
ROOT_B=$(echo "Premise B: measurement collapse is gauge selection" | ket put -)

# Each lineage develops independently
MID_A=$(ket dag create "Intermediate: Higgs mechanism as committed history" \
        --kind reasoning --agent human --parent "$ROOT_A" --json | jq -r .node_cid)
MID_B=$(ket dag create "Intermediate: decoherence as irreversible gauge commitment" \
        --kind reasoning --agent human --parent "$ROOT_B" --json | jq -r .node_cid)

# Shared conclusion — content identical regardless of path
CONCLUSION="The state space supports non-unique preimage histories. \
Lineage is gauge choice, not ground truth. CID certifies present. \
No present state certifies a unique history."

CID_CONTENT=$(echo "$CONCLUSION" | ket put -)

# Two nodes, same output_cid, different parents
NODE_A=$(ket dag create "Conclusion via thermodynamic path" \
         --kind reasoning --agent human \
         --parent "$MID_A" --json | jq -r .node_cid)
NODE_B=$(ket dag create "Conclusion via quantum path" \
         --kind reasoning --agent human \
         --parent "$MID_B" --json | jq -r .node_cid)

# Record to audit log
TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
echo "$TS | 02_gauge_choice | root_a | $ROOT_A" >> "$AUDIT_LOG"
echo "$TS | 02_gauge_choice | root_b | $ROOT_B" >> "$AUDIT_LOG"
echo "$TS | 02_gauge_choice | mid_a | $MID_A" >> "$AUDIT_LOG"
echo "$TS | 02_gauge_choice | mid_b | $MID_B" >> "$AUDIT_LOG"
echo "$TS | 02_gauge_choice | conclusion_content | $CID_CONTENT" >> "$AUDIT_LOG"
echo "$TS | 02_gauge_choice | node_a | $NODE_A" >> "$AUDIT_LOG"
echo "$TS | 02_gauge_choice | node_b | $NODE_B" >> "$AUDIT_LOG"

# Lineage traces differ. Output content is the same.
echo "Lineage A:"
ket dag lineage "$NODE_A"
echo ""
echo "Lineage B:"
ket dag lineage "$NODE_B"
echo ""
echo "Both output CIDs: $CID_CONTENT"

# Export for use by downstream demos
export CVT_NODE_A="$NODE_A"
export CVT_NODE_B="$NODE_B"
export CVT_CONCLUSION_CID="$CID_CONTENT"
