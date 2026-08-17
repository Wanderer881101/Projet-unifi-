from __future__ import annotations

from projet_unifi.legacy import probe_dependencies, probe_legacy_sources


def test_dependency_probe_never_requires_optional_stack() -> None:
    statuses = probe_dependencies((("json", "stdlib"), ("definitely_missing_package_xyz", "fixture")))
    by_name = {item.name: item for item in statuses}
    assert by_name["json"].available is True
    assert by_name["definitely_missing_package_xyz"].available is False


def test_legacy_source_probe_is_non_destructive(tmp_path) -> None:
    original = tmp_path / "nexus_core.py"
    original.write_text("# historical fixture\n", encoding="utf-8")

    statuses = probe_legacy_sources(tmp_path)
    by_name = {item.source: item for item in statuses}

    assert by_name["nexus_core"].present is True
    assert original.read_text(encoding="utf-8") == "# historical fixture\n"
    assert by_name["lagrosseclef"].present is False
