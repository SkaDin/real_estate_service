from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, StringField
from wtforms.validators import DataRequired, Regexp


class BuildingForm(FlaskForm):
    """Форма для поиска здания по заданным данным."""

    number = IntegerField(
        "Примерный вид кадастрового номера: 3228003164320 (вводить без символов,только цифры)",
        validators=[
            DataRequired(message="Поле обязательное!"),
        ],
    )
    latitude = StringField(
        "Широта. Примерный вид `53.248659`",
        validators=[
            DataRequired(message="Поле обязательное"),
            Regexp(r"^-?\d{1,2}+.\d{6}$", message="Некорректный формат"),
        ],
    )
    longitude = StringField(
        "Долгота. Примерный вид `34.355260`",
        validators=[
            DataRequired(message="Поле обязательное"),
            Regexp(r"^-?\d{1,2}+.\d{6}$", message="Некорректный формат"),
        ],
    )
    submit = SubmitField("Узнать")
