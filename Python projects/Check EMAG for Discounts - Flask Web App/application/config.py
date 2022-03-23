from dotenv import load_dotenv
from datetime import timedelta
import os

#Using ENV Variables for secret keys
load_dotenv(dotenv_path=".env")
DB_KEY=os.getenv("DB_KEY")
SEC_KEY=os.getenv("SECRET_KEY")


class BaseConfig:

    MONGODB_SETTINGS = {"host":DB_KEY}
    SECRET_KEY= SEC_KEY


class DevConfig(BaseConfig):

    FLASK_ENV="development"
    DEBUG=True
    TESTING=True
    PERMANENT_SESSION_LIFETIME=timedelta(minutes=10)
    TEMPLATES_AUTO_RELOAD = True


class ProdConfig(BaseConfig):

    FLASK_ENV="production"
    DEBUG=False
    TESTING=False
    PERMANENT_SESSION_LIFETIME=timedelta(minutes=10)
    TEMPLATES_AUTO_RELOAD = True






