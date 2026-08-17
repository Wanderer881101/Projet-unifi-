import pytest

from projet_unifi.source_policy import (
    PUBLIC_SOURCE_REPOSITORIES,
    SourceBoundaryError,
    assert_public_source,
    is_public_source,
)


def test_declared_public_sources_are_allowed():
    assert "Wanderer881101/Projet-unifi-" in PUBLIC_SOURCE_REPOSITORIES
    assert "Wanderer881101/Nex-us-V" in PUBLIC_SOURCE_REPOSITORIES
    assert "Wanderer881101/module" in PUBLIC_SOURCE_REPOSITORIES
    for repository in PUBLIC_SOURCE_REPOSITORIES:
        assert is_public_source(repository)
        assert_public_source(repository)


def test_unknown_or_nonapproved_repository_is_rejected():
    repository = "example/private-or-unapproved"
    assert not is_public_source(repository)
    with pytest.raises(SourceBoundaryError):
        assert_public_source(repository)
