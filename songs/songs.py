import json
import functions_framework

def songs(request, args):
    with open('songs.json', 'r') as f:
        songs = json.load(f)
    return songs

@app.route('/songs', methods=['GET'])
def get_song():
    return "songs"

@app.route('/songs/<song_id>', methods=['GET'])
def getsong(song_id):
    # stream it back here
    return "song" + str(song_id)