from flask_restful import Resource
from flask import url_for,session,request,jsonify
from oauth import google,oa
from models.Users import Users
from schemas.users import UserSchema
from flask_jwt_extended import create_access_token,create_refresh_token


user_schema=UserSchema()

class GoogleLogin(Resource):

##This is the entry url(endpoint) where the user will be redirected to Google for authentication

    def get(self):
        redirect_url = url_for("oauth_authorized",_external=True)
        ## This method starts the flow and redirects the user from google to the url after seccessfull authentication
        return google.authorize_redirect(redirect_url)



class GoogleAuthorized(Resource):

##This is where the user gets redirected after authentication from Google. We collect the response and use the user_info
    def get(self):
        ##Does the complicated stuff of exchanging authorization token for acccess token from the Google Resource Server
        # but since Google Oauth2 uses OpenID standart (giving basic user info directly with the access token)
        # we don't use the access token to access resources on the server(we only need the user name and email), instead we just parse the token_id in the request
        # and take the user info from there#
        token=google.authorize_access_token()
        resp=google.get('https://www.googleapis.com/calendar/v3/calendars/actioncoachbot@gmail.com/events',token=token)
        resp.raise_for_status()
        calendars = resp.json().get('items')
        return {"msg":calendars}

