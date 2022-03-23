from flask_restful import Resource,request
from flask_jwt_extended import jwt_required, get_jwt_identity
from libs.image_helper import save_file,get_filename,get_filepath,get_all
from schemas.uploads import ImageSchema
from marshmallow.exceptions import ValidationError
from flask_uploads import UploadNotAllowed,IMAGES
import os


class ImageUploads(Resource):

    @jwt_required()
    def post(self):

        try:
            ##Getting data trough werkzeug request object and loading it to the schema
            data = ImageSchema().load(request.files)
            user_id = get_jwt_identity()
            ##Every folder takes the name of the current user(get user name from jwt)
            folder = f"user_{user_id}"
            #Saving file trough simple library that I created which implements flask_upload library.
            # The Library <flask_upload> takes care that the upload files are of proper size and format before saving.
            # Also creates a common pattern for upload location for same file types(images,pdf etc.)#
            file = save_file(data["image"], folder)
            return {"msg": f"Your file <{file}> has been uploaded"}
        except ValidationError:
            return{"msg":f"Missing required field <images>"}
        except UploadNotAllowed:
            return{"msg":f"Not an Image file.Supported formats {IMAGES}"}


class Image(Resource):

##Get all files
    @jwt_required()
    def get(self):
        user_id=get_jwt_identity()
        folder=f"user_{user_id}"
        files=[image.name for image in get_all(folder)]
        return {"items":files}

    @jwt_required()
    def delete(self):
        data = request.get_json()
        user_id = get_jwt_identity()
        image = data["image_name"]
        folder = f"user_{user_id}"
    ##using function from the simple library I created for updating files with flask-update
        file_folder = get_filepath(f"{folder}" + f"/{image}")

        try:
            os.remove(file_folder)
            return {"msg":f"item < {image} > successfully deleted"}
        except FileNotFoundError:
            return {"mas":f"< {image} > not found for {user_id}"}





