from __future__ import annotations

from dataclasses import dataclass
from importlib.util import find_spec
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True, slots=True)
class DependencyStatus:
    name: str
    available: bool
    required_for: str
    kind: str = "python"


@dataclass(frozen=True, slots=True)
class LegacySourceStatus:
    source: str
    present: bool
    path: str | None = None


KNOWN_OPTIONAL_DEPENDENCIES: tuple[tuple[str, str], ...] = (
    ("ccxt", "Nexus finance connectors"),
    ("web3", "Nexus blockchain connectors"),
    ("docker", "Lagrosseclef container integration"),
    ("kubernetes", "Lagrosseclef cluster integration"),
    ("grpc", "Lagrosseclef RPC integration"),
    ("boto3", "Lagrosseclef AWS integration"),
    ("google.cloud.storage", "Lagrosseclef Google Cloud integration"),
    ("azure.identity", "Lagrosseclef Azure integration"),
    ("tensorflow", "Lagrosseclef ML integration"),
    ("prometheus_client", "Lagrosseclef observability integration"),
    ("numpy", "Nexus numerical features"),
    ("sklearn", "Nexus machine-learning features"),
    ("pqc_module", "Lagrosseclef post-quantum integration"),
)


def probe_dependencies(
    dependencies: Iterable[tuple[str, str]] = KNOWN_OPTIONAL_DEPENDENCIES,
) -> tuple[DependencyStatus, ...]:
    """Inspect legacy integration dependencies without importing them.

    This intentionally uses ``find_spec`` instead of importing packages because
    several historical modules perform infrastructure detection or other work at
    import time. Public runtime startup must stay side-effect free.
    """

    statuses: list[DependencyStatus] = []
    for name, purpose in dependencies:
        try:
            available = find_spec(name) is not None
        except (ImportError, ModuleNotFoundError, AttributeError, ValueError):
            available = False
        statuses.append(DependencyStatus(name=name, available=available, required_for=purpose))
    return tuple(statuses)


def probe_legacy_sources(root: str | Path) -> tuple[LegacySourceStatus, ...]:
    """Report presence of preserved historical source files without modifying them."""

    base = Path(root)
    candidates = (
        ("nexus_core", "nexus_core.py"),
        ("nexus_ai", "nexus_ai.py"),
        ("nexus_network", "nexus_network.py"),
        ("nexus_memory", "nexus_memory.py"),
        ("nexus_persistence", "nexus_persistence.py"),
        ("nexus_ml", "nexus_ml.py"),
        ("lagrosseclef", "Lagrosseclef.py"),
        ("seconde_genese", "protocole de la seconde genèse.py"),
    )
    result: list[LegacySourceStatus] = []
    for source, relative in candidates:
        path = base / relative
        result.append(
            LegacySourceStatus(
                source=source,
                present=path.is_file(),
                path=str(path) if path.is_file() else None,
            )
        )
    return tuple(result)
