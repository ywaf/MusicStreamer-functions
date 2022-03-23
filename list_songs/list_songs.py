import json


def list_songs(request):
    with open('songs.json', 'r') as f:
        songs = json.load(f)
    return songs