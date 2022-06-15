import firebase_admin
# import flask
import functions_framework
import json
# from flask import Flask, Response
from firebase_admin import auth
from flask import send_file
from flask import Response
# from flask import request
import os
from firebase_admin import credentials
from firebase_admin import db
from google.cloud import storage


# app = flask.Flask(__name__)


def getobject(id):
    try:
        storage_client = storage.Client.from_service_account_json('/keys/firebase_service_key.json')
        bucket = storage_client.bucket("music_streamer_songs")
        blob = bucket.blob("songs/" + id + ".mp3")
        contents = blob.download_as_string()
        print(contents)
        return contents
    except Exception as e:
        print(e)
        return {"success": "false", "error": "error getting object or song does not exist"}, 400


@functions_framework.http
def songs(request):
    try:  # shamelessly ripped from oncreate function
        privkey = "/keys/firebase_service_key.json"  # gets the json secret from mounted disk - manage in gcp secrets manager
        db_url = str(
            os.getenv("FIREBASE_DB_URL"))  # firebase db url - just get from realtime database tab in firebase console
        print(db_url)
    except Exception as e:
        print("Error Getting env variables!")  # this shouldnt ever happen if you have it setup properly
        return_env_variables = {"success": "false",
                                "error": "error getting env variables"}
        return return_env_variables, 400
    try:
        cred = credentials.Certificate(privkey)  # use actions secrets!!
    except Exception as e:
        print("Error loading credentials!")
        return_credentials = {"success": "false",
                              "error": "error loading credentials"}
        return return_credentials, 400

    try:
        firebase_admin.initialize_app(cred, {
            'databaseURL': "https://musicstreamer-sdd-default-rtdb.asia-southeast1.firebasedatabase.app"
            # todo fix the bug when getting this db url from secrets manager
        })
    except Exception as e:
        print("firebase app failed to init, or is init already, full traceback: " + str(e))

    headers = request.headers
    songid = headers.get('songid')
    if songid is None:
        return {"success": "false", "error": "no song id"}, 400
    else:
        try:
            authtoken = headers.get("Authorization")
            print(authtoken)
            if authtoken == "" or authtoken is None:
                return {"success": "false", "error": "no auth provided"}, 400
            try:

                decoded_token = auth.verify_id_token(authtoken)
                # token is good
                uid = decoded_token['uid']  # get uid from jwt
                # get the song from gcp bucket
                song_probably = getobject(songid)
                return Response(song_probably, mimetype="audio/mpeg")

            except Exception as e:
                print(e)
                return {"success": "false", "error": "invalid auth token"}, 400
            return uid
        except:
            print("Failure Getting Headers")
            return {"success": "false", "error": "failure getting headers"}, 400
        return "how tf did u get here"

# app.run(host="0.0.0.0", port=8080)
