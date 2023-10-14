from app import admin, db
from flask_admin.contrib.sqla import ModelView

from app.models import Building


admin.add_view(ModelView(Building, db.session))
