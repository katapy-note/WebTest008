from flask import render_template, Blueprint
from flask_login import login_required

from DB.model import Item

main = Blueprint('main', __name__)


@main.route('/')
@login_required  # ログインしている時だけサイトを閲覧できる
def hello_world():
    res = Item.query.all()
    return render_template("hello.html", items=res)
