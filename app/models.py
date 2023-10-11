from datetime import datetime

from app import db


class Building(db.Model):
    """Модель запросов пользователя."""

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(
        db.BigInteger, unique=True, index=True, nullable=False
    )
    latitude = db.Column(
        db.String, unique=True, nullable=False
    )
    longitude = db.Column(
        db.String, unique=True, nullable=False
    )
    timestamp = db.Column(
        db.DateTime, default=datetime.now
    )
    answer = db.Column(db.Text)
