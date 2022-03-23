from models.base_model import db
from uuid import uuid4
from time import time
from libs.MailGun import MailGun



class Confirmations(db.Model):

    __tablename__="confirmations"
    id=db.Column(db.String(50), primary_key=True)
    expire_at=db.Column(db.Integer,nullable=False)
    confirmed=db.Column(db.Boolean)
    user_id=db.Column(db.Integer,db.ForeignKey("users.name"),nullable=False)
    user=db.relationship("Users",back_populates="confirmation")

    def __init__(self,user_name):
        self.id=uuid4().hex
        self.expire_at= int(time()) + 180 # + 3 minutes
        self.confirmed=False
        self.user_id=user_name

    def register_confirmation(self):
        db.session.add(self)
        db.session.commit()

    @property
    def expired(self):
        return int(time()) > self.expire_at

    @classmethod
    def getby_id(cls,confirmation_id):
        result=cls.query.filter_by(id=confirmation_id).first()
        return result

    def force_expire(self):
        if not self.expired:
            self.expire_at = int(time())
            db.session.commit()

    def update_confirmation(self):
        db.session.commit()

    def send_confirmation(self,email):
        MailGun.send_mail(email, conf_id=self.id)

    def resend_confirmation(self):
        self.id=uuid4().hex
        self.confirmed=False
        self.expire_at = int(time()) + 180
        MailGun.send_mail(self.user.email,self.id)
        db.session.commit()