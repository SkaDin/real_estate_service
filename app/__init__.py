from flask import Flask
from flask_bootstrap import Bootstrap
from flask_admin import Admin
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Settings


app = Flask(__name__)
app.config.from_object(Settings)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
admin = Admin(app, name="real_estate_service", template_mode="bootstrap4")

from errors import bp as errors_bp
from admin import bp as admin_bp

app.register_blueprint(errors_bp)
app.register_blueprint(admin_bp)

from . import routers, api_views
