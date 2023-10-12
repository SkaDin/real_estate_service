from flask import render_template, jsonify

from app import db
from constants import NOT_FOUND, INTERNAL_SERVER_ERROR
from errors import bp


class InvalidAPIUsage(Exception):
    """Кастомный класс ошибок."""

    status_code = NOT_FOUND

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return dict(message=self.message)


@bp.app_errorhandler(InvalidAPIUsage)
def invalid_api_usage(error):
    # Возвращает в ответе текст ошибки и статус-код
    return jsonify(error.to_dict()), error.status_code


@bp.app_errorhandler(NOT_FOUND)
def page_not_found(error):  # noqa
    return render_template("404.html"), NOT_FOUND


@bp.app_errorhandler(INTERNAL_SERVER_ERROR)
def internal_error(error):  # noqa
    db.session.rollback()
    return render_template("500.html"), INTERNAL_SERVER_ERROR
