from flask import Flask
from config import TestConfig
from home.routes import home
from resources.routes import auth
from resources.base_api import api
from flask_jwt_extended import JWTManager
from models.base_model import db
from schemas.base_schema import ma
from oauth import oa
from flask_uploads import configure_uploads, patch_request_class
from libs.image_helper import IMAGE_SET



jwt = JWTManager()


##Using Flask Factory pattern


def create_app():
    app = Flask(__name__)
    app.config.from_object(TestConfig)

    jwt.init_app(app)
    api.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    oa.init_app(app)
    ##Using Python_upload for managing and restricting file uploads
    configure_uploads(app,IMAGE_SET)
    ##Restricting file Size. Default is 16 MB
    patch_request_class(app,4*1024*1024) # 4 MB

##Making sure the db tables are created before the first request
    @app.before_first_request
    def create_tables():
        db.create_all()

    app.register_blueprint(home)
    app.register_blueprint(auth)

    return app

if  __name__=="__main__":
    app=create_app()
    app.run()