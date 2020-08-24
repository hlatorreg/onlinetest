"""Global pytest fixtures."""
import pytest

from main import create_app
from main import db as database
from main.models.drug import Drug
from main.models.vaccination import Vaccination


@pytest.fixture
def app():
    app = create_app("main.configs.DevelopmentConfig")
    return app


@pytest.fixture
def drug():
    d = Drug(name="Drug", code="test", description="description")
    return d


@pytest.fixture
def vaccination():
    v = Vaccination()
    return v
