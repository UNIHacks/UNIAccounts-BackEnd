import uuid

from sqlalchemy_utils import Timestamp, UUIDType

from config.database import db


class BaseModelClass(Timestamp, db.Model):
    __abstract__ = True
    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    is_removed = db.Column(db.Boolean, nullable=False, default=False)
