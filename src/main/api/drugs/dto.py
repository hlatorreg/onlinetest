from flask_restx.reqparse import RequestParser
from flask_restx import Model
from flask_restx.fields import Integer, Nested, String, List

drug_reqparser = RequestParser(bundle_errors=True)
drug_reqparser.add_argument(
    name="name", type=str, location="json", required=True, nullable=False
)
drug_reqparser.add_argument(
    name="code", type=str, location="json", required=True, nullable=False
)
drug_reqparser.add_argument(
    name="description", type=str, location="json", required=True, nullable=False
)

drug_model = Model(
    "drug", {"id": Integer, "name": String, "code": String, "description": String}
)

drugs_model = Model("drugs", {"drugs": List(Nested(drug_model))})

