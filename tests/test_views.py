import pytest

from app.models import Building


def test_index_form_get(client):
    response = client.get("/")
    assert (
        response.status_code == 200
    ), "GET-запрос к главной странице должен возвращать статус `200`."


def test_create_request(client):
    response = client.get("/query")
    assert (
            response.status_code == 200
    ), "GET-запрос к странице '/query' должен возвращать статус `200`."
    assert b'form' in response.data, (
        "Добавьте форму в контекст страницы '/query'."
    )


def test_create_request_post_form(client):
    response = client.post("/query", data={
        "number": 3228003164320,
        "latitude": 53.248659,
        "longitude": 34.35526
    })
    assert response.status_code == 200, (
        "После отправки формы страница '/query' должна возвращать статус '200'."
    )
