# read_match_data.py

import requests
from match import Match

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

def next_matches(matches, games=3):
    unplayed = []
    for i in matches:
        if i.status == "TIMED":
            unplayed.append(i)
    unplayed = sorted(unplayed, key=lambda Match: Match.date)
    return unplayed[:games]

def save_matches_as_csv(matches_dict, path):
    import csv
    keys = matches_dict[0].keys()
    with open(path, 'w', encoding='utf8', newline='') as outfile:
        dict_writer = csv.DictWriter(outfile, keys)
        dict_writer.writeheader()
        dict_writer.writerows(matches_dict)

# See API documentation for options available: https://docs.football-data.org/general/v4/index.html
league = 'PL' 
seasons = ['2020','2021','2022']

headers = { 
    'X-Auth-Token': '13b41abb78284b7482713f316a0e3578',
           }

matches_list = []
for season in seasons:
    uri = 'https://api.football-data.org/v4/competitions/{}/matches?season={}'.format(league, season)
    response = requests.get(uri, headers=headers)
    matches_dict = parse_match(response.json()['matches'])
    matches_list.extend(matches_dict)

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
                  d['away_team_halfscore'],) for d in matches_list ]

next_matches_list = next_matches(matches)
