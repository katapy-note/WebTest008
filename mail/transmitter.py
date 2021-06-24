import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate


class mail_transmitter():
    def __init__(self):
        self.__from = 'katapy.tennis@gmail.com'

    def init_smtpobj(self):
        self.__smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
        self.__smtpobj.ehlo()
        self.__smtpobj.starttls()
        self.__smtpobj.ehlo()
        self.__smtpobj.login(self.__from, 'ywnagaeefbkgeciw')

    def send(self, model):
        self.init_smtpobj()
        msg = MIMEText(model.body, 'html')
        msg['Subject'] = model.subject
        msg['Date'] = formatdate()
        print(msg)

        self.__smtpobj.sendmail(self.__from, model.to_addr, msg.as_string())
        self.__smtpobj.close()
