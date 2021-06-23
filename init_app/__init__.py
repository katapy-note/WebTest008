import os

from flask import Flask


def create_app():
    app = Flask(__name__)
    db_uri = os.environ.get('DATABASE_URL') or "postgresql://localhost/testDB"
    db_uri = db_uri.replace('postgres:', 'postgresql:')  # postgresだとエラーになる
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

    app.secret_key = 'xxxxyyyyyzzzzz'

    return app


def create_blueprint(app):
    # blueprint for auth routes in our app
    from view.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from auth.view import view as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from mail.view import view as mail_blueprint
    app.register_blueprint(mail_blueprint)
