"""HTTP controller of the read endpoints."""

from flask import Blueprint, Response, jsonify, request

from cafe_api import constants
from cafe_api.application.use_cases.get_all_cafes import GetAllCafes
from cafe_api.application.use_cases.get_random_cafe import GetRandomCafe
from cafe_api.application.use_cases.search_cafes import SearchCafes
from cafe_api.presentation.contracts.cafe_contract import cafe_body, cafes_body


def create_cafe_blueprint(
    random_cafe: GetRandomCafe,
    all_cafes: GetAllCafes,
    search_cafes: SearchCafes,
) -> Blueprint:
    """Build the blueprint with the read routes.

    @param random_cafe Use case behind GET /random.
    @param all_cafes Use case behind GET /all.
    @param search_cafes Use case behind GET /search.
    @return The blueprint to register on the app.
    """
    blueprint = Blueprint(constants.BLUEPRINT_NAME, __name__)

    @blueprint.get(constants.ROUTE_RANDOM)
    def get_random() -> Response:
        return jsonify(cafe_body(random_cafe.execute()))

    @blueprint.get(constants.ROUTE_ALL)
    def get_all() -> Response:
        return jsonify(cafes_body(all_cafes.execute()))

    @blueprint.get(constants.ROUTE_SEARCH)
    def get_search() -> Response:
        location = request.args.get(constants.QUERY_PARAM_LOCATION, "")
        return jsonify(cafes_body(search_cafes.execute(location)))

    return blueprint
