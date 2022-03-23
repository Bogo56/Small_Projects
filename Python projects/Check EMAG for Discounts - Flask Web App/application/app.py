from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from config import DevConfig
from users.routes import users_auth
from items.routes import items
from application.models import User


##Constructing the App using flask-factory pattern

db=MongoEngine()
login_manager=LoginManager()
login_manager.login_view="users_auth.log_in"

def create_app():

    app=Flask(__name__)
    app.config.from_object(DevConfig)

    db.init_app(app)
    login_manager.init_app(app)


    app.register_blueprint(users_auth)
    app.register_blueprint(items)

    @login_manager.user_loader
    def load_user(user_id):
        return User.objects(username=user_id).first()

    return app


if __name__=="__main__":
    app=create_app()
    app.run()



