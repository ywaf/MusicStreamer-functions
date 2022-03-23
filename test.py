import flask
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/getsong', methods=['GET'])
def get_song():
    idtoget = request.args.get('id')
    with open('songs.json') as f:
        songs = json.load(f)
    return {'success': 'true', 'title': songs['songs'][idtoget]['title'], 'artist': songs['songs'][idtoget]['artist'], 'album': songs['songs'][idtoget]['album'], 'url': songs['songs'][idtoget]['url'], 'id': idtoget, 'artwork': songs['songs'][idtoget]['artwork']}, 200

app.run(host='127.0.0.1', port=8080, debug=True)