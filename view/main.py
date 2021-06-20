from flask import render_template, Blueprint

from DB.model import Item


main = Blueprint('main', __name__)


@main.route('/')
def hello_world():
    res = Item.query.all()
    return render_template("hello.html", items=res)
