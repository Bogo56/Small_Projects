from schemas.base_schema import ma
from models.Items import Items
from models.Stores import Stores

class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Items
    ##keep relationships between tables
        include_relationships =True
    ##keep foreign keys
        include_fk = True
    ##this command tells marschmello to create a model object after loading the json data
        load_instance = True

    ## Don't want ot display the items(relationship) in the .dump response
    store=ma.auto_field("store",load_only=True)