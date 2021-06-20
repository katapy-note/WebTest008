# from flask_sqlalchemy import SQLAlchemy
# from DB import create_db
from app import db


# db = SQLAlchemy(app)
# db = create_db()

class Item(db.Model):
    __tablename__ = 'items'
    item_name = db.Column(db.Text, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
