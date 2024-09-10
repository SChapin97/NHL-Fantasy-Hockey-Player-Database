
import psycopg2

from src.dto.goalie import Goalie


class GoalieDao:
    def __init__(self):
        self.connection = self._get_db_connection()

    @staticmethod
    def _get_db_connection():
        conn_string: str = "dbname=nhl user=postgres password=postgres host=127.0.0.1"
        connection = psycopg2.connect(conn_string)
        return connection

    def add_goalie_to_table(self, goalie: Goalie):
        insert_statement: str = (
            "INSERT INTO nhl_2023.goalies (player_name, team_name, games_played, wins, losses, overtime_losses, "
            "goals_against_average, goals_allowed, shots_against, saves, save_percentage, shutouts, minutes_played) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        )

        cursor = self.connection.cursor()

        cursor.execute(insert_statement, (
            goalie.player_name, goalie.team_name, goalie.games_played, goalie.wins, goalie.losses,
            goalie.overtime_losses, goalie.goals_against_average, goalie.goals_allowed, goalie.shots_against,
            goalie.saves, goalie.save_percentage, goalie.shutouts, goalie.minutes_played)
        )

        self.connection.commit()

    def create_goalie_table(self):
        create_statement: str = (
            "CREATE TABLE nhl_2023.goalie (player_name VARCHAR(255), team_name VARCHAR(255), games_played INT, wins INT,"
            " losses INT, overtime_losses INT, goals_against_average DECIMAL(8,1), goals_allowed INT, "
            "shots_against INT, saves INT, save_percentage DECIMAL(4,3), shutouts INT, minutes_played INT, "
            "fantasy_total_points INT)"
        )

        cursor = self.connection.cursor()

        cursor.execute(create_statement)

        self.connection.commit()