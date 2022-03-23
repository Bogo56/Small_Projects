from schemas.base_schema import ma
from models.Users import Users


class ConfirmationSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model=Users
    ##keep relationships between tables
        include_relationships = True
    ##keep foreign keys
        include_fk = True
    ##this command tells marschmello to create a model object after loading the json data
        load_instance = True

