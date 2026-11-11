"""End-to-end tests of the read endpoints through the Flask test client."""

from pathlib import Path

import pytest
from flask.testing import FlaskClient

from cafe_api.infrastructure.persistence.seed import _EXAMPLES
from cafe_api.presentation.app_factory import create_app

CAFE_KEYS = {
    "id",
    "name",
    "map_url",
    "img_url",
    "location",
    "seats",
    "has_toilet",
    "has_wifi",
    "has_sockets",
    "can_take_calls",
    "coffee_price",
}


@pytest.fixture
def client(tmp_path: Path) -> FlaskClient:
    app = create_app(f"sqlite:///{tmp_path / 'e2e.db'}", seed=True)
    return app.test_client()


@pytest.fixture
def empty_client(tmp_path: Path) -> FlaskClient:
    app = create_app(f"sqlite:///{tmp_path / 'empty.db'}", seed=False)
    return app.test_client()


def test_random_returns_one_cafe_with_all_keys(client: FlaskClient) -> None:
    response = client.get("/random")

    assert response.status_code == 200
    assert set(response.get_json()["cafe"]) == CAFE_KEYS


def test_all_returns_every_seeded_cafe(client: FlaskClient) -> None:
    response = client.get("/all")

    assert response.status_code == 200
    cafes = response.get_json()["cafes"]
    assert len(cafes) == len(_EXAMPLES)
    assert all(set(cafe) == CAFE_KEYS for cafe in cafes)


def test_search_returns_only_cafes_at_location(client: FlaskClient) -> None:
    response = client.get("/search", query_string={"loc": "Peckham"})

    cafes = response.get_json()["cafes"]
    assert response.status_code == 200
    assert len(cafes) >= 2
    assert {cafe["location"] for cafe in cafes} == {"Peckham"}


def test_search_is_case_insensitive(client: FlaskClient) -> None:
    response = client.get("/search", query_string={"loc": "peckHAM"})

    assert response.status_code == 200
    assert len(response.get_json()["cafes"]) >= 2


def test_search_unknown_location_returns_404_json_error(client: FlaskClient) -> None:
    response = client.get("/search", query_string={"loc": "Atlantis"})

    assert response.status_code == 404
    assert "error" in response.get_json()


def test_search_without_loc_returns_400_json_error(client: FlaskClient) -> None:
    response = client.get("/search")

    assert response.status_code == 400
    assert "error" in response.get_json()


def test_search_with_blank_loc_returns_400_json_error(client: FlaskClient) -> None:
    response = client.get("/search", query_string={"loc": "  "})

    assert response.status_code == 400


def test_random_on_empty_database_returns_404_json_error(
    empty_client: FlaskClient,
) -> None:
    response = empty_client.get("/random")

    assert response.status_code == 404
    assert "error" in response.get_json()
