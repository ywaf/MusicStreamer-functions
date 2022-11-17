# gcp function to update the name of a user - call after a user is created
import os
import firebase_admin
from firebase_admin import db
from firebase_admin import auth
from firebase_admin import credentials

def update_details(request):
    try:
        # privkey = str(os.getenv('FIREBASE_KEYS')) # firebase priv key - linked to service account with perms - doesnt work as firebase sdk needs json file wtf
        privkey = "/keys/firebase_service_key.json" # gets the json secret from mounted disk - manage in gcp secrets manager
        db_url = str(os.getenv("FIREBASE_DB_URL")) # firebase db url - just get from realtime database tab in firebase console
        print(db_url)
    except Exception as e:
        print("Error Getting env variables!") # this shouldnt ever happen if you have it setup properly
        return_env_variables = {"success" : "false",
             "error" : "error getting env variables"}
        return return_env_variables, 400


    cred = credentials.Certificate(privkey) # use actions secrets!!
    try:
        firebase_admin.initialize_app(cred, {
            'databaseURL': db_url 
        })
    except Exception as e:
        print("firebase app failed to init, or is init already, full traceback: " + str(e))

    try:
        args = request.args
        token = args.get("token")
        nametoset = args.get("name")

    except:
        return_bad_args = {"success" : "false",
             "error" : "bad arguments"}
        return return_bad_args, 400

    try:
        decoded_token = auth.verify_id_token(str(token))
        uid = decoded_token['uid']
    except:
        return_bad_token = {"success" : "false",
             "error" : "bad token"}
        return return_bad_token, 400

    try:
        a = db.reference("/")
        users_ref = a.child('users')
        uid_ref = users_ref.child(str(uid))
        updat = uid_ref.update({'name': str(nametoset)})
        if updat.success():
            return_success = {"success" : "true", "error" : "none"}
            return return_success, 200
        else:
            return_failed = {"success" : "false", "error" : "failed to update"}
            return return_failed, 400

    except Exception as e:
        print("Error " + str(e))
        return_failed = {"success" : "false", "error" : "failed to update"}
        return return_failed, 400




