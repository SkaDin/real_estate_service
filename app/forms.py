from flask_wtf import FlaskForm
from wtforms import SubmitField, DecimalField, IntegerField, StringField
from wtforms.validators import DataRequired


class BuildingForm(FlaskForm):
    """Форма для поиска здания по заданным данным."""

    number = IntegerField(
        "Примерный вид кадастрового номера: ХХ: ХХ: ХХХХХХХ: ХХ",
        validators=[
            DataRequired(message="Поле обязательное!"),
        ]
    )
    latitude = StringField(
        "Широта",
        validators=[
            DataRequired(message="Поле обязательное!"),
        ]
    )
    longitude = StringField(
        "Долгота",
        validators=[
            DataRequired(message="Поле обязательное!"),
        ]
    )
    submit = SubmitField("Узнать")
