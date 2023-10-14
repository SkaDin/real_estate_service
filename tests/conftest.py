import pytest

from dotenv import load_dotenv

load_dotenv()

try:
    from app import app, db
    from app.models import Building
except NameError:
    raise AssertionError(
        "Не обнаружен объект приложения. Создайте экземпляр класса Flask и назовите его app.",
    )
except ImportError as exc:
    if any(obj in exc.name for obj in ["models", "Building"]):
        raise AssertionError("В файле models не найдена модель Building")
    raise AssertionError(
        "Не обнаружен объект класса SQLAlchemy. Создайте его и назовите db."
    )


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


@pytest.fixture
def data_model(_app, query_data):
    building = Building(**query_data, answer="Test answer")
    db.session.add(building)
    db.session.commit()
    return building


@pytest.fixture
def query_data(_app):
    data = {
        "number": 3225003164320,
        "latitude": 53.248659,
        "longitude": 34.355266,
    }
    return data
