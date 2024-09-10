
import psycopg2

from src.dto.skater import Skater


class SkaterDao:
    def __init__(self):
        self.connection = self._get_db_connection()

    @staticmethod
    def _get_db_connection():
        conn_string: str = "dbname=nhl user=postgres password=postgres host=127.0.0.1"
        connection = psycopg2.connect(conn_string)
        return connection

    def add_goalie_to_table(self, skater: Skater):
        insert_statement: str = (
            "INSERT INTO nhl_2023.skater (player_name, team_name, position, games_played, goals, assists, points, "
            "plus_minus, penalty_minutes, shots_on_goal, game_winning_goals, powerplay_goals, powerplay_assists, "
            "shorthanded_goals, shorthanded_assists, hits, blocked_shots) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        )

        cursor = self.connection.cursor()

        cursor.execute(insert_statement, (
            skater.player_name, skater.team_name, skater.position, skater.games_played, skater.goals, skater.assists,
            skater.points, skater.plus_minus, skater.penalty_minutes, skater.shots_on_goal,
            skater.game_winning_goals, skater.powerplay_goals, skater.powerplay_assists, skater.shorthanded_goals,
            skater.shorthanded_assists, skater.hits, skater.blocked_shots)
        )

        self.connection.commit()

    def create_skater_table(self):
        create_statement: str = (
            "CREATE TABLE nhl_2023.skater (player_name VARCHAR(255), team_name  VARCHAR(255), position  VARCHAR(255), "
            "games_played INT, goals INT, assists INT, points INT, plus_minus INT, penalty_minutes INT, "
            "shots_on_goal INT, game_winning_goals INT, powerplay_goals INT, powerplay_assists INT, "
            "shorthanded_goals INT, shorthanded_assists INT, hits INT, blocked_shots INT, fantasy_points_total INT)"
        )

        cursor = self.connection.cursor()

        cursor.execute(create_statement)

        self.connection.commit()
