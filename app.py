from DB import create_db
from auth import create_auth
from auth.stub import users
from init_app import create_app, create_blueprint

app = create_app()
db = create_db(app=app)
create_blueprint(app=app)
login_manager = create_auth(app=app)


@login_manager.user_loader
def load_user(user_id):
    return users.get(int(user_id))


if __name__ == '__main__':
    app.run()
