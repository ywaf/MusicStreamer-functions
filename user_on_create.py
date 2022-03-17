import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


def user_on_create(event, context): # cloud functions entrypoint
    uid = event['uid']
    email = event['email']
    print(str(event))
    cred = credentials.Certificate("/Users/leho/Downloads/serviceAccountKey.json") # change this!! use actions secrets!!

    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://musicstreamer-sdd-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })

    a = db.reference("/")
    users_ref = a.child('users')
    users_ref.set({
        str(uid): {
            'name': '',
            'email': str(email),
            'profile_picture': 'none',
            'plan': 'free'
        }
    })


