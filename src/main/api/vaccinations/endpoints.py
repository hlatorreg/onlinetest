"""API endpoint definitions for /vaccination namespace."""
from http import HTTPStatus

from flask_restx import Namespace, Resource

from main.api.vaccinations.business import (
    list_vaccinations,
    create_vaccination,
    get_vaccination,
    update_vaccination,
    delete_vaccination,
)

from main.api.vaccinations.dto import (
    vaccination_model,
    vaccinations_model,
    vaccination_reqparser,
)


vaccination_ns = Namespace(name="vaccination", validate=True)
vaccination_ns.models[vaccination_model.name] = vaccination_model
vaccination_ns.models[vaccinations_model.name] = vaccinations_model


@vaccination_ns.route("", endpoint="vaccination")
@vaccination_ns.response(
    int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error."
)
@vaccination_ns.response(int(HTTPStatus.UNAUTHORIZED), "Unauthorized.")
class Vaccination(Resource):
    """Handles HTTP requests to URL: /api/v1/vaccination"""

    @vaccination_ns.doc(security="Bearer")
    @vaccination_ns.response(
        int(HTTPStatus.OK), "Got vaccination array.", vaccinations_model
    )
    @vaccination_ns.marshal_with(vaccinations_model)
    def get(self):
        """Return all the vaccination."""

        return list_vaccinations()

    @vaccination_ns.expect(vaccination_reqparser)
    @vaccination_ns.doc(security="Bearer")
    @vaccination_ns.response(
        int(HTTPStatus.CREATED), "vaccination created.", vaccination_model
    )
    @vaccination_ns.marshal_with(vaccination_model)
    def post(self):
        """Creates a vaccination from payload."""

        vaccination = vaccination_reqparser.parse_args()

        return create_vaccination(vaccination)


@vaccination_ns.route("/<id>", endpoint="vaccination_by_id")
@vaccination_ns.response(int(HTTPStatus.NOT_FOUND), "Vaccination not found.")
@vaccination_ns.response(
    int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error."
)
@vaccination_ns.response(int(HTTPStatus.UNAUTHORIZED), "Unauthorized.")
class VaccinationById(Resource):
    """Handles HTTP requests to URL: /api/v1/vaccination/<id>"""

    @vaccination_ns.doc(security="Bearer")
    @vaccination_ns.response(
        int(HTTPStatus.OK), "Got vaccination array.", vaccination_model
    )
    @vaccination_ns.marshal_with(vaccination_model)
    def get(self, id):
        """Return vaccination by id."""

        return get_vaccination(id)

    @vaccination_ns.expect(vaccination_reqparser)
    @vaccination_ns.doc(security="Bearer")
    @vaccination_ns.response(int(HTTPStatus.OK), "vaccination modified.")
    def put(self, id):
        """Updates a vaccination based on id and payload."""

        vaccination = vaccination_reqparser.parse_args()

        return update_vaccination(vaccination, id)

    @vaccination_ns.doc(security="Bearer")
    @vaccination_ns.response(int(HTTPStatus.NO_CONTENT), "vaccination deleted.")
    def delete(self, id):
        """Deletes vaccination by id."""

        return delete_vaccination(id)

