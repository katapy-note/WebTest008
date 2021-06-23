from flask_mail import Mail

import mail
from DB import create_db
from auth import create_auth
from auth.stub import users
from init_app import create_app, create_blueprint

# from mail.view import mail_view

app = create_app()
db = create_db(app=app)
create_blueprint(app=app)
login_manager = create_auth(app=app)
# smtpobj = mail.create_smtpobj()
# mail = Mail(app)


@login_manager.user_loader
def load_user(user_id):
    return users.get(int(user_id))


if __name__ == '__main__':
    app.run()
