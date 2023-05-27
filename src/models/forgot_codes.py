from config.database import db

from .base_model import BaseModelClass


class ForgotCodeModel(BaseModelClass):
    __tablename__ = "forgot_codes"
    user_name = db.Column(db.String(255), nullable=False)
    code = db.Column(db.String(255), nullable=False)