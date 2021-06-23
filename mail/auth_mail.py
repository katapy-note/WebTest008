from flask import render_template

from mail.models import mail_model
from mail.transmitter import mail_transmitter


def confirm_signup(user):
    usermail = user.email
    subject = "Welcome to " + user.username
    message = render_template("mail/confirm_signup.html", user=user)
    print(message)
    model = mail_model(
        usermail,
        subject,
        message
    )
    transmitter = mail_transmitter()
    transmitter.send(model)
