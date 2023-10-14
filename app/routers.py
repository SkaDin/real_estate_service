import csv
import requests
import click
from datetime import datetime

from requests.exceptions import ConnectionError
from flask import render_template, redirect, url_for, flash

from app import app, db
from app.forms import BuildingForm
from app.models import Building
from constants import OK, FASTAPI_URL


@app.route("/")
def index():
    """Главная страница."""
    return render_template("index.html")


@app.route("/result/<int:pk>", methods=["GET"])
def show_result(pk: int):
    """Отрисовка ответа."""
    building = Building.query.get(pk)
    return render_template("result.html", building=building)


def send_request(number, latitude, longitude):  # noqa
    """Эмуляция запроса на сервер."""
    try:
        response = requests.get(FASTAPI_URL)
        if response.status_code == OK:
            return response.json().get("answer")
    except ConnectionError:
        flash("Сервер недоступен. Попробуйте позже.")
        return None


@app.route("/query", methods=["GET", "POST"])
def create_request():
    """Форма создания запроса и отправка его на сервер."""
    form = BuildingForm()
    if form.validate_on_submit():
        number = form.number.data
        latitude = form.latitude.data
        longitude = form.longitude.data
        result = send_request(number, latitude, longitude)
        if not result:
            return render_template("query.html", form=form)
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
    try:
        response = requests.get(FASTAPI_URL)
        if response.status_code == OK:
            return render_template("ping.html", context="Работает")
    except ConnectionError:
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
    click.echo("Данные загружены")
