# match.py

class Match:
    def __init__(self, 
                 league, 
                 season, 
                 date, 
                 matchday, 
                 home_team, 
                 home_team_short,
                 home_team_code,
                 away_team,
                 away_team_short,
                 away_team_code,
                 home_team_score,
                 away_team_score,
                 home_team_halfscore,
                 away_team_halfscore):
        self.league = league 
        self.season = season 
        self.date = date
        self.matchday = matchday
        self.home_team = home_team
        self.home_team_short = home_team_short
        self.home_team_code = home_team_code
        self.away_team = away_team
        self.away_team_short = away_team_short
        self.away_team_code = away_team_code
        self.home_team_score = home_team_score
        self.away_team_score = away_team_score
        self.home_team_halfscore = home_team_halfscore
        self.away_team_halfscore = away_team_halfscore

    def __repr__(self):
        return f'Match({self.matchday},{self.home_team},{self.away_team},{self.home_team_score},{self.away_team_score})'