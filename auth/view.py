from flask import Blueprint, Response, request, abort, render_template, session
from flask_login import login_required, login_user, logout_user

from app import db
from auth.models import User
from mail.auth_mail import confirm_signup

view = Blueprint('view', __name__)


# ログインしないと表示されないパス
@view.route('/protected/')
@login_required
def protected():
    return Response('''
    protected<br />
    <a href="/logout/">logout</a>
    ''')


# ログアウトパス
@view.route('/logout/')
@login_required
def logout():
    logout_user()
    return Response('''
    logout success!<br />
    <a href="/login/">login</a>
    ''')


# ログインパス
@view.route('/login/', methods=["GET"])
def login():
    return render_template("auth/login.html")


@view.route('/login', methods=["POST"])
def login_post():
    username = request.form["username"]
    password = request.form["password"]
    print("name: " + username)
    # ユーザーチェック
    user = User.query.filter_by(username=username, password=password).first()
    if user is not None:
        # ユーザーが存在した場合はログイン
        login_user(user)
        return Response('''
                            login success!<br />
                            <a href="/protected/">protected</a><br />
                            <a href="/logout/">logout</a>
                            ''')
    else:
        return render_template("auth/login.html")


@view.route('/signup', methods=["GET"])
def signup():
    return render_template("auth/signup.html")


@view.route('/signup', methods=["POST"])
def signup_post():
    try:
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        me = User(username=username, password=password, email=email)
        db.session.add(me)
        db.session.commit()
        confirm_signup(me)
        return render_template("auth/login.html")
    except:
        return render_template("auth/signup.html")
