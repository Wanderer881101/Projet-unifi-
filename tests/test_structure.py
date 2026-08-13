from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_repository_scaffold_is_complete():
    required = [
        "README.md",
        "MANIFEST.md",
        "STRUCTURE.md",
        "docs/WORKFLOWS.md",
        "scripts/validate_structure.py",
        "setup_integration.sh",
    ]
    missing = [path for path in required if not (ROOT / path).exists()]
    assert not missing, f"Missing repository scaffold files: {missing}"


def test_validator_is_valid_python():
    source = (ROOT / "scripts/validate_structure.py").read_text(encoding="utf-8")
    compile(source, "scripts/validate_structure.py", "exec")
