from __future__ import annotations

import argparse
import asyncio
import json
from dataclasses import asdict
from enum import Enum
from typing import Any

from .runtime import NexusRuntime


def _json_default(value: Any) -> Any:
    if isinstance(value, Enum):
        return value.value
    if hasattr(value, "isoformat"):
        return value.isoformat()
    return str(value)


def _emit(payload: Any) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2, default=_json_default))


async def _health(identifier: str) -> int:
    runtime = NexusRuntime(identifier=identifier)
    await runtime.start()
    try:
        _emit(asdict(runtime.health()))
        return 0
    finally:
        await runtime.stop()


async def _capabilities(identifier: str) -> int:
    runtime = NexusRuntime(identifier=identifier)
    await runtime.start()
    try:
        _emit({"identifier": identifier, "capabilities": runtime.capabilities.names()})
        return 0
    finally:
        await runtime.stop()


async def _invoke(identifier: str, capability: str, arguments: str) -> int:
    try:
        kwargs = json.loads(arguments)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid --args JSON: {exc}") from exc
    if not isinstance(kwargs, dict):
        raise SystemExit("--args must decode to a JSON object")

    runtime = NexusRuntime(identifier=identifier)
    await runtime.start()
    try:
        result = await runtime.invoke(capability, **kwargs)
        _emit(asdict(result))
        return 0 if result.ok else 2
    finally:
        await runtime.stop()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="projet-unifi",
        description="Public, policy-driven runtime for the Projet-unifi / Nexus ecosystem.",
    )
    parser.add_argument("--identifier", default="Nexus_Public")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("health", help="start the runtime and emit a health snapshot")
    sub.add_parser("capabilities", help="list registered public capabilities")
    invoke = sub.add_parser("invoke", help="invoke one policy-authorized capability")
    invoke.add_argument("capability")
    invoke.add_argument("--args", default="{}", help="JSON object passed as keyword arguments")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.command == "health":
        return asyncio.run(_health(args.identifier))
    if args.command == "capabilities":
        return asyncio.run(_capabilities(args.identifier))
    if args.command == "invoke":
        return asyncio.run(_invoke(args.identifier, args.capability, args.args))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
