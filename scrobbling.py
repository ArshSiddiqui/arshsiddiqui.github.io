import requests
import json

userName = 'arshsiddiqui'
apiKey = '90874a2969204e8c7da1d789f5e90638'

res = requests.get(f'https://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user={userName}&api_key={apiKey}&period=7day&limit=10&format=json')
res.encoding = 'ISO-8859-1'
response = json.loads(res.text)

f = open("last_week_scrobble.json", 'w')
f.write(str(response))
f.close()

res = requests.get(f'https://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user={userName}&api_key={apiKey}&period=12month&limit=25&format=json')
res.encoding = 'ISO-8859-1'
response = json.loads(res.text)

f = open("last_year_scrobble.json", 'w')
f.write(str(response))
f.close()

res = requests.get(f'https://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user={userName}&api_key={apiKey}&period=overall&limit=25&format=json')
res.encoding = 'ISO-8859-1'
response = json.loads(res.text)

f = open("overall_scrobble.json", 'w')
f.write(str(response))
f.close()

