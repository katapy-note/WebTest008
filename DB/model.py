from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)


class Item(db.Model):
    __tablename__ = 'items'
    item_name = db.Column(db.Text, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
