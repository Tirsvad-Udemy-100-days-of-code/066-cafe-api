"""End-to-end tests of the write endpoints through the Flask test client."""

from pathlib import Path
from typing import Any

import pytest
from flask.testing import FlaskClient

from cafe_api import constants
from cafe_api.presentation.app_factory import create_app

TEST_KEY = "e2e-test-key"
KEY_HEADER = {"X-API-Key": TEST_KEY}
WRONG_HEADER = {"X-API-Key": "wrong"}
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


def _payload(**changes: Any) -> dict[str, Any]:
    body: dict[str, Any] = {
        "name": "Written Cafe",
        "map_url": "https://example.com/map",
        "img_url": "https://example.com/img.jpg",
        "location": "Bank",
        "seats": "0-10",
        "has_toilet": True,
        "has_wifi": False,
        "has_sockets": True,
        "can_take_calls": False,
        "coffee_price": "2.80",
    }
    body.update(changes)
    return body


@pytest.fixture
def client(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> FlaskClient:
    monkeypatch.setenv(constants.ENV_API_KEY, TEST_KEY)
    return create_app(f"sqlite:///{tmp_path / 'write.db'}", seed=True).test_client()


def _all_cafes(client: FlaskClient) -> list[dict[str, Any]]:
    cafes: list[dict[str, Any]] = client.get("/all").get_json()["cafes"]
    return cafes


def test_add_returns_201_and_cafe_appears_in_all(client: FlaskClient) -> None:
    before = _all_cafes(client)

    response = client.post("/add", json=_payload())

    assert response.status_code == 201
    cafe = response.get_json()["cafe"]
    assert set(cafe) == CAFE_KEYS
    assert cafe["id"] not in {c["id"] for c in before}
    after = _all_cafes(client)
    assert len(after) == len(before) + 1
    assert cafe in after


def test_add_accepts_missing_and_null_price(client: FlaskClient) -> None:
    body = _payload(name="No Price")
    del body["coffee_price"]
    other = _payload(name="Null Price", coffee_price=None)

    assert client.post("/add", json=body).get_json()["cafe"]["coffee_price"] is None
    assert client.post("/add", json=other).get_json()["cafe"]["coffee_price"] is None


def test_add_returns_400_naming_the_missing_field(client: FlaskClient) -> None:
    body = _payload()
    del body["location"]

    response = client.post("/add", json=body)

    assert response.status_code == 400
    assert "location" in response.get_json()["error"]


@pytest.mark.parametrize("name", ["", "   "])
def test_add_returns_400_when_name_is_blank(client: FlaskClient, name: str) -> None:
    response = client.post("/add", json=_payload(name=name))

    assert response.status_code == 400
    assert "name" in response.get_json()["error"]


@pytest.mark.parametrize("value", ["true", 1, None])
def test_add_returns_400_when_flag_is_not_boolean(
    client: FlaskClient, value: object
) -> None:
    response = client.post("/add", json=_payload(has_wifi=value))

    assert response.status_code == 400
    assert "has_wifi" in response.get_json()["error"]


def test_add_returns_400_when_price_is_not_text(client: FlaskClient) -> None:
    response = client.post("/add", json=_payload(coffee_price=2.5))

    assert response.status_code == 400
    assert "coffee_price" in response.get_json()["error"]


def test_add_returns_400_when_name_already_exists(client: FlaskClient) -> None:
    existing = _all_cafes(client)[0]["name"]

    response = client.post("/add", json=_payload(name=existing))

    assert response.status_code == 400
    assert "error" in response.get_json()


@pytest.mark.parametrize(
    ("data", "content_type"),
    [("not json", "text/plain"), ("{broken", "application/json"), ("", None)],
)
def test_add_returns_400_when_body_is_not_json(
    client: FlaskClient, data: str, content_type: str | None
) -> None:
    response = client.post("/add", data=data, content_type=content_type)

    assert response.status_code == 400
    assert "error" in response.get_json()


def test_add_returns_400_when_json_is_not_an_object(client: FlaskClient) -> None:
    response = client.post("/add", json=["a", "b"])

    assert response.status_code == 400
    assert "error" in response.get_json()


def test_update_price_changes_price_and_all_shows_it(client: FlaskClient) -> None:
    cafe_id = _all_cafes(client)[0]["id"]

    response = client.patch(
        f"/update-price/{cafe_id}", query_string={"new_price": "7.77"}
    )

    assert response.status_code == 200
    assert response.get_json()["cafe"]["coffee_price"] == "7.77"
    shown = next(c for c in _all_cafes(client) if c["id"] == cafe_id)
    assert shown["coffee_price"] == "7.77"


def test_update_price_returns_404_when_id_is_unknown(client: FlaskClient) -> None:
    response = client.patch("/update-price/99999", query_string={"new_price": "1.00"})

    assert response.status_code == 404
    assert "error" in response.get_json()


@pytest.mark.parametrize("query", [{}, {"new_price": ""}, {"new_price": "  "}])
def test_update_price_returns_400_when_new_price_is_missing_or_blank(
    client: FlaskClient, query: dict[str, str]
) -> None:
    cafe_id = _all_cafes(client)[0]["id"]

    response = client.patch(f"/update-price/{cafe_id}", query_string=query)

    assert response.status_code == 400
    assert "error" in response.get_json()


def test_report_closed_deletes_cafe_when_key_is_right(client: FlaskClient) -> None:
    before = _all_cafes(client)
    cafe_id = before[0]["id"]

    response = client.delete(f"/report-closed/{cafe_id}", headers=KEY_HEADER)

    assert response.status_code == 200
    assert response.get_json() == {"message": constants.MSG_CAFE_DELETED}
    after = _all_cafes(client)
    assert len(after) == len(before) - 1
    assert cafe_id not in {c["id"] for c in after}


def test_report_closed_returns_403_when_key_is_wrong(client: FlaskClient) -> None:
    before = _all_cafes(client)
    cafe_id = before[0]["id"]

    response = client.delete(f"/report-closed/{cafe_id}", headers=WRONG_HEADER)

    assert response.status_code == 403
    assert "error" in response.get_json()
    assert len(_all_cafes(client)) == len(before)


def test_report_closed_returns_403_when_key_is_missing(client: FlaskClient) -> None:
    before = _all_cafes(client)
    cafe_id = before[0]["id"]

    response = client.delete(f"/report-closed/{cafe_id}")

    assert response.status_code == 403
    assert len(_all_cafes(client)) == len(before)


def test_report_closed_returns_403_when_key_variable_is_unset(
    client: FlaskClient, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.delenv(constants.ENV_API_KEY)
    cafe_id = _all_cafes(client)[0]["id"]

    with_header = client.delete(f"/report-closed/{cafe_id}", headers=KEY_HEADER)
    empty_header = client.delete(f"/report-closed/{cafe_id}", headers={"X-API-Key": ""})

    assert with_header.status_code == 403
    assert empty_header.status_code == 403


def test_report_closed_returns_404_when_id_is_unknown_and_key_is_right(
    client: FlaskClient,
) -> None:
    response = client.delete("/report-closed/99999", headers=KEY_HEADER)

    assert response.status_code == 404
    assert "error" in response.get_json()


def test_report_closed_returns_403_not_404_when_key_is_wrong_and_id_unknown(
    client: FlaskClient,
) -> None:
    response = client.delete("/report-closed/99999", headers=WRONG_HEADER)

    assert response.status_code == 403


def test_responses_never_contain_the_api_key(client: FlaskClient) -> None:
    response = client.delete("/report-closed/99999", headers=WRONG_HEADER)

    assert TEST_KEY not in response.get_data(as_text=True)
