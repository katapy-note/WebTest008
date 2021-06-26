from flask import Blueprint, Response, request, render_template
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

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
    db.create_all()
    users = User.query.filter(User.username == username).all()
    user = None
    for u in users:
        if check_password_hash(u.password, password):
            user = u

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
        _password = request.form["password"]
        # パスワードのハッシュ化
        password = generate_password_hash(_password)
        email = request.form["email"]

        # DB
        db.create_all()
        me = User(username=username, password=password, email=email)
        db.session.add(me)
        db.session.commit()
        confirm_signup(me)
        return render_template("auth/login.html")
    except:
        return render_template("auth/signup.html")
