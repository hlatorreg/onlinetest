from http import HTTPStatus

from flask_restx import abort
from flask import jsonify

from main.api.token.decorators import token_required
from main.models.drug import Drug


@token_required
def get_drug(id):
    try:
        drug = Drug.query.get(id)
    except Exception:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)
    if drug:
        return drug
    else:
        abort(HTTPStatus.NOT_FOUND)


@token_required
def list_drugs():
    try:
        drugs = Drug.query.all()
        return {"drugs": Drug.query.all()}
    except Exception:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)


@token_required
def create_drug(drug):
    d = Drug(name=drug["name"], code=drug["code"], description=drug["description"])
    if d.save():
        return d, HTTPStatus.CREATED
    else:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR, "Drug code already exists.")


@token_required
def update_drug(drug, id):
    d = Drug.query.get(id)
    if not d:
        abort(HTTPStatus.NOT_FOUND)
    d.name = drug["name"]
    d.code = drug["code"]
    d.description = drug["description"]
    if d.save():
        return True, HTTPStatus.OK
    else:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR, "Drug code already exists.")


@token_required
def delete_drug(id):
    d = Drug.query.get(id)
    if not d:
        abort(HTTPStatus.NOT_FOUND)
    if d.delete():
        return True, HTTPStatus.NO_CONTENT
    else:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR, "Error while deleting drug record.")
