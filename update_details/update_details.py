import os
import firebase_admin
from firebase_admin import db
from firebase_admin import auth

def update_details(request):
    try:
        privkey = str(os.getenv('FIREBASE_KEYS')) # firebase priv key json - linked to service account with perms
        db_url = str(os.getenv("FIREBASE_DB_URL")) # firebase db url - just get from realtime database tab in firebase console
    except Exception as e:
        print("Error Getting env variables!") # this shouldnt ever happen if you have it setup properly

    args = request.args
    print(args)

    if db_url in args:
        print("found db url in args")
        return "True"
    else:
        print("didnt find db url in args :(")
        return "False"

