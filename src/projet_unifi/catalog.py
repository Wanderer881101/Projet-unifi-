from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Maturity(str, Enum):
    STABLE = "stable"
    EXPERIMENTAL = "experimental"
    CONCEPTUAL = "conceptual"
    LEGACY = "legacy"


@dataclass(frozen=True, slots=True)
class CapabilityDescriptor:
    name: str
    maturity: Maturity
    description: str
    side_effects: bool = False
    provenance: str = "public-runtime"


BUILTIN_CATALOG: tuple[CapabilityDescriptor, ...] = (
    CapabilityDescriptor(
        "core.identity",
        Maturity.STABLE,
        "Return the runtime public identity.",
    ),
    CapabilityDescriptor(
        "core.echo",
        Maturity.STABLE,
        "Deterministic local echo primitive.",
    ),
    CapabilityDescriptor(
        "health.snapshot",
        Maturity.STABLE,
        "Return runtime health and observability counters.",
    ),
    CapabilityDescriptor(
        "simulation.assess",
        Maturity.EXPERIMENTAL,
        "Local deterministic assessment primitive with normalized factors.",
    ),
)


def descriptor_for(name: str) -> CapabilityDescriptor | None:
    return next((item for item in BUILTIN_CATALOG if item.name == name), None)


def public_catalog() -> tuple[CapabilityDescriptor, ...]:
    return BUILTIN_CATALOG
