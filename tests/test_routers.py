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


def test_page_create_request(client):
    response = client.get("/query")
    assert (
        response.status_code == OK
    ), "GET-запрос к эндпоинту '/query' должен возвращать статус `200`."
    assert (
        b"form" in response.data
    ), "Нет формы в контексте страницы '/query'."

    response = client.post(
        "/query",
        data={
            "number": 3225003164320,
            "latitude": 53.248659,
            "longitude": 34.35526,
        },
    )
    assert (
        response.status_code == FOUND
    ), "После отправки формы страница '/query' должна возвращать статус `302`."
    query_data = Building.query.filter_by(number=3225003164320).first()

    assert (
        query_data.id
    ), "После отправки формы в базе данных должна создаваться новая запись."


def test_page_show_result(client):
    response = client.get(f"/result/1")
    assert (
        response.status_code == OK
    ), "GET-запрос к эндпоинту '/show_result' должен возвращать статус `200`"
    response = client.post("/result/1")
    assert (
        response.status_code == METHOD_NOT_ALLOWED
    ), "POST-запрос к эндпоинту `/result` запрещён"


def test_page_ping(client):
    response = client.get("/ping")
    assert (
        response.status_code == OK
    ), "GET-запрос к эндпоинту '/ping' должен возвращать статус `200`"
    response = client.post("/ping")
    assert (
        response.status_code == METHOD_NOT_ALLOWED
    ), "POST-запрос к эндпоинту `/ping` запрещён"


def test_404(client):
    got = client.get("/unexpected")
    assert (
        got.status_code == NOT_FOUND
    ), "При обращении к несуществующей странице возвращается статус `404`"
