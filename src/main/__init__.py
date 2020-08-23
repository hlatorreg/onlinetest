import logging

from flask import Flask, has_request_context, request, render_template
from flask.logging import default_handler
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


cors = CORS()
db = SQLAlchemy()


class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
        else:
            record.url = None

        return super().format(record)


def config_logger():
    formatter = RequestFormatter(
        "[%(asctime)s] level: %(levelname)s message: %(message)s"
    )

    default_handler.setFormatter(formatter)


def register_blueprints(app):
    from main.api import api_bp, api
    from flask_restx import apidoc

    app.register_blueprint(api_bp)


def create_app(app_settings):
    config_logger()
    app = Flask(__name__)

    app.config.from_object(app_settings)

    cors.init_app(app)

    # Databases setup
    db.init_app(app)

    register_blueprints(app)

    return app
