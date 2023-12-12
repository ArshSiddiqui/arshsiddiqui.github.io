import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

SPOTIFY_CLIENT_ID="e37ae59bcdd242088e01ebfc07664479"
SPOTIFY_CLIENT_SECRET="9eb43eafaaca4f41a901e1fe575cac88"
SPOTIFY_REFRESH_TOKEN="AQAVCExItC0GIHptQUkloUQO-Sa74b9Oq0hszxwteyRmsSMVh1peimmW4bdLB8P5ISThMW5f9rBPsM1gVZ5EGhZF8xfWWCJTvs8ZK05QmjKTH1HjWq9WkSBDgCkpGCmlscKk4cHDppgq9ANYXCVAaKOLrUeD2kFfWIEhYuSQIFgnkRtJr-9qREeLY3gylN2J9bo8FC23AgD16bHCoatc0ZjWGq-Mh0PssT5F53Ipxk6YRa1tvCSnr7bS0tL7e1yT0huco7uR-YOBsCVEumXq1PtwwhVo"

scope = "user-top-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
client_id="e37ae59bcdd242088e01ebfc07664479",
client_secret=SPOTIFY_CLIENT_SECRET,
redirect_uri="http://localhost:3000/callback"))

chansons = sp.current_user_top_tracks(limit=10, time_range='short_term')

# print(f"attr {chansons}")

song_names = []
singer_names = []
for i in range(0, len(chansons['items'])):
    song_names.append(chansons['items'][i]['name'])
    singer_names.append(chansons['items'][i]['album']['artists'][0]['name'])

json_out = '['
for i in range(0, len(song_names)):
    json_out += f'{{"name": "{song_names[i]}", "artist": "{singer_names[i]}"}}'
    if i < len(song_names) - 1:
        json_out += ','
json_out += ']'
print(json.loads(json_out))