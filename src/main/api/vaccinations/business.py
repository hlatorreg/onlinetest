from http import HTTPStatus

from flask_restx import abort

from main.api.token.decorators import token_required
from main.models.vaccination import Vaccination


@token_required
def get_vaccination(id):
    try:
        vac = Vaccination.query.get(id)
    except Exception:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)
    if not vac:
        abort(HTTPStatus.NOT_FOUND)
    return vac


@token_required
def list_vaccinations():
    try:
        vacs = Vaccination.query.all()
        return {"vaccinations": vacs}
    except Exception:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)


@token_required
def create_vaccination(vaccination):
    vac = Vaccination(**vaccination)
    try:
        result, error = vac.save()
    except Exception as exc:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR, str(exc))
    if not result:
        abort(HTTPStatus.BAD_REQUEST, error)
    return result, HTTPStatus.CREATED


@token_required
def update_vaccination(vaccination, id):
    vac = get_vaccination(id)
    vac.rut = vaccination["rut"]
    vac.dose = vaccination["dose"]
    vac.date = vaccination["date"]
    vac.drug = vaccination["drug"]
    try:
        result, error = vac.save()
    except Exception as exc:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR, str(exc))
    if not result:
        abort(HTTPStatus.BAD_REQUEST, error)
    return True, HTTPStatus.OK


@token_required
def delete_vaccination(id):
    vac = Vaccination.query.get(id)
    if not vac:
        abort(HTTPStatus.NOT_FOUND)
    if vac.delete():
        return True, HTTPStatus.NO_CONTENT
    else:
        abort(
            HTTPStatus.INTERNAL_SERVER_ERROR, "Error while deleting vaccination record."
        )
