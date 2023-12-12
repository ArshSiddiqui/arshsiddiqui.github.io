import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

SPOTIFY_CLIENT_ID="e37ae59bcdd242088e01ebfc07664479"
SPOTIFY_CLIENT_SECRET="9eb43eafaaca4f41a901e1fe575cac88"
SPOTIFY_REFRESH_TOKEN="AQAVCExItC0GIHptQUkloUQO-Sa74b9Oq0hszxwteyRmsSMVh1peimmW4bdLB8P5ISThMW5f9rBPsM1gVZ5EGhZF8xfWWCJTvs8ZK05QmjKTH1HjWq9WkSBDgCkpGCmlscKk4cHDppgq9ANYXCVAaKOLrUeD2kFfWIEhYuSQIFgnkRtJr-9qREeLY3gylN2J9bo8FC23AgD16bHCoatc0ZjWGq-Mh0PssT5F53Ipxk6YRa1tvCSnr7bS0tL7e1yT0huco7uR-YOBsCVEumXq1PtwwhVo"

scope = "user-top-read"

sp_oauth = auth_manager=SpotifyOAuth(
    scope=scope,
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri="http://localhost:3000/callback"
)

# sp = spotipy.Spotify(sp_oauth)
tok = sp_oauth.get_access_token()
ref_token = tok['refresh_token']

token_info = sp_oauth.refresh_access_token(ref_token)
access_token = token_info['access_token']

sp = spotipy.Spotify(auth=access_token)

chansons = sp.current_user_top_tracks(limit=10, time_range='short_term')

# print(f"attr {chansons}")

song_names = []
singer_names = []
singer_links = []
preview_links = []
song_links = []
for i in range(0, len(chansons['items'])):
    song_names.append(chansons['items'][i]['name'])
    singer_names.append(chansons['items'][i]['album']['artists'][0]['name'])
    singer_links.append(chansons['items'][i]['album']['artists'][0]['external_urls']['spotify'])
    preview_links.append(chansons['items'][i]['preview_url'])
    song_links.append(chansons['items'][i]['external_urls']['spotify'])

json_out = '['
for i in range(0, len(song_names)):
    json_out += f'{{"name": "{song_names[i]}", "artist": "{singer_names[i]}", "artist_url": "{singer_links[i]}", "preview_link": "{preview_links[i]}", "song_link": "{song_links[i]}"}}'
    if i < len(song_names) - 1:
        json_out += ','
json_out += ']'

f = open("5_short_term_songs.json", "w", encoding='utf8')
f.write(json_out)
f.close()