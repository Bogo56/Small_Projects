import requests
from flask import request,url_for

##Handling exceptions
class MailGunException(Exception):
    def __init__(self,message):
        super().__init__(message)

class MailGun():
    mailgun_url = "https://api.mailgun.net/v3/sandboxd4bf5d92716f41cd7ecf98.mailgun.org/messages"
    mailgun_key = ""
    from_mail = "Excited User <mailgun@sandboxd4bf5d92716f41c68e9ae8824d7ecf98.mailgun.org>"
    mail_body = "Click this link to activate mail: {}"
    mail_subject = 'Email confirmation'


    @classmethod
    def send_mail(cls,to_mail,conf_id):
        activation_link = request.url_root[:-1] + url_for("api.activate",conf_id=conf_id)

        if cls.mailgun_key is None:
            ##Normally we would use env variables instead of hardcoding stuff
            raise MailGunException("Key is None. Check your Environmental variables")

        response = requests.post(cls.mailgun_url,
                                 auth=("api", cls.mailgun_key),
                                 data={"from": cls.from_mail,
                               "to": to_mail,
                               "subject": cls.mail_subject,
                               "text": cls.mail_body.format(activation_link)})

        if response.status_code !=200:
            message=response.content.decode("UTF-8")
            ##sending the message from Mailgun API error
            message=message.strip()
            raise MailGunException("Error in sending confirmation. {}".format(message))
        return response