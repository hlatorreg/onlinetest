"""Business logic for /token API endpoint."""
from datetime import datetime
from http import HTTPStatus

import jwt
from flask import abort, current_app, jsonify
from .decorators import _decode_access_token


def process_token_request():
    try:
        now = datetime.now()
        key = current_app.config.get("SECRET_KEY")
        access_token = jwt.encode(
            dict(validated="yes", iat=now), key, algorithm="HS256"
        )
        _decode_access_token(access_token.decode())
        return _create_auth_successful_response(
            token=access_token.decode(), status_code=HTTPStatus.OK
        )
    except Exception as e:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR, str(e))


def _create_auth_successful_response(token, status_code):
    response = jsonify(token=token)
    response.status_code = status_code
    return response
