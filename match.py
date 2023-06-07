# match.py
import dateutil.parser

class Match:
    def __init__(self, 
                 league, 
                 season_start,
                 season_end,
                 date,
                 status,
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
        self.season_start = dateutil.parser.parse(season_start)
        self.season_end = dateutil.parser.parse(season_end)
        self.date = dateutil.parser.isoparse(date)
        self.status = status
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
    
    @property
    def goal_diff(self):
        try:
            goal_diff = self.home_team_score - self.away_team_score
        except TypeError:
            goal_diff = None
        return goal_diff
    
    @property
    def winner(self):
        try:
            diff = self.home_team_score - self.away_team_score
        except TypeError:
            diff = None
        if diff == None:
            return None
        elif diff == 0:
            return "tie"
        elif diff > 0:
            return self.home_team
        else:
            return self.away_team

    def __repr__(self):
        return f'Match(Matchday:{self.matchday}, home:{self.home_team}, away:{self.away_team},{self.home_team_score}:{self.away_team_score}, winner:{self.winner})'