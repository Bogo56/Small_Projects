from flask import Blueprint,request,jsonify
from flask_jwt_extended import create_access_token,create_refresh_token,jwt_required, get_jwt_identity
from models.Users import Users
from schemas.users import UserSchema
from libs.MailGun import MailGunException

auth=Blueprint("resources",__name__,template_folder="templates")
##Some fancy Stuff for seriliazation of Data(Marshmellow). Basically it integrates with sqlalchemy and creates
# models from the jason request info, it also creates json file from a model input#
user_schema=UserSchema()


@auth.route("/resources",methods=["POST"])
def authenticate():

    data=request.get_json()
    user_data=user_schema.load(data)

    user=Users.get_user(user_data.name)

    if user and user_data.password==user.password:

    #if the user has been authenticated we create an access token, which we would use in all requests after that, which
    # are wrapped in @jwt_required decorator#
        if user.active:
            access_token=create_access_token(identity=user_data.name,fresh=True)
            refresh_token=create_refresh_token(identity=user_data.name)
            return jsonify({"info":{"access_token":access_token,"refresh_token":refresh_token,
                                    "username":user_data.name}}), 200
        else:
            return jsonify({"msg":"Username hasn't been confirmed. Check your e-mail"})
    else:
        return jsonify({"msg":"Bad username or password"}),401


@auth.route("/reg",methods=["POST"])
def register():
    data = request.get_json()
    user=user_schema.load(data)

    if Users.get_user(user.name):
        return jsonify({"msg":"username already taken"}), 404
    try:
        user.register_user()
        return jsonify({"msg":"An activation email has been sent"})
    except MailGunException as e:
        return jsonify({"msg":str(e)}), 500



# @resources.route("/activate/<conf_id>", methods=["GET"])
# def activate(conf_id):
#     user=Users.get_user(conf_id)
#
#     if user:
#         user.active=True
#         user.update_user()
#         return render_template("confirmation_page.html",name=user.name)
#     else:
#         return jsonify({"msg":"No such user in our DB"})


@auth.route("/del",methods=["DELETE"])
@jwt_required(fresh=True)
def delete():
    data = request.get_json()
    user=user_schema.load(data)

    if Users.get_user(user.name):
        Users.del_user(user.name)
        return jsonify({"msg":"User successfully deleted"})
    else:
        return jsonify({"msg":"no such user in our DB"}), 404


@auth.route("/refresh",methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    user=get_jwt_identity()
    new_token=create_access_token(identity=user,fresh=False)
    return jsonify({"access_token":new_token})




