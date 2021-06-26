from flask_sqlalchemy import SQLAlchemy


def create_db(app):
    db = SQLAlchemy(app)
    # db.create_all()
    return db
