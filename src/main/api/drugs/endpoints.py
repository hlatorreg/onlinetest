"""API endpoint definitions for /drugs namespace."""
from http import HTTPStatus

from flask_restx import Namespace, Resource

from main.api.drugs.business import (
    list_drugs,
    update_drug,
    create_drug,
    get_drug,
    delete_drug,
)
from main.api.drugs.dto import drug_model, drugs_model, drug_reqparser

drugs_ns = Namespace(name="drugs", validate=True)
drugs_ns.models[drug_model.name] = drug_model
drugs_ns.models[drugs_model.name] = drugs_model


@drugs_ns.route("/drugs", endpoint="drugs")
@drugs_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
@drugs_ns.response(int(HTTPStatus.UNAUTHORIZED), "Unauthorized.")
class Drugs(Resource):
    """Handles HTTP requests to URL: /api/v1/drugs"""

    @drugs_ns.doc(security="Bearer")
    @drugs_ns.response(int(HTTPStatus.OK), "Got drugs array.", drugs_model)
    @drugs_ns.marshal_with(drugs_model)
    def get(self):
        """Return all the drugs."""

        return list_drugs()


@drugs_ns.route("/drugs/<id>", endpoint="drug_by_id")
@drugs_ns.response(int(HTTPStatus.NOT_FOUND), "Drug not found.")
@drugs_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
@drugs_ns.response(int(HTTPStatus.UNAUTHORIZED), "Unauthorized.")
class DrugById(Resource):
    """Handles HTTP requests to URL: /api/v1/drugs/<id>"""

    @drugs_ns.doc(security="Bearer")
    @drugs_ns.response(int(HTTPStatus.OK), "Got drugs array.", drug_model)
    @drugs_ns.marshal_with(drug_model)
    def get(self, id):
        """Return drug by id."""

        return get_drug(id)


@drugs_ns.route("/drug", endpoint="create_drug")
@drugs_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
@drugs_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
@drugs_ns.response(int(HTTPStatus.UNAUTHORIZED), "Unauthorized.")
class CreateDrug(Resource):
    """Handles HTTP requests to URL: /api/v1/drug"""

    @drugs_ns.expect(drug_reqparser)
    @drugs_ns.doc(security="Bearer")
    @drugs_ns.response(int(HTTPStatus.CREATED), "Drug created.", drug_model)
    @drugs_ns.marshal_with(drug_model)
    def post(self):
        """Creates a drug from payload."""

        drug = drug_reqparser.parse_args()

        return create_drug(drug)


@drugs_ns.route("/drug/<id>", endpoint="manipulate_drug")
@drugs_ns.response(int(HTTPStatus.NOT_FOUND), "Drug not found.")
@drugs_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
@drugs_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
@drugs_ns.response(int(HTTPStatus.UNAUTHORIZED), "Unauthorized.")
class DrugManipulation(Resource):
    """Handles HTTP requests to URL: /api/v1/drug/<id>"""

    @drugs_ns.expect(drug_reqparser)
    @drugs_ns.doc(security="Bearer")
    @drugs_ns.response(int(HTTPStatus.OK), "Drug modified.")
    def put(self, id):
        """Updates a drug based on id and payload."""

        drug = drug_reqparser.parse_args()

        return update_drug(drug, id)

    @drugs_ns.doc(security="Bearer")
    @drugs_ns.response(int(HTTPStatus.NO_CONTENT), "Drug deleted.")
    def delete(self, id):
        """Deletes drug by id."""

        return delete_drug(id)
