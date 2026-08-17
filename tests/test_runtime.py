from __future__ import annotations

import asyncio

from projet_unifi.runtime import NexusRuntime


def test_runtime_start_invoke_and_stop() -> None:
    async def scenario() -> None:
        runtime = NexusRuntime("test-nexus")
        await runtime.start()
        assert runtime.health().state.value == "running"

        identity = await runtime.invoke("core.identity")
        assert identity.ok is True
        assert identity.data == {"identifier": "test-nexus"}

        echo = await runtime.invoke("core.echo", value={"preserved": True})
        assert echo.ok is True
        assert echo.data == {"preserved": True}

        await runtime.stop()
        assert runtime.health().state.value == "stopped"

    asyncio.run(scenario())


def test_policy_denies_external_unknown_capability() -> None:
    async def scenario() -> None:
        runtime = NexusRuntime()
        await runtime.start()
        try:
            result = await runtime.invoke("network.external.scan", target="example")
            assert result.ok is False
            assert result.error == "unknown capability"
        finally:
            await runtime.stop()

    asyncio.run(scenario())


def test_simulation_assess_is_bounded_and_deterministic() -> None:
    async def scenario() -> None:
        runtime = NexusRuntime()
        await runtime.start()
        try:
            result = await runtime.invoke(
                "simulation.assess",
                target="local-fixture",
                factors={"a": -4.0, "b": 0.5, "c": 9.0},
            )
            assert result.ok is True
            assert result.data["factors"] == {"a": 0.0, "b": 0.5, "c": 1.0}
            assert result.data["score"] == 0.5
            assert result.data["mode"] == "simulation"
        finally:
            await runtime.stop()

    asyncio.run(scenario())
