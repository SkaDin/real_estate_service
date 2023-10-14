from sqlalchemy import inspect

from app.models import Building


def test_fields():
    inspector = inspect(Building)
    fields = [column.name for column in inspector.columns]
    print(fields)
    assert all(
        field in fields
        for field in [
            "id",
            "number",
            "latitude",
            "longitude",
            "timestamp",
            "answer",
        ]
    ), (
        "В модели не найдены все необходимые поля. "
        "Проверьте модель: в ней должны быть поля id,"
        " number, latitude, longitude, timestamp и answer."
    )
