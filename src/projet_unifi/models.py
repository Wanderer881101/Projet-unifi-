from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any
from uuid import uuid4


class RuntimeState(str, Enum):
    CREATED = "created"
    STARTING = "starting"
    RUNNING = "running"
    STOPPING = "stopping"
    STOPPED = "stopped"
    DEGRADED = "degraded"


@dataclass(frozen=True, slots=True)
class Event:
    topic: str
    payload: dict[str, Any] = field(default_factory=dict)
    source: str = "runtime"
    event_id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass(frozen=True, slots=True)
class CapabilityResult:
    capability: str
    ok: bool
    data: Any = None
    error: str | None = None
    duration_ms: float = 0.0


@dataclass(frozen=True, slots=True)
class HealthReport:
    state: RuntimeState
    capabilities: tuple[str, ...]
    events_processed: int
    policy_denials: int
    uptime_seconds: float
