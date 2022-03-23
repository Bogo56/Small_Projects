from flask_restful import Api
from resources.items import Item,ItemsList
from resources.stores import Store,StoreList
from resources.confirmations import Confirmation, ConfirmationByUser
from resources.uploads import ImageUploads,Image
from resources.oauth import GoogleLogin,GoogleAuthorized

api=Api()

api.add_resource(StoreList,"/stores")
api.add_resource(Store,"/store/<string:name>")

api.add_resource(ItemsList,"/items")
api.add_resource(Item,"/item/<string:name>")

api.add_resource(Confirmation,"/activate/<conf_id>",endpoint="api.activate")
api.add_resource(ConfirmationByUser,"/reactivate/<user_name>")

api.add_resource(ImageUploads,"/uploads/image")
api.add_resource(Image,"/uploads")

api.add_resource(GoogleLogin,"/login/google")
api.add_resource(GoogleAuthorized,"/authorized",endpoint="oauth_authorized")
