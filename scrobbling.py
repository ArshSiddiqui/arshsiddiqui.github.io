import requests
import json

userName = 'arshsiddiqui'
apiKey = '90874a2969204e8c7da1d789f5e90638'

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
f.write(str(response))
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
f.write(str(response))
f.close()

