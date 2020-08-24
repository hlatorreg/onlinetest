"""API endpoint definitions for /token namespace."""
from http import HTTPStatus

from flask_restx import Namespace, Resource

from main.api.token.business import process_token_request

token_ns = Namespace(name="token", validate=True)


@token_ns.route("", endpoint="token")
class GetToken(Resource):
    """Handles HTTP requests to URL: /api/v1/token."""

    @token_ns.response(int(HTTPStatus.OK), "Token was successfully created.")
    @token_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    def get(self):
        """Return an access token."""

        return process_token_request()
