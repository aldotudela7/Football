# match.py

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
        self.season_start = season_start
        self.season_end = season_end
        self.date = date
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
        return self.home_team_score - self.away_team_score
    
    @property
    def winner(self):
        diff = self.home_team_score - self.away_team_score
        if diff == 0:
            return "tie"
        elif diff > 0:
            return self.home_team
        else:
            return self.away_team

    def __repr__(self):
        return f'Match(Matchday:{self.matchday}, home:{self.home_team}, away:{self.away_team},{self.home_team_score}:{self.away_team_score}, winner:{self.winner})'