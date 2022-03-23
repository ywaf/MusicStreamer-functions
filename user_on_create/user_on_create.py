import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os



def user_on_create(event, context): # cloud functions entrypoint
    uid = event['uid']
    email = event['email']
    print(str(event))
    try:
        privkey = "/keys/firebase_service_key.json" # gets the json secret from mounted disk - manage in gcp secrets manager
        # privkey = str(os.getenv('FIREBASE_KEYS')) # firebase priv key json - linked to service account with perms
        db_url = str(os.getenv("FIREBASE_DB_URL")) # firebase db url - just get from realtime database tab in firebase console
    except Exception as e:
        print("Error Getting Firebase Key!") # this shouldnt ever happen if you have it setup properly
    cred = credentials.Certificate(privkey) # use actions secrets!!
    try:
        firebase_admin.initialize_app(cred, {
            'databaseURL': db_url # get db url from secrets for security i guess :/
        })
    except:
        print("probably init already")

    a = db.reference("/")
    users_ref = a.child('users')
    users_ref.update({
        str(uid): {
            'name': 'none',
            'email': str(email),
            'plan': 'free'
        }
    })


