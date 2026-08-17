from __future__ import annotations

import time
from typing import Any

from .capabilities import CapabilityRegistry
from .event_bus import EventBus
from .models import Event, HealthReport, RuntimeState
from .policy import PolicyEngine


class NexusRuntime:
    """Public V2 runtime: observable, policy-driven and capability-oriented."""

    def __init__(self, identifier: str = "Nexus_Public") -> None:
        self.identifier = identifier
        self.state = RuntimeState.CREATED
        self.policy = PolicyEngine()
        self.events = EventBus()
        self.capabilities = CapabilityRegistry(self.policy)
        self._started_at: float | None = None
        self._install_builtin_capabilities()

    def _install_builtin_capabilities(self) -> None:
        self.capabilities.register("core.identity", lambda: {"identifier": self.identifier})
        self.capabilities.register("core.echo", lambda value=None: value)
        self.capabilities.register("health.snapshot", self.health)
        self.capabilities.register("simulation.assess", self._simulation_assess)

    async def start(self) -> None:
        if self.state == RuntimeState.RUNNING:
            return
        self.state = RuntimeState.STARTING
        await self.events.start()
        self._started_at = time.monotonic()
        self.state = RuntimeState.RUNNING
        await self.events.publish(Event("runtime.started", {"identifier": self.identifier}))

    async def stop(self) -> None:
        if self.state in {RuntimeState.STOPPED, RuntimeState.CREATED}:
            self.state = RuntimeState.STOPPED
            return
        self.state = RuntimeState.STOPPING
        await self.events.publish(Event("runtime.stopping", {"identifier": self.identifier}))
        await self.events.stop()
        self.state = RuntimeState.STOPPED

    async def invoke(self, capability: str, **kwargs: Any):
        if self.state != RuntimeState.RUNNING:
            raise RuntimeError("runtime must be running before invoking capabilities")
        result = await self.capabilities.invoke(capability, **kwargs)
        await self.events.publish(
            Event(
                "capability.invoked",
                {"capability": capability, "ok": result.ok, "duration_ms": result.duration_ms},
            )
        )
        return result

    def health(self) -> HealthReport:
        uptime = 0.0 if self._started_at is None else max(0.0, time.monotonic() - self._started_at)
        return HealthReport(
            state=self.state,
            capabilities=self.capabilities.names(),
            events_processed=self.events.processed,
            policy_denials=self.policy.denials,
            uptime_seconds=uptime,
        )

    @staticmethod
    def _simulation_assess(target: str, factors: dict[str, float] | None = None) -> dict[str, Any]:
        """Deterministic local assessment primitive; no external scan or hidden side effect."""
        factors = factors or {}
        normalized = {key: min(1.0, max(0.0, float(value))) for key, value in factors.items()}
        score = sum(normalized.values()) / len(normalized) if normalized else 0.0
        return {"target": target, "score": round(score, 6), "factors": normalized, "mode": "simulation"}
