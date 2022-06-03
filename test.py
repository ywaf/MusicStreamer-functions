from firebase_admin import credentials
from google.cloud import storage
from flask import Flask, Response
from flask import request
from flask import send_file

app = Flask(__name__)
# from google.cloud import
#
# cred = credentials.Certificate("a.json")  # use actions secrets!!
@app.route("/test", methods=["GET"])
def pls():
    try:
        storage_client = storage.Client.from_service_account_json('a.json')
        bucket = storage_client.bucket("music_streamer_songs")
        blob = bucket.blob("songs/3.mp3")
        contents = blob.download_as_string()
        print(contents)
        return Response(contents, mimetype="audio/mpeg")
    except Exception as e:
        print(e)
        return "wtf are you doing :skull:"

app.run(host='0.0.0.0', port=69)