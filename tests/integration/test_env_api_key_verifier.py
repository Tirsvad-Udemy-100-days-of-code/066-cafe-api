"""Integration tests of the API key check against the process environment."""

import pytest

from cafe_api import constants
from cafe_api.infrastructure.config.api_key_verifier import EnvApiKeyVerifier

TEST_KEY = "integration-test-key"


def test_is_valid_accepts_key_equal_to_environment_value(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv(constants.ENV_API_KEY, TEST_KEY)

    assert EnvApiKeyVerifier().is_valid(TEST_KEY) is True


@pytest.mark.parametrize("key", ["other-key", "", None, TEST_KEY + "x"])
def test_is_valid_rejects_wrong_or_missing_key(
    monkeypatch: pytest.MonkeyPatch, key: str | None
) -> None:
    monkeypatch.setenv(constants.ENV_API_KEY, TEST_KEY)

    assert EnvApiKeyVerifier().is_valid(key) is False


def test_is_valid_rejects_every_key_when_variable_is_unset(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv(constants.ENV_API_KEY, raising=False)

    assert EnvApiKeyVerifier().is_valid(TEST_KEY) is False
    assert EnvApiKeyVerifier().is_valid("") is False


def test_is_valid_rejects_every_key_when_variable_is_empty(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv(constants.ENV_API_KEY, "")

    assert EnvApiKeyVerifier().is_valid("") is False
    assert EnvApiKeyVerifier().is_valid(TEST_KEY) is False


def test_is_valid_handles_non_ascii_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(constants.ENV_API_KEY, "nøgle-test")

    assert EnvApiKeyVerifier().is_valid("nøgle-test") is True
