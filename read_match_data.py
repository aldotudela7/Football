# read_match_data.py

import requests
import json
from match import Match

# See API ocumentation for options available: https://docs.football-data.org/general/v4/index.html
league = 'PL' 
season = '2021'

uri = 'https://api.football-data.org/v4/competitions/{}/matches?season={}'.format(league, season)
headers = { 
    'X-Auth-Token': '13b41abb78284b7482713f316a0e3578',
           }

def parse_match(json_response):
    matches = []
    for m in json_response:
        match = {}
        match['league'] = m['competition']['name']
        match['season_start'] = m['season']['startDate']
        match['season_end'] = m['season']['endDate']
        match['date'] = m['utcDate']
        match['status'] = m['status']
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

matches = [ Match(d['league'], 
                  d['season_start'],
                  d['season_end'], 
                  d['date'],
                  d['status'],
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
