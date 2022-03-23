import mongoengine as engine
from flask_bcrypt import Bcrypt
from flask_login import UserMixin


##Using MongoEngine as ORM to create Models for connecting to the DB

class Items(engine.EmbeddedDocument):

    url=engine.StringField()
    price=engine.IntField()
    item_image=engine.StringField()
    new_price=engine.ListField()


##Integrating Flask-Login and The Model structure
class User(UserMixin,engine.Document):

    username = engine.StringField(required=True)
    email = engine.StringField()
    password = engine.BinaryField()
    items = engine.ListField()
    items_info = engine.EmbeddedDocumentListField(Items)

    def get_id(self):
        return self.username

    @staticmethod
    def check_password(username, password):
        user_pass=User.objects(username=username).get()["password"]
        checked_pass=Bcrypt().check_password_hash(pw_hash=user_pass,
                                                password=password)

        return checked_pass

    @staticmethod
    def check_user(username):
        username=User.objects(username=username).first()

        return username




