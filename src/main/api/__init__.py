"""API blueprint configuration."""
from flask import Blueprint, current_app
from flask_restx import Api

from main.api.token.endpoints import token_ns
from main.api.drugs.endpoints import drugs_ns
from main.api.vaccinations.endpoints import vaccination_ns

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

api.add_namespace(token_ns, path="/api/1/token")
api.add_namespace(drugs_ns, path="/api/1")
api.add_namespace(vaccination_ns, path="/api/1/vaccination")
