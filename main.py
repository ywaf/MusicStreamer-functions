import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("/Users/leho/Downloads/serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://musicstreamer-sdd-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
uid = "8478hjfe"
a = db.reference("/")
users_ref = a.child('users')
users_ref.set({
    str(uid): {
        'name': '',
        'email': '',
        'profile_picture': '',
        'plan': ''
    }
})


