import requests
import json

userName = 'arshsiddiqui'
apiKey = '90874a2969204e8c7da1d789f5e90638'

res = requests.get(f'http://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user={userName}&api_key={apiKey}&format=json')
res.encoding = 'utf-8'
response = json.loads(res.text.encode('utf-8'))

top_artists = []
top_artists_url = []
for i in range(0, 3):
    top_artists.append(response['topartists']['artist'][i]['name'])
    top_artists_url.append(response['topartists']['artist'][i]['url'])

json_out = '['
for i in range(0, 3):
    json_out += f'{{"name": "{top_artists[i]}", "link": "{top_artists_url[i]}"}}'
    if i < 2:
        json_out += ','
json_out += ']'

f = open("top_artists.json", 'w', encoding='utf8')
f.write(str(json_out))
f.close()

res = requests.get(f'http://ws.audioscrobbler.com/2.0/?method=user.getweeklyalbumchart&user={userName}&api_key={apiKey}&format=json') 
res.encoding = 'utf-8'
response = json.loads(res.text.encode('utf-8'))

top_albums = []
top_albums_url = []
for i in range(0, 3):
    top_albums.append(response['weeklyalbumchart']['album'][i]['name'])
    top_albums_url.append(response['weeklyalbumchart']['album'][i]['url'])

json_out = '['
for i in range(0, 3):
    json_out += f'{{"name": "{top_albums[i]}", "link": "{top_albums_url[i]}"}}'
    if i < 2:
        json_out += ','
json_out += ']'

f = open("top_albums.json", 'w', encoding='utf8')
f.write(str(json_out))
f.close()


res = requests.get(f'https://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user={userName}&api_key={apiKey}&period=7day&limit=10&format=json')
res.encoding = 'utf-8'
response = json.loads(res.text)

chansons = response['toptracks']['track'] 
song_names = []
artist_names = []
url = []
artist_url = []

for i in range(0, len(chansons)):
    song_names.append(chansons[i]['name'])
    artist_names.append(chansons[i]['artist']['name'])
    url.append(chansons[i]['url'])
    artist_url.append(chansons[i]['artist']['url'])


json_out = '['
for i in range(0, len(chansons)):
    json_out += f'{{"name": "{song_names[i]}", "artist": "{artist_names[i]}", "song_url": "{url[i]}", "artist_url": "{artist_url[i]}"}}'
    if i < len(chansons) - 1:
        json_out += ','
json_out += ']'

f = open("last_week_scrobble.json", 'w', encoding='utf8')
f.write(str(json_out))
f.close()

res = requests.get(f'https://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user={userName}&api_key={apiKey}&period=12month&limit=25&format=json')
res.encoding = 'utf-8'
response = json.loads(res.text)

chansons = response['toptracks']['track'] 
song_names = []
artist_names = []
url = []
artist_url = []

for i in range(0, len(chansons)):
    song_names.append(chansons[i]['name'])
    artist_names.append(chansons[i]['artist']['name'])
    url.append(chansons[i]['url'])
    artist_url.append(chansons[i]['artist']['url'])


json_out = '['
for i in range(0, len(chansons)):
    json_out += f'{{"name": "{song_names[i]}", "artist": "{artist_names[i]}", "song_url": "{url[i]}", "artist_url": "{artist_url[i]}"}}'
    if i < len(chansons) - 1:
        json_out += ','
json_out += ']'


f = open("last_year_scrobble.json", 'w', encoding='utf8')
f.write(str(json_out))
f.close()

res = requests.get(f'https://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user={userName}&api_key={apiKey}&period=overall&limit=25&format=json')
res.encoding = 'utf-8'
response = json.loads(res.text)

chansons = response['toptracks']['track'] 
song_names = []
artist_names = []
url = []
artist_url = []

for i in range(0, len(chansons)):
    song_names.append(chansons[i]['name'])
    artist_names.append(chansons[i]['artist']['name'])
    url.append(chansons[i]['url'])
    artist_url.append(chansons[i]['artist']['url'])


json_out = '['
for i in range(0, len(chansons)):
    json_out += f'{{"name": "{song_names[i]}", "artist": "{artist_names[i]}", "song_url": "{url[i]}", "artist_url": "{artist_url[i]}"}}'
    if i < len(chansons) - 1:
        json_out += ','
json_out += ']'


f = open("overall_scrobble.json", 'w', encoding='utf8')
f.write(str(json_out))
f.close()

