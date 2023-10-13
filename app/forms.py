from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, StringField
from wtforms.validators import DataRequired, Regexp


class BuildingForm(FlaskForm):
    """Форма для поиска здания по заданным данным."""

    number = IntegerField(
        "Примерный вид кадастрового номера: ХХ: ХХ: ХХХХХХХ: ХХ",
        validators=[
            DataRequired(message="Поле обязательное!"),
        ],
    )
    latitude = StringField(
        "Широта",
        validators=[
            DataRequired(message="Поле обязательное"),
            Regexp(r"^-?\d{1,2}+.\d{6}$", message="Некорректный формат"),
        ],
    )
    longitude = StringField(
        "Долгота",
        validators=[
            DataRequired(message="Поле обязательное"),
            Regexp(r"^-?\d{1,2}+.\d{6}$", message="Некорректный формат"),
        ],
    )
    submit = SubmitField("Узнать")
