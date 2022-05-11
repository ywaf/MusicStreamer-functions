import flask
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/songs', methods=['GET'])
def get_song():
    return "songs"

@app.route('/songs/<song_id>', methods=['GET'])
def getsong(song_id):
    # stream it back here
    return "song" + str(song_id)


app.run(host='127.0.0.1', port=8080, debug=True)