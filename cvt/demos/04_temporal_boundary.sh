#!/usr/bin/env bash
# Demo 04 — Boundary Entropy as Gauge-Invariant Time
#
# What it shows: Nodes with more independent lineages (higher boundary
# entropy) persist longer under MM decay. The temporal measure is a
# function of the boundary — not of any single path. This is the
# gauge-invariant clock.
set -euo pipefail

AUDIT_LOG="$(dirname "$0")/../audit/cids.log"

# Compare decay persistence: single-lineage node vs multi-lineage node

# Single lineage: one path, low boundary entropy
SINGLE=$(ket dag create "Isolated claim, one ancestor" \
         --kind reasoning --agent human \
         --meta "decay_lambda=0.1" \
         --meta "decay_alpha0=0.2" --json | jq -r .node_cid)

# Multi-lineage: same content, two independent paths (from demo 02)
# NODE_A and NODE_B both reach the same conclusion
# Boundary entropy is log(2) vs log(1)

# If demo 02 was sourced, use its exports; otherwise note the dependency
if [ -z "${CVT_NODE_A:-}" ]; then
    echo "Note: Run demo 02 first to populate CVT_NODE_A."
    echo "Using single-lineage comparison only."
    NODE_A_CID="(requires demo 02)"
else
    NODE_A_CID="$CVT_NODE_A"
fi

# Query decay status at equivalent elapsed time
echo "Single-lineage decay at t=3600:"
ket mcp decay_status --cid "$SINGLE" --elapsed_secs 3600

if [ -n "${CVT_NODE_A:-}" ]; then
    echo ""
    echo "Multi-lineage node (NODE_A) at t=3600:"
    ket mcp decay_status --cid "$CVT_NODE_A" --elapsed_secs 3600
fi

# Record to audit log
TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
echo "$TS | 04_temporal_boundary | single_lineage | $SINGLE" >> "$AUDIT_LOG"
if [ -n "${CVT_NODE_A:-}" ]; then
    echo "$TS | 04_temporal_boundary | multi_lineage_a | $CVT_NODE_A" >> "$AUDIT_LOG"
fi

# Expected: multi-lineage node retains higher activation.
# The boundary provides the persistence — not the node itself.
# This is the Ryu-Takayanagi analog in the substrate.
echo ""
echo "Expected: multi-lineage node retains higher activation."
echo "The boundary provides the persistence — not the node itself."
