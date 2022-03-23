from pathlib import Path
from uuid import uuid4

images_path=Path.cwd().joinpath("static","images")

class TestConfig:

    TESTING="True"
    DEBUG="True"
    ENV="development"
    SECRET_KEY=uuid4().hex
    JWT_SECRET_KEY=uuid4().hex
    SQLALCHEMY_DATABASE_URI="sqlite:///models/test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    PROPAGATE_EXCEPTIONS=True
    UPLOADED_IMAGES_DEST = images_path
