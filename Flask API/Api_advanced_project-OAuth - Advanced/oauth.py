from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
import os


load_dotenv(".env")
client_key=os.environ.get("CLIENT_KEY")
client_secret=os.environ.get("CLIENT_SECRET")

oa=OAuth()

##Creating a Client that can retrieve info from Google profile. This handles all the complicated stuff in the background
google=oa.register("google",
                     request_token_url=None,
                     server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
                     client_id=client_key,
                     client_secret=client_secret,
                     client_kwargs={'scope': 'openid email profile https://www.googleapis.com/auth/calendar'}
                     )
