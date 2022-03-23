from flask_restful import Resource
from models.Confirmations import Confirmations
from models.Users import Users
from libs.MailGun import MailGunException



class Confirmation(Resource):

    def get(self,conf_id):
        confirmation=Confirmations.getby_id(conf_id)

        if confirmation:
            if confirmation.confirmed:
                return {"msg":"Confirmation link already active"}, 400
            if confirmation.expired:
                return {"msg":"Confirmation link has expired. Please create a new one"}, 400
            try:
            ##Confirmation Model has access to the User model trough the relationship in it "user"
                confirmation.user.active=True
                confirmation.confirmed=True
                confirmation.user.update_user()
                confirmation.update_confirmation()
                return {"msg":"Email successfully activated"}, 200
            except MailGunException as e:
                return {"msg":str(e)}, 500
            except:
                return {"msg":"Sending Failed"}, 500
        else:
            return {"msg":"Please check if confirmation mail was sent to you first and activate it"}, 404


class ConfirmationByUser(Resource):

    def post(self,user_name):
        user=Users.get_user(user_name)

        if not user:
            return {"msg":"No such user in our DB"}, 400
        if user:
            if user.active:
                return {"msg":"User is already activated"}, 400
            else:
                user.confirmation[0].resend_confirmation()
                return {"msg":"An activation link has been sent to your email"}