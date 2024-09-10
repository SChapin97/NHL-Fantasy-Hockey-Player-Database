
class Goalie:

    def __init__(
            self,
            player_name: str,
            team_name: str,
            games_played: int,
            wins: int,
            losses: int,
            overtime_losses: int,
            goals_against_average: float,
            goals_allowed: int,
            shots_against: int,
            saves: int,
            save_percentage: float,
            shutouts: int,
            minutes_played: int
    ):
        self.player_name: str = player_name
        self.team_name: str = team_name
        self.games_played: int = games_played
        self.wins: int = wins
        self.losses: int = losses
        self.overtime_losses: int = overtime_losses
        self.goals_against_average: float = goals_against_average
        self.goals_allowed: int = goals_allowed
        self.shots_against: int = shots_against
        self.saves: int = saves
        self.save_percentage: float = save_percentage
        self.shutouts: int = shutouts
        self.minutes_played: int = minutes_played
