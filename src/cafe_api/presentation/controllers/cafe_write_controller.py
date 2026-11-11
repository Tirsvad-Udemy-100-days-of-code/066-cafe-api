"""HTTP controller of the write endpoints."""

from http import HTTPMethod, HTTPStatus

from flask import Blueprint, Response, jsonify, request

from cafe_api import constants
from cafe_api.application.use_cases.add_cafe import AddCafe
from cafe_api.application.use_cases.delete_cafe import DeleteCafe
from cafe_api.application.use_cases.update_coffee_price import UpdateCoffeePrice
from cafe_api.presentation.contracts.cafe_contract import (
    cafe_body,
    message_body,
    parse_new_cafe,
)


class CafeWriteController:
    """Maps the write requests to use cases and the results to JSON."""

    def __init__(
        self,
        add_cafe: AddCafe,
        update_price: UpdateCoffeePrice,
        delete_cafe: DeleteCafe,
    ) -> None:
        """Create the controller.

        @param add_cafe Use case behind POST /add.
        @param update_price Use case behind PATCH /update-price/<id>.
        @param delete_cafe Use case behind DELETE /report-closed/<id>.
        """
        self._add_cafe = add_cafe
        self._update_price = update_price
        self._delete_cafe = delete_cafe

    def post_add(self) -> tuple[Response, int]:
        """Answer POST /add with the created cafe and status 201."""
        data = parse_new_cafe(request.get_json(silent=True))
        body = cafe_body(self._add_cafe.execute(data))
        return jsonify(body), HTTPStatus.CREATED.value

    def patch_update_price(self, cafe_id: int) -> Response:
        """Answer PATCH /update-price/<id> with the updated cafe."""
        new_price = request.args.get(constants.QUERY_PARAM_NEW_PRICE, "")
        return jsonify(cafe_body(self._update_price.execute(cafe_id, new_price)))

    def delete_report_closed(self, cafe_id: int) -> Response:
        """Answer DELETE /report-closed/<id> after the API key is checked."""
        api_key = request.headers.get(constants.HEADER_API_KEY)
        self._delete_cafe.execute(api_key, cafe_id)
        return jsonify(message_body(constants.MSG_CAFE_DELETED))

    def create_blueprint(self) -> Blueprint:
        """Build the blueprint that routes the write paths to this controller.

        @return The blueprint to register on the app.
        """
        blueprint = Blueprint(constants.BLUEPRINT_NAME_WRITE, __name__)
        routes = (
            (constants.ROUTE_ADD, self.post_add, HTTPMethod.POST),
            (constants.ROUTE_UPDATE_PRICE, self.patch_update_price, HTTPMethod.PATCH),
            (
                constants.ROUTE_REPORT_CLOSED,
                self.delete_report_closed,
                HTTPMethod.DELETE,
            ),
        )
        for path, view, method in routes:
            blueprint.add_url_rule(path, view_func=view, methods=[method])
        return blueprint


def create_cafe_write_blueprint(
    add_cafe: AddCafe,
    update_price: UpdateCoffeePrice,
    delete_cafe: DeleteCafe,
) -> Blueprint:
    """Build the blueprint with the write routes.

    @param add_cafe Use case behind POST /add.
    @param update_price Use case behind PATCH /update-price/<id>.
    @param delete_cafe Use case behind DELETE /report-closed/<id>.
    @return The blueprint to register on the app.
    """
    return CafeWriteController(add_cafe, update_price, delete_cafe).create_blueprint()
