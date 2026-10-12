#!/bin/bash
# Rendert alle ruimtes op volle kwaliteit en maakt webversies. Gebruik: ./render-alle.sh [uitmap] [ruimtes...]
cd "$(dirname "$0")"
OUT=${1:-/tmp/claude-0/r/final}; shift
mkdir -p "$OUT"
ROOMS=${@:-badkamer toilet keuken woonkamer slaapkamer kantoor}
for r in $ROOMS; do
  echo "== $r $(date +%T)"
  python3 ruimte_$r.py "$OUT/$r.png" 1800 1200 128 2>&1 | grep -E "Saved|Error" 
  python3 nabewerking.py "$OUT/$r.png" "$OUT/$r.jpg"
done
echo "klaar $(date +%T)"
