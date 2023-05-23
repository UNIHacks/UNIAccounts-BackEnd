from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def get_session():
    return db.session()
