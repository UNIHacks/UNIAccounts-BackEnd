# External Packages
from flask import Flask
from flask_migrate import Migrate

import config.base as CONFIG
from api.v1.routers.core import views_core
from api.v1.routers.user_services import views_user_services

# Local Packages
from api.v1.routers.users import views_users
from config.database import db

app = Flask(__name__)
app.register_blueprint(views_users)
app.register_blueprint(views_user_services)
app.register_blueprint(views_core)


app.config["SQLALCHEMY_DATABASE_URI"] = CONFIG.SQLALCHEMY_DATABASE_URI
app.config["DATABASE_PATH"] = CONFIG.BASE_DIR
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)
