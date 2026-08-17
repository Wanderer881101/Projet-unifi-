from __future__ import annotations

import inspect
import time
from collections.abc import Awaitable, Callable
from typing import Any

from .models import CapabilityResult
from .policy import PolicyEngine

Capability = Callable[..., Any] | Callable[..., Awaitable[Any]]


class CapabilityRegistry:
    def __init__(self, policy: PolicyEngine) -> None:
        self._items: dict[str, Capability] = {}
        self._policy = policy

    def register(self, name: str, capability: Capability, *, replace: bool = False) -> None:
        if name in self._items and not replace:
            raise ValueError(f"capability already registered: {name}")
        self._items[name] = capability

    def names(self) -> tuple[str, ...]:
        return tuple(sorted(self._items))

    async def invoke(self, name: str, **kwargs: Any) -> CapabilityResult:
        started = time.perf_counter()
        if name not in self._items:
            return CapabilityResult(name, False, error="unknown capability")
        if not self._policy.authorize(name):
            return CapabilityResult(name, False, error="capability denied by policy")

        try:
            result = self._items[name](**kwargs)
            if inspect.isawaitable(result):
                result = await result
            return CapabilityResult(
                capability=name,
                ok=True,
                data=result,
                duration_ms=(time.perf_counter() - started) * 1000,
            )
        except Exception as exc:  # boundary: convert plugin failure into runtime result
            return CapabilityResult(
                capability=name,
                ok=False,
                error=f"{type(exc).__name__}: {exc}",
                duration_ms=(time.perf_counter() - started) * 1000,
            )
