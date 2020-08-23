"""API blueprint configuration."""
from flask import Blueprint, current_app
from flask_restx import Api

api_bp = Blueprint("api", __name__)
authorizations = {"Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}}

api = Api(
    api_bp,
    version="1.0",
    title="Rest API boilerplate",
    description="23people tecnical test documentation",
    doc="/api/1/ui",
    authorizations=authorizations,
)
