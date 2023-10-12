from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired


class BuildingForm(FlaskForm):
    """Форма для поиска здания по заданным данным."""

    number = IntegerField(
        "Примерный вид кадастрового номера: ХХ: ХХ: ХХХХХХХ: ХХ",
        validators=[
            DataRequired(message="Поле обязательное!"),
        ],
    )
    latitude = FloatField(
        "Широта",
        validators=[DataRequired(message="Поле обязательное, числовое!")],
    )
    longitude = FloatField(
        "Долгота",
        validators=[
            DataRequired(message="Поле обязательное, числовое!"),
        ],
    )
    submit = SubmitField("Узнать")
