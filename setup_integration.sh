#!/bin/bash
# Projet-unifi- Integration Script
# Integrate the Nexus repositories using git subtree.
# Usage: bash setup_integration.sh

set -euo pipefail

REPO_URL="https://github.com/Wanderer881101"

# Keep the script safe to re-run: add a subtree only when its prefix is absent,
# otherwise pull the existing subtree. This avoids an add followed immediately
# by a pull of the same source.
integrate_subtree() {
  local prefix="$1"
  local repository="$2"

  if [ -d "$prefix" ] || git ls-tree -d HEAD -- "$prefix" | grep -q .; then
    echo "🔄 Updating $prefix from $repository..."
    git subtree pull --prefix="$prefix" "${REPO_URL}/${repository}.git" main --squash
  else
    echo "📦 Adding $prefix from $repository..."
    git subtree add --prefix="$prefix" "${REPO_URL}/${repository}.git" main --squash
  fi
}

echo "🔧 Starting Nexus System Integration..."

git config user.name "Jonathan Therrien"
git config user.email "jonathantherrien2021@gmail.com"

integrate_subtree "src/nexus-core" "Nex-us-V"
integrate_subtree "src/module" "module"
integrate_subtree "build/dist" "3-Nex-us-V"
integrate_subtree "build/lib" "4-Nex-us-V"
integrate_subtree "build/runtime" "5-Nex-us-V"
integrate_subtree "build/cache" "6-Nex-us-V"
integrate_subtree "templates" "2-Nex-us-V"

# 7-Nex-us-V is a template variant. Keep the primary templates subtree intact;
# merge that repository manually if its files differ and should be preserved.

echo "🔎 Validating unified structure..."
python3 scripts/validate_structure.py

echo "✅ Integration complete."

git add .
git diff --cached --quiet || git commit -m "feat: integrate Nexus repositories"

echo "🎉 Setup finished successfully!"
