#!/usr/bin/env python3
"""Validate the unified Nexus repository and report materialized integration state.

This is intentionally truthful: missing historical integration targets are reported as
PENDING instead of being treated as if they already existed merely because MANIFEST.md
mentions them.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_DOCUMENTATION = {
    "README.md",
    "MANIFEST.md",
    "STRUCTURE.md",
    "docs/WORKFLOWS.md",
    "docs/PROVENANCE.md",
    "docs/SOURCE_AUDIT.md",
    "docs/ARCHITECTURE_2028.md",
    "setup_integration.sh",
}
PUBLIC_RUNTIME = {
    "pyproject.toml",
    "src/projet_unifi/__init__.py",
    "src/projet_unifi/runtime.py",
    "src/projet_unifi/capabilities.py",
    "src/projet_unifi/event_bus.py",
    "src/projet_unifi/policy.py",
    "src/projet_unifi/models.py",
    "src/projet_unifi/cli.py",
    "src/projet_unifi/legacy.py",
    "src/projet_unifi/catalog.py",
}
EXPECTED_INTEGRATION_PATHS = {
    "src/nexus-core": "Nex-us-V",
    "src/module": "module",
    "build/dist": "3-Nex-us-V",
    "build/lib": "4-Nex-us-V",
    "build/runtime": "5-Nex-us-V",
    "build/cache": "6-Nex-us-V",
    "templates": "2-Nex-us-V / 7-Nex-us-V",
}


def _missing(paths: set[str]) -> list[str]:
    return sorted(path for path in paths if not (ROOT / path).exists())


def main() -> int:
    missing_docs = _missing(EXPECTED_DOCUMENTATION)
    missing_runtime = _missing(PUBLIC_RUNTIME)

    if missing_docs or missing_runtime:
        if missing_docs:
            print("ERROR: missing repository/documentation files:")
            for path in missing_docs:
                print(f"  - {path}")
        if missing_runtime:
            print("ERROR: missing public runtime files:")
            for path in missing_runtime:
                print(f"  - {path}")
        return 1

    print("Documentation scaffold: OK")
    print("Public runtime scaffold: OK")
    print("Historical integration status:")
    missing_integrations = []
    for path, source in EXPECTED_INTEGRATION_PATHS.items():
        present = (ROOT / path).exists()
        state = "PRESENT" if present else "PENDING"
        if not present:
            missing_integrations.append(path)
        print(f"  [{state}] {path} <- {source}")

    print()
    if missing_integrations:
        print(
            f"{len(missing_integrations)} historical integration target(s) remain pending. "
            "This does not invalidate the standalone public runtime."
        )
    else:
        print("All declared historical integration targets are present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
