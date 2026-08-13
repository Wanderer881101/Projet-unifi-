#!/usr/bin/env python3
"""Validate the unified Nexus repository without requiring the source repos to be embedded.

The repository currently starts as an integration manifest. This validator deliberately
checks the files that are present and reports missing integration targets separately,
so documentation cannot claim that a subtree exists when it does not.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_DOCUMENTATION = {
    "README.md",
    "MANIFEST.md",
    "STRUCTURE.md",
    "docs/WORKFLOWS.md",
    "setup_integration.sh",
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


def main() -> int:
    missing_docs = [p for p in EXPECTED_DOCUMENTATION if not (ROOT / p).exists()]
    missing_integrations = [p for p in EXPECTED_INTEGRATION_PATHS if not (ROOT / p).exists()]

    if missing_docs:
        print("ERROR: missing repository files:")
        for path in missing_docs:
            print(f"  - {path}")
        return 1

    print("Documentation scaffold: OK")
    print("Integration status:")
    for path, source in EXPECTED_INTEGRATION_PATHS.items():
        state = "PRESENT" if (ROOT / path).exists() else "PENDING"
        print(f"  [{state}] {path} <- {source}")

    print()
    if missing_integrations:
        print(
            f"{len(missing_integrations)} integration target(s) are not present yet. "
            "Run setup_integration.sh from a local checkout to materialize them."
        )
    else:
        print("All declared integration targets are present.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
