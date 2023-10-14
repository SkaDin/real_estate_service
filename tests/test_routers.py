from app.models import Building
from constants import OK, NOT_FOUND, METHOD_NOT_ALLOWED, FOUND


def test_page_index_get(client):
    response = client.get("/")
    assert (
        response.status_code == OK
    ), "GET-запрос к главной странице должен возвращать статус `200`."
    response = client.post("/")
    assert (
        response.status_code == METHOD_NOT_ALLOWED
    ), "POST-запрос к главной странице запрещён"


def test_page_create_request(client, data_model):
    response = client.get("/query")
    assert (
        response.status_code == OK
    ), "GET-запрос к странице '/query' должен возвращать статус `200`."
    assert (
        b"form" in response.data
    ), "Нет формы в контексте страницы '/query'."
    data = Building.query.filter_by(id=data_model.id).first()
    assert (
        data.id
    ), "После отправки формы в базе данных должна создаваться новая запись."


def test_page_show_result(client, data_model):
    response = client.get(f"/result/{data_model.id}")
    assert (
        response.status_code == OK
    ), "GET-запрос к странице '/show_result' должен возвращать статус `200`"
    response = client.post(f"/result/{data_model.id}")
    assert (
        response.status_code == METHOD_NOT_ALLOWED
    ), "POST-запрос к странице `/result` запрещён"


def test_page_ping(client):
    response = client.get("/ping")
    assert (
        response.status_code == OK
    ), "GET-запрос к странице '/ping' должен возвращать статус `200`"
    response = client.post("/ping")
    assert (
        response.status_code == METHOD_NOT_ALLOWED
    ), "POST-запрос к странице `/ping` запрещён"


def test_404(client):
    got = client.get("/unexpected")
    assert (
        got.status_code == NOT_FOUND
    ), "При обращении к несуществующей странице возвращается статус `404`"
