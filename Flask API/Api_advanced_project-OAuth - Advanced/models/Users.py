from models.base_model import db
from models.Confirmations import Confirmations


class Users(db.Model):

    __tablename__="users"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80),unique=True,nullable=False)
    password=db.Column(db.String(80))
    email=db.Column(db.String(90),unique=True)
    active=db.Column(db.Boolean,default=False)
    confirmation=db.relationship("Confirmations",lazy="dynamic",
                                 cascade="all, delete-orphan",
                                 back_populates="user")

    def register_user(self):
        confirmation= Confirmations(self.name)
        confirmation.register_confirmation()
        confirmation.send_confirmation(self.email)
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_user(cls,name):
        result=cls.query.filter_by(name=name).first()
        return result

    @classmethod
    def del_user(cls, name):
        result = cls.get_user(name)
        db.session.delete(result)
        db.session.commit()

    def update_user(self):
        db.session.commit()


