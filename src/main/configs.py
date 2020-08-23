import os
import urllib


class DevelopmentConfig:
    """ Base configuration """

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql://{}:{}@{}/{}".format(
        os.getenv("USER"), os.getenv("PASS"), os.getenv("HOST"), os.getenv("DATABASE"),
    )
    DEBUG = True
    SECRET_KEY = os.getenv("SECRET_KEY")
    SWAGGER_UI_DOC_EXPANSION = "list"
    RESTX_MASK_SWAGGER = False
