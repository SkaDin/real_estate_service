from flask import jsonify

from constants import NOT_FOUND, OK
from . import app
from app.models import Building
from errors.error_handlers import InvalidAPIUsage


@app.route("/api/history/<int:number>/", methods=["GET"])
def get_history_by_number(number: int):
    """Вывод истории по кадастровому номеру."""
    history_objs = Building.query.filter_by(number=number).all()
    history_data = [obj.to_dict() for obj in history_objs]
    if history_data:
        return jsonify({"data": history_data}), OK
    raise InvalidAPIUsage(
        "Запроса с таким номером не было", NOT_FOUND
    )


@app.route("/api/history/", methods=["GET"])
def get_all_history():
    """Вывод истории всех запросов."""
    stories = Building.query.all()
    history_data = [obj.to_dict() for obj in stories]
    if history_data:
        return jsonify({"data": history_data}), OK
    raise InvalidAPIUsage(
        "Запросов не было", NOT_FOUND
    )
