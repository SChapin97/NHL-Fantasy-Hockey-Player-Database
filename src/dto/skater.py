
class Skater:

    def __init__(
            self,
            player_name: str,
            team_name: str,
            position: str,
            games_played: int,
            goals: int,
            assists: int,
            points: int,
            plus_minus: int,
            penalty_minutes: int,
            shots_on_goal: int,
            game_winning_goals: int,
            powerplay_goals: int,
            powerplay_assists: int,
            shorthanded_goals: int,
            shorthanded_assists: int,
            hits: int,
            blocked_shots: int
    ):
        self.player_name: str = player_name
        self.team_name: str = team_name
        self.position: str = position
        self.games_played: int = games_played
        self.goals: int = goals
        self.assists: int = assists
        self.points: int = points
        self.plus_minus: int = plus_minus
        self.penalty_minutes: int = penalty_minutes
        self.shots_on_goal: int = shots_on_goal
        self.game_winning_goals: int = game_winning_goals
        self.powerplay_goals: int = powerplay_goals
        self.powerplay_assists: int = powerplay_assists
        self.shorthanded_goals: int = shorthanded_goals
        self.shorthanded_assists: int = shorthanded_assists
        self.hits: int = hits
        self.blocked_shots: int = blocked_shots
