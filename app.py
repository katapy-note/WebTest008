
from DB import create_db
from auth import create_auth
from init_app import create_app, create_blueprint


app = create_app()
db = create_db(app=app)
create_blueprint(app=app)
login_manager = create_auth(app=app)


if __name__ == '__main__':
    app.run()
