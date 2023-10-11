import random

from flask import render_template, flash, redirect, url_for

from app import app
from app.forms import BuildingForm
from app.models import Building


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result/<int:pk>", methods=["GET"])
def show_result(pk: int):
    building = Building.query.get(pk)
    if building:
        return render_template("result.html", building=building)
    else:
        flash("Запрос не найден", "danger")
        return redirect(url_for("index"))


def send_request(number, latitude, longitude):
    # Здесь эмулируется отправка запроса на внешний сервер
    # Вместо этого места вставьте код, который отправляет запрос и получает ответ
    # Вместо этого места также можете добавить задержку,
    # чтобы эмулировать обработку запроса на внешнем сервере
    # В данном примере просто возвращается случайное значение true или false
    return random.choice([True, False])


@app.route("/query", methods=["GET", "POST"])
def create_request():
    form = BuildingForm()
    if form.validate_on_submit():
        print("\n\n\n\n\n\n\n\n")
        number = form.number.data
        latitude = form.latitude.data
        longitude = form.longitude.data
        building = Building.query.filter_by(
            number=number,
            latitude=latitude,
            longitude=longitude
        ).first()
        result = send_request(number, latitude, longitude)
        if result:
            return redirect(url_for("show_view", pk=building.id))
        else:
            flash("Данные не найдены", "danger")
    return render_template("query.html", form=form)



