import json

def get_song(request):
    request.args.get('id')
    with open('data/songs.json') as f:
        songs = json.load(f)
    return songs['id']