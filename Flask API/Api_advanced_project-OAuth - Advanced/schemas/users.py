from schemas.base_schema import ma
from models.Users import Users


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Users
        load_only=("password")
        dump_only=("id")
        load_instance=True





