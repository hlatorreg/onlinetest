from flask_restx.reqparse import RequestParser
from flask_restx import Model
from flask_restx.fields import Integer, Nested, String, List, DateTime, Float
from flask_restx.inputs import datetime_from_iso8601

vaccination_reqparser = RequestParser(bundle_errors=True)
vaccination_reqparser.add_argument(
    name="rut", type=str, location="json", required=True, nullable=False
)
vaccination_reqparser.add_argument(
    name="dose", type=float, location="json", required=True, nullable=False
)
vaccination_reqparser.add_argument(
    name="date",
    type=datetime_from_iso8601,
    location="json",
    required=True,
    nullable=False,
)
vaccination_reqparser.add_argument(
    name="drug", type=int, location="json", required=True, nullable=False
)

vaccination_model = Model(
    "vaccination",
    {"id": Integer, "rut": String, "dose": Float, "date": DateTime, "drug": Integer},
)

vaccinations_model = Model(
    "vaccinations", {"vaccinations": List(Nested(vaccination_model))}
)

