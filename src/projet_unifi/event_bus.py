from __future__ import annotations

import asyncio
from collections import defaultdict
from collections.abc import Awaitable, Callable

from .models import Event

EventHandler = Callable[[Event], Awaitable[None]]


class EventBus:
    """Small async event bus with explicit backpressure and deterministic shutdown."""

    def __init__(self, max_queue_size: int = 1024) -> None:
        self._queue: asyncio.Queue[Event] = asyncio.Queue(maxsize=max_queue_size)
        self._handlers: dict[str, list[EventHandler]] = defaultdict(list)
        self._worker: asyncio.Task[None] | None = None
        self._running = False
        self.processed = 0

    def subscribe(self, topic: str, handler: EventHandler) -> None:
        if handler not in self._handlers[topic]:
            self._handlers[topic].append(handler)

    async def publish(self, event: Event) -> None:
        await self._queue.put(event)

    async def start(self) -> None:
        if self._running:
            return
        self._running = True
        self._worker = asyncio.create_task(self._run(), name="projet-unifi-event-bus")

    async def stop(self) -> None:
        if not self._running:
            return
        await self._queue.join()
        self._running = False
        if self._worker:
            self._worker.cancel()
            try:
                await self._worker
            except asyncio.CancelledError:
                pass
            self._worker = None

    async def _run(self) -> None:
        while self._running:
            event = await self._queue.get()
            try:
                handlers = [*self._handlers.get(event.topic, []), *self._handlers.get("*", [])]
                for handler in handlers:
                    await handler(event)
                self.processed += 1
            finally:
                self._queue.task_done()
