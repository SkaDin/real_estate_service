import requests as req
from requests.exceptions import ConnectionError

from flask import jsonify, request

from constants import NOT_FOUND, OK, CREATED, BAD_REQUEST, FASTAPI_URL, INTERNAL_SERVER_ERROR
from app import app, db
from app.models import Building
from errors.error_handlers import InvalidAPIUsage


@app.route("/api/history/<int:number>", methods=["GET"])
def get_history_by_number(number: int):
    """Вывод истории по кадастровому номеру."""
    history_objs = Building.query.filter_by(number=number).all()
    history_data = [obj.to_dict() for obj in history_objs]
    if history_data:
        return jsonify({"data": history_data}), OK
    raise InvalidAPIUsage("Запроса с таким номером не было", NOT_FOUND)


@app.route("/api/history", methods=["GET"])
def get_all_history():
    """Вывод истории всех запросов."""
    stories = Building.query.all()
    history_data = [obj.to_dict() for obj in stories]
    if history_data:
        return jsonify({"data": history_data}), OK
    raise InvalidAPIUsage("Запросов не было", NOT_FOUND)


@app.route("/api/query", methods=["GET", "POST"])
def add_query():
    """Запрос к внешнему серверу за информацией/получение ответа."""
    try:
        data = request.get_json()
        answer = req.get(FASTAPI_URL).json().get("answer")
        data["answer"] = answer
        for i in ["number", "latitude", "longitude"]:
            if i not in data:
                raise InvalidAPIUsage(
                    "В запросе отсутствуют обязательные поля", BAD_REQUEST
                )
        # Имитация запроса к внешнему серверу.
        db_obj = Building()
        db_obj.from_dict(data)
        db.session.add(db_obj)
        db.session.commit()
    except ConnectionError:
        raise InvalidAPIUsage(
            "Сервер не работает", INTERNAL_SERVER_ERROR
        )
    return jsonify({"data": db_obj.to_dict()}), CREATED


@app.route("/api/ping", methods=["GET"])
def ping_server():
    """Проверка работоспособности сервера."""
    try:
        response = req.get(FASTAPI_URL)
        if response.status_code == OK:
            return jsonify({"message": "Сервер работает"})
    except ConnectionError:
        raise InvalidAPIUsage(
                "Сервер не работает", INTERNAL_SERVER_ERROR
            )
