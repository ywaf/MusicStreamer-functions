import firebase_admin
import flask
import functions_framework
import json
from flask import Flask
from firebase_admin import auth
from flask import send_file
from flask import request
import os
from firebase_admin import credentials
from firebase_admin import db
from google.cloud import storage

app = flask.Flask(__name__)

def getobject(id):


@app.route("/test", methods=['GET'])
def songs():
    try: # shamelessly ripped from oncreate function
        privkey = "a.json" # gets the json secret from mounted disk - manage in gcp secrets manager
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
            'databaseURL': "https://musicstreamer-sdd-default-rtdb.asia-southeast1.firebasedatabase.app"  # get db url from secrets for security i guess :/
        })
    except Exception as e:
        print("firebase app failed to init, or is init already, full traceback: " + str(e))

    headers = request.headers
    try:
        authtoken = headers.get("Authorization")
        print(authtoken)
        if authtoken == "" or authtoken is None:
            return "no auth provided :kekw:"
        try:

            decoded_token = auth.verify_id_token(authtoken)
            # token is good
            uid = decoded_token['uid'] # get uid from jwt
            # get the song from gcp bucket


        except Exception as e:
            print(e)
            return "invalid token"
        return uid
    except:
        print("Failure Getting Headers")
        return "Error"
    return "how tf did u get here"

app.run(host="0.0.0.0", port=8080)