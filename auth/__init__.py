from flask_login import LoginManager

from auth.stub import users


def create_auth(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    # login_manager.login_view = 'login'
    login_manager.login_view = 'view.login'

    return login_manager
