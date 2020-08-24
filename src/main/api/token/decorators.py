"""Decorators that decode and verify tokens."""
from functools import wraps

from flask import request, current_app

from werkzeug.exceptions import Unauthorized

import jwt


def token_required(f):
    """Execute function if request contains valid access token."""

    @wraps(f)
    def decorated(*args, **kwargs):
        token_payload = _check_access_token()
        if token_payload:
            setattr(decorated, "authorized", token_payload)
        return f(*args, **kwargs)

    return decorated


def _check_access_token():
    """Checks if we have a token, tries to decode it afterwards"""

    token = request.headers.get("Authorization")
    if not token:
        raise Unauthorized(
            description="Unauthorized: No token in headers",
            response=None,
            www_authenticate=None,
        )
    result = _decode_access_token(token)
    if not result:
        raise Unauthorized(
            description="Unauthorized: Invalid token",
            response=None,
            www_authenticate=None,
        )
    return result


def _decode_access_token(access_token):
    """Decodes the token"""

    if isinstance(access_token, bytes):
        access_token = access_token.decode("ascii")
    if access_token.startswith("Bearer "):
        split = access_token.split("Bearer")
        access_token = split[1].strip()
    try:
        key = current_app.config.get("SECRET_KEY")
        payload = jwt.decode(access_token, key, algorithms=["HS256"])
        if "validated" not in payload:
            raise jwt.InvalidTokenError
    except jwt.InvalidTokenError:
        return False
    return access_token
