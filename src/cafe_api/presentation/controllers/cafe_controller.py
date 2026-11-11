"""HTTP controller of the read endpoints."""

from http import HTTPMethod

from flask import Blueprint, Response, jsonify, request

from cafe_api import constants
from cafe_api.application.use_cases.get_all_cafes import GetAllCafes
from cafe_api.application.use_cases.get_random_cafe import GetRandomCafe
from cafe_api.application.use_cases.search_cafes import SearchCafes
from cafe_api.presentation.contracts.cafe_contract import cafe_body, cafes_body


class CafeReadController:
    """Maps the read requests to use cases and the results to JSON."""

    def __init__(
        self,
        random_cafe: GetRandomCafe,
        all_cafes: GetAllCafes,
        search_cafes: SearchCafes,
    ) -> None:
        """Create the controller.

        @param random_cafe Use case behind GET /random.
        @param all_cafes Use case behind GET /all.
        @param search_cafes Use case behind GET /search.
        """
        self._random_cafe = random_cafe
        self._all_cafes = all_cafes
        self._search_cafes = search_cafes

    def get_random(self) -> Response:
        """Answer GET /random with one cafe."""
        return jsonify(cafe_body(self._random_cafe.execute()))

    def get_all(self) -> Response:
        """Answer GET /all with every cafe."""
        return jsonify(cafes_body(self._all_cafes.execute()))

    def get_search(self) -> Response:
        """Answer GET /search with the cafes at the requested location."""
        location = request.args.get(constants.QUERY_PARAM_LOCATION, "")
        return jsonify(cafes_body(self._search_cafes.execute(location)))

    def create_blueprint(self) -> Blueprint:
        """Build the blueprint that routes the read paths to this controller.

        @return The blueprint to register on the app.
        """
        blueprint = Blueprint(constants.BLUEPRINT_NAME, __name__)
        routes = (
            (constants.ROUTE_RANDOM, self.get_random),
            (constants.ROUTE_ALL, self.get_all),
            (constants.ROUTE_SEARCH, self.get_search),
        )
        for path, view in routes:
            blueprint.add_url_rule(path, view_func=view, methods=[HTTPMethod.GET])
        return blueprint


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
    return CafeReadController(random_cafe, all_cafes, search_cafes).create_blueprint()
