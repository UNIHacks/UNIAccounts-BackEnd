from config.database import db

from .base_model import BaseModelClass


class ServicesModel(BaseModelClass):
    __tablename__ = "services"
    name = db.Column(db.String(255), nullable=False)
    mother_login = db.Column(db.Boolean, default=False)
    api_key = db.Column(db.String(255), nullable=False)
    jwt_exp = db.Column(db.Integer, nullable=False)
