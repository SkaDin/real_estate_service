import csv
import random
import time
from datetime import datetime

from flask import render_template, flash, redirect, url_for

from app import app, db
from app.forms import BuildingForm
from app.models import Building
from constants import SLEEP


@app.route("/")
def index():
    """Главная страница."""
    return render_template("index.html")


@app.route("/result/<int:pk>", methods=["GET"])
def show_result(pk: int):
    """Отрисовка ответа."""
    building = Building.query.get(pk)
    if building:
        return render_template("result.html", building=building)
    else:
        flash("Запрос не найден", "danger")
        return redirect(url_for("index"))


def send_request(number, latitude, longitude):  # noqa
    """Эмуляция запроса на сервер."""
    time.sleep(SLEEP)  # Задержка запроса(до 60 сек)
    response = random.choice(["True", "False"])
    return response


@app.route("/query", methods=["GET", "POST"])
def create_request():
    """Форма создания запроса и отправка его на сервер."""
    form = BuildingForm()
    if form.validate_on_submit():
        number = form.number.data
        latitude = form.latitude.data
        longitude = form.longitude.data
        result = send_request(number, latitude, longitude)
        building = Building(
            number=number,
            latitude=latitude,
            longitude=longitude,
            answer=result,
        )
        db.session.add(building)
        db.session.commit()
        return redirect(url_for("show_result", pk=building.id))
    return render_template("query.html", form=form)


@app.route("/ping", methods=["GET"])
def check_server():
    """Проверка работоспособности сервера."""
    if send_request(number=None, longitude=None, latitude=None):
        return render_template("ping.html", context="Работает")
    time.sleep(SLEEP)
    return render_template("ping.html", context="Не работает")


@app.cli.command("load_data")
def load_test_data():
    """Создание тестовых данных."""
    db.create_all()
    with open("data.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            timestamp = datetime.strptime(
                row["timestamp"], "%Y-%m-%d%H:%M:%S.%f"  # noqa
            )
            row["timestamp"] = timestamp  # noqa
            data = Building(**row)  # noqa
            db.session.add(data)
            db.session.commit()
