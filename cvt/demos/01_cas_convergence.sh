#!/usr/bin/env bash
# Demo 01 — CAS Convergence (Non-Injectivity, Mechanical)
#
# What it shows: Two independent reasoning chains about the same fact
# produce the same CID when their content converges. The store has no
# record of which path was taken. This is the law demonstrated by put().
set -euo pipefail

AUDIT_LOG="$(dirname "$0")/../audit/cids.log"
CLAIM="The forward map of a consistent rule system is non-injective at equilibrium."

# Path A: approached from thermodynamics
CID_A=$(echo "From thermodynamics: entropy measures the log of preimage degeneracy.
At equilibrium, multiple microstates map to the same macrostate.
Therefore: $CLAIM" | ket put -)

# Path B: approached from information theory
CID_B=$(echo "From information theory: compression identifies equivalence classes.
Independent compressions of the same fact produce identical bit strings.
Therefore: $CLAIM" | ket put -)

# Record to audit log
TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
echo "$TS | 01_cas_convergence | path_a | $CID_A" >> "$AUDIT_LOG"
echo "$TS | 01_cas_convergence | path_b | $CID_B" >> "$AUDIT_LOG"

# Report
echo "Path A CID: $CID_A"
echo "Path B CID: $CID_B"

if [ "$CID_A" = "$CID_B" ]; then
    echo "CONVERGED: Both paths produce the same CID."
    echo "The law holds mechanically in this substrate."
else
    echo "DIVERGED: CIDs differ."
    echo "The content differs — the reasoning was not equivalent."
fi
