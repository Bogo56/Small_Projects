from schemas.base_schema import ma
from models.Stores import Stores


class StoreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Stores
    ##keep relationships between tables
        include_relationships =True
    ##keep foreign keys
        include_fk = True
    ##this command tells marschmello to create a model object after loading the json data
        load_instance = True

    ## Don't want ot display the items(relationship) in the .dump response
    items=ma.auto_field("items",load_only=True)