from datetime import datetime

from app import db


class Building(db.Model):
    """Модель запросов пользователя."""

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.BigInteger, index=True, nullable=False)
    latitude = db.Column(db.String(15), index=True, nullable=False)
    longitude = db.Column(db.String(15), index=True, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now)
    answer = db.Column(db.Text)

    def to_dict(self):
        """Метод-сериализатор."""
        return dict(
            cadastral_number=self.number,
            latitude=self.latitude,
            longitude=self.longitude,
            date=self.timestamp,
            answer_server=self.answer,
        )

    def from_dict(self, data: dict):
        """Метод-десериализатор."""
        for field in ["number", "latitude", "longitude", "answer"]:
            if field in data:
                setattr(self, field, data[field])
