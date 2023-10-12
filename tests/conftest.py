import pytest

from dotenv import load_dotenv
from mixer.backend.flask import mixer as _mixer

from app import app

load_dotenv()


@pytest.fixture()
def default_app():
    with app.app_context():
        yield app


@pytest.fixture()
def client(default_app):
    return default_app.test_client()


@pytest.fixture()
def runner(default_app):
    return default_app.test_cli_runner()


@pytest.fixture
def mixer():
    _mixer.init_app(app)
    return _mixer
