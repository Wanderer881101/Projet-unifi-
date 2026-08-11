#!/bin/bash
# Projet-unifi- Integration Script
# Integrate all repositories using git subtree
# Usage: bash setup_integration.sh

set -e

REPO_URL="https://github.com/Wanderer881101"
MAIN_REPO="Projet-unifi-"

echo "🔧 Starting Nexus System Integration..."

# Configure git
git config user.name "Jonathan Therrien"
git config user.email "jonathantherrien2021@gmail.com"

# 1. Add Nex-us-V source code
echo "📦 Integrating Nex-us-V (core)..."
git subtree add --prefix=src/nexus-core ${REPO_URL}/Nex-us-V.git main --squash || echo "Subtree exists, updating..."
git subtree pull --prefix=src/nexus-core ${REPO_URL}/Nex-us-V.git main --squash

# 2. Add module protocols
echo "📦 Integrating module (protocols)..."
git subtree add --prefix=src/module ${REPO_URL}/module.git main --squash || echo "Subtree exists, updating..."
git subtree pull --prefix=src/module ${REPO_URL}/module.git main --squash

# 3. Add build artifacts
echo "📦 Integrating 3-Nex-us-V (dist)..."
git subtree add --prefix=build/dist ${REPO_URL}/3-Nex-us-V.git main --squash || echo "Subtree exists, updating..."
git subtree pull --prefix=build/dist ${REPO_URL}/3-Nex-us-V.git main --squash

echo "📦 Integrating 4-Nex-us-V (lib)..."
git subtree add --prefix=build/lib ${REPO_URL}/4-Nex-us-V.git main --squash || echo "Subtree exists, updating..."
git subtree pull --prefix=build/lib ${REPO_URL}/4-Nex-us-V.git main --squash

echo "📦 Integrating 5-Nex-us-V (runtime)..."
git subtree add --prefix=build/runtime ${REPO_URL}/5-Nex-us-V.git main --squash || echo "Subtree exists, updating..."
git subtree pull --prefix=build/runtime ${REPO_URL}/5-Nex-us-V.git main --squash

echo "📦 Integrating 6-Nex-us-V (cache)..."
git subtree add --prefix=build/cache ${REPO_URL}/6-Nex-us-V.git main --squash || echo "Subtree exists, updating..."
git subtree pull --prefix=build/cache ${REPO_URL}/6-Nex-us-V.git main --squash

# 4. Add templates
echo "📦 Integrating 2-Nex-us-V & 7-Nex-us-V (templates)..."
git subtree add --prefix=templates ${REPO_URL}/2-Nex-us-V.git main --squash || echo "Subtree exists, updating..."
git subtree pull --prefix=templates ${REPO_URL}/2-Nex-us-V.git main --squash

echo "✅ Integration complete!"
echo "💾 Committing changes..."
git add .
git commit -m "feat: Integrate all Nexus repositories via git subtree" || echo "No changes to commit"

echo "🎉 Setup finished successfully!"
