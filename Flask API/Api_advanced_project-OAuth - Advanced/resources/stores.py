from flask_restful import Resource,reqparse
from flask_jwt_extended import jwt_required
from models.Stores import Stores
from schemas.stores import StoreSchema

store_schema=StoreSchema()
store_schema_list=StoreSchema(many=True)

class StoreList(Resource):

    def get(self):
        stores=Stores.get_all()
    ##serializing with marshmello from object to json
        return store_schema_list.dump(stores)

class Store(Resource):

    def get(self,name):
        store=Stores.get_store(name)

        if store:
            return store_schema.dump(store)
        else:
            return {"msg": "No such store found in the DB"}

    @jwt_required()
    def post(self, name):
        store=Stores.get_store(name)

        if store:
            return {"msg": "We already have that store registered"}, 400
        else:
        ## Marschmello makes it possible to do that, some strange stuff
            Stores(store_name=name).register_item()
            return {"msg": "Store successfully added"}

    @jwt_required()
    def delete(self, name):
        try:
            Stores.delete_item(name)
            return {"msg": "Store successfully deleted"}
        except:
            return {"msg": "No such Store in our DB"}


