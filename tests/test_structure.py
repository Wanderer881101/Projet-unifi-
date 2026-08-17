from __future__ import annotations

from pathlib import Path

from scripts.validate_structure import EXPECTED_DOCUMENTATION, PUBLIC_RUNTIME, ROOT


def test_documentation_scaffold_is_materialized() -> None:
    missing = sorted(path for path in EXPECTED_DOCUMENTATION if not (ROOT / path).exists())
    assert missing == []


def test_public_runtime_is_materialized() -> None:
    missing = sorted(path for path in PUBLIC_RUNTIME if not (ROOT / path).exists())
    assert missing == []


def test_validator_root_points_to_repository() -> None:
    assert (ROOT / "README.md").is_file()
    assert (ROOT / "pyproject.toml").is_file()
    assert ROOT == Path(__file__).resolve().parents[1]
