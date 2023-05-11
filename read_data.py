# read_data.py

import requests
import json
from match import Match

uri = 'https://api.football-data.org/v4/competitions/PL/matches'
headers = { 'X-Auth-Token': '13b41abb78284b7482713f316a0e3578' }

def parse_match(json_response):
    matches = []
    for m in json_response:
        match = {}
        match['league'] = m['competition']['name']
        match['season'] = m['season']['startDate']
        match['date'] = m['utcDate']
        match['matchday'] = m['matchday']
        match['home_team'] = m['homeTeam']['name']
        match['home_team_short'] = m['homeTeam']['shortName']
        match['home_team_code'] = m['homeTeam']['tla']
        match['away_team'] = m['awayTeam']['name']
        match['away_team_short'] = m['awayTeam']['shortName']
        match['away_team_code'] = m['awayTeam']['tla']
        match['home_team_score'] = m['score']['fullTime']['home']
        match['away_team_score'] = m['score']['fullTime']['away']
        match['home_team_halfscore'] = m['score']['halfTime']['home']
        match['away_team_halfscore'] = m['score']['halfTime']['away']
        matches.append(match)
    return matches

response = requests.get(uri, headers=headers)
matches_dict = parse_match(response.json()['matches'])

# matches = []
# for m in matches_dict:
#     match = Match()
#     for item in m:
#         match.item = m[item]
#     matches.append(match)

matches = [ Match(d['league'], 
                  d['season'], 
                  d['date'],
                  d['matchday'],
                  d['home_team'],
                  d['home_team_short'],
                  d['home_team_code'],
                  d['away_team'],
                  d['away_team_short'],
                  d['away_team_code'],
                  d['home_team_score'],
                  d['away_team_score'],
                  d['home_team_halfscore'],
                  d['away_team_halfscore'],) for d in matches_dict ]
