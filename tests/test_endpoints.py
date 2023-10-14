from constants import OK, NOT_FOUND, METHOD_NOT_ALLOWED, CREATED, FASTAPI_URL


def test_get_all_history(client, data_model):  # noqa
    response = client.get("/api/history")
    assert (
        response.status_code == OK
    ), "GET-запрос к эндпоинту '/api/history' возвращает статус `200`"
    response = client.post("/api/history")
    assert (
        response.status_code == METHOD_NOT_ALLOWED
    ), "POST-запрос к эндпоинту '/api/history' запрещён"


def test_get_history_by_number(client, data_model):
    response = client.get(f"/api/history/{data_model.number}")
    assert response.status_code == OK, (
        f"GET-запрос к эндпоинту '/api/history/{data_model.number}' "
        f"возвращает статус `200`"
    )
    response = client.post("/api/history")
    assert response.status_code == METHOD_NOT_ALLOWED, (
        f"POST-запрос к эндпоинту"
        f" '/api/history/{data_model.number}' запрещён"
    )


def test_ping_server(client):
    response = client.get(FASTAPI_URL)
    assert (
        response.status_code == OK
    ), "GET-запрос к эндпоинту '/api/ping' возвращает статус `200`"
    response = client.post("/api/ping")
    assert (
        response.status_code == METHOD_NOT_ALLOWED
    ), "POST-запрос к эндпоинту '/api/ping' запрещён"


def test_get_url_not_found(client):
    response = client.get("/api/id/{unexpected}/")
    assert response.status_code == NOT_FOUND, (
        "В ответ на GET-запрос для получения несуществующей ссылки "
        "возвращается статус `404`."
    )
