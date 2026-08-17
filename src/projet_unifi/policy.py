from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class PolicyEngine:
    """Default-deny policy layer for capabilities with external side effects."""

    allowed: set[str] = field(default_factory=set)
    denied: set[str] = field(default_factory=set)
    denials: int = 0

    SAFE_PREFIXES = ("core.", "memory.", "analysis.", "simulation.", "health.")

    def authorize(self, capability: str) -> bool:
        if capability in self.denied:
            self.denials += 1
            return False
        if capability in self.allowed or capability.startswith(self.SAFE_PREFIXES):
            return True
        self.denials += 1
        return False

    def allow(self, capability: str) -> None:
        self.denied.discard(capability)
        self.allowed.add(capability)

    def deny(self, capability: str) -> None:
        self.allowed.discard(capability)
        self.denied.add(capability)
