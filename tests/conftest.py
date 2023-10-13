import pytest

from dotenv import load_dotenv

from app import app, db

load_dotenv()


@pytest.fixture()
def default_app():
    with app.app_context():
        yield app


@pytest.fixture
def _app():
    with app.app_context():
        app.config.update(
            {
                "TESTING": True,
                "WTF_CSRF_ENABLED": False,
            }
        )
        db.create_all()
        yield app
        db.drop_all()
        db.session.close()


@pytest.fixture
def client(_app):
    return _app.test_client()
