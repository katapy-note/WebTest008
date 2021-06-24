from flask_login import LoginManager


def create_auth(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'view.login'

    from auth.models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return login_manager
