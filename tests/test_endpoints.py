from constants import OK, NOT_FOUND, METHOD_NOT_ALLOWED, CREATED


def test_get_all_history(client, query_data):
    client.post(
        "/query",
        data=query_data,
    )
    response = client.get("/api/history")
    assert (
        response.status_code == OK
    ), "GET-запрос к эндпоинту '/api/history' возвращает статус `200`"
    response = client.post("/api/history")
    assert (
        response.status_code == METHOD_NOT_ALLOWED
    ), "POST-запрос к эндпоинту '/api/history' запрещён"


def test_get_history_by_number(client, data_model, query_data):
    client.post(
        "/query",
        data=query_data,
    )
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
    response = client.get("/api/ping")
    assert (
        response.status_code == OK
    ), "GET-запрос к эндпоинту '/api/ping' возвращает статус `200`"
    response = client.post("/api/ping")
    assert (
        response.status_code == METHOD_NOT_ALLOWED
    ), "POST-запрос к эндпоинту '/api/ping' запрещён"


def test_add_query(client, query_data):
    response = client.post("/api/query", json=query_data)
    assert (
        response.status_code == CREATED
    ), "POST-запрос на эндпоинт '/api/query' возвращает статус 201"
    for i in ["number", "latitude", "longitude"]:
        if i not in query_data:
            raise AssertionError(
                "Если в запросе отсутствуют поля" " , должно быть исключение"
            )


def test_get_url_not_found(client):
    response = client.get("/api/id/{unexpected}/")
    assert response.status_code == NOT_FOUND, (
        "В ответ на GET-запрос для получения несуществующей ссылки "
        "возвращается статус `404`."
    )
