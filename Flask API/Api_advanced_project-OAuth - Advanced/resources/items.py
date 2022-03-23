from flask_restful import Resource,reqparse, request
from flask_jwt_extended import jwt_required
from models.Items import Items
from schemas.items import ItemSchema

item_schema_list=ItemSchema(many=True)
item_schema=ItemSchema()

##Using Flask-Restfull Extension to Build the Api structure and interface

class ItemsList(Resource):

     def get(self):
         items=Items.get_all()
         return item_schema_list.dump(items)


class Item(Resource):

    def get(self,name):
        item = Items.get_item(name)

        if item:
            return item_schema.dump(item)
        else:
            return {"msg": "No such item found in the DB"}

##JWT requires that the user has the authentication token(generated at login) to make this request
##The token is being send in the header request trough POSTMAN
##With Post we can only add items and if they don't already exist
    @jwt_required()
    def post(self,name):
        item = Items.get_item(name)

        if item:
            return {"msg":"We already have that item"}
        else:
            data=request.get_json()
            data["item_name"]=name
            item=item_schema.load(data)
            item.register_item()
            return {"msg":"Item successfully added"}

##With Put we can add or update items if they exist already
    def put(self,name):
        data=request.get_json()
        data["item_name"]=name

        item=Items.get_item(name)

        if item:
            item=item_schema.load(data)
            Items.update_item(name,item.price,item.quantity)
            return{"msg":"Item updated"}
        else:
            item=item_schema.load(data)
            item.register_item()
            return{"msg":"Item successfully added"}

    @jwt_required(fresh=True)
    def delete(self,name):
        try:
            Items.delete_item(name)
            return {"msg":"Item successfully deleted"}
        except:
            return {"msg":"No such item in the DB"}




