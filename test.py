import os
import firebase_admin
from firebase_admin import db
from firebase_admin import auth
from firebase_admin import credentials

#
# cred = credentials.Certificate(a)  # use actions secrets!!
# firebase_admin.initialize_app(cred)
# decoded_token = auth.verify_id_token("")
# uid = decoded_token['uid']
# print(decoded_token)
# print(uid)
#
