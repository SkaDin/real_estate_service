import pytest

from constants import OK, NOT_FOUND, METHOD_NOT_ALLOWED, FOUND


def test_history_by_number(client, query_data):
    client.post(
        "/query",
        data=query_data,
    )
    response = client.get("/api/history")
    assert (
        response.status_code == OK
    ), "GET-запрос к эндпоинту '/api/history' возвращает статус `200`"


def test_get_url_not_found(client):
    response = client.get("/api/id/{enexpected}/")
    assert response.status_code == NOT_FOUND, (
        "В ответ на GET-запрос для получения несуществующей ссылки "
        "возвращается статус `404`."
    )
