# read_data.py

import requests
import json

uri = 'https://api.football-data.org/v4/competitions/PL/matches'
headers = { 'X-Auth-Token': '13b41abb78284b7482713f316a0e3578' }

response = requests.get(uri, headers=headers)
for match in response.json()['matches']:
    print (match)