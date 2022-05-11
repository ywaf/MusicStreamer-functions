import json

def songs(request, args):
    with open('songs.json', 'r') as f:
        songs = json.load(f)
    return songs