from __future__ import annotations

from dataclasses import dataclass


class SourceBoundaryError(ValueError):
    """Raised when a source is outside the public publication boundary."""


PUBLIC_SOURCE_REPOSITORIES = frozenset(
    {
        "Wanderer881101/Projet-unifi-",
        "Wanderer881101/Nex-us-V",
        "Wanderer881101/module",
        "Wanderer881101/2-Nex-us-V",
        "Wanderer881101/3-Nex-us-V",
        "Wanderer881101/4-Nex-us-V",
        "Wanderer881101/5-Nex-us-V",
        "Wanderer881101/6-Nex-us-V",
        "Wanderer881101/7-Nex-us-V",
        "Wanderer881101/Book-1-Livre-1",
    }
)


@dataclass(frozen=True, slots=True)
class PublicSource:
    repository: str
    purpose: str

    def validate(self) -> "PublicSource":
        assert_public_source(self.repository)
        return self


def is_public_source(repository: str) -> bool:
    return repository in PUBLIC_SOURCE_REPOSITORIES


def assert_public_source(repository: str) -> None:
    """Reject any repository not explicitly approved for public derivation.

    This policy is intentionally allowlist-based. Access to a repository does not
    imply permission to derive public code or documentation from it.
    """

    if repository not in PUBLIC_SOURCE_REPOSITORIES:
        raise SourceBoundaryError(
            "repository is outside the public-source allowlist; "
            "do not derive public implementation or documentation from it"
        )
