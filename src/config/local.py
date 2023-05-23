import os

from .base import BASE_DIR

DATABASE_PATH = os.path.join(BASE_DIR, "mydatabase.db")
SQLALCHEMY_DATABASE_URI = "sqlite:///" + DATABASE_PATH
