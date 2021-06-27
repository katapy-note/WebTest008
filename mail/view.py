from flask import Blueprint, request
from flask_mail import Mail

from mail import transmitter
from mail.models import mail_model
from app import app

view = Blueprint('mail', __name__)
_mail = Mail(app)
transmitter = transmitter.mail_transmitter()


@view.route("/mail", methods=["POST"])
def mail():
    try:
        model = mail_model(
            request.form["usermail"],
            request.form["subject"],
            request.form["message"]
        )
        transmitter.send(model)

        return "send mail"

    except:
        return "mail error"
