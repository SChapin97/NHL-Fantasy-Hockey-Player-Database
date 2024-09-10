
import psycopg2


class FantasyPointDao:
    def __init__(self):
        self.connection = self._get_db_connection()
        self.points_dict: dict = {
            "goals": 6,
            "assists": 4,
            "powerplay_goals": 2,
            "powerplay_assists": 1,
            "shorthanded_goals": 1.5,
            "shots_on_goal": .6,
            "faceoff_wins": .25,
            "hits": .4,
            "blocks": .5,
            "games_started": 1,
            "wins": 5,
            "goals_against": -2.25,
            "saves": .42,
            "shutouts": 5
        }

    @staticmethod
    def _get_db_connection():
        conn_string: str = "dbname=nhl user=postgres password=postgres host=127.0.0.1"
        connection = psycopg2.connect(conn_string)
        return connection

    def add_values_to_table(self):
        for key, value in self.points_dict:
            insert_statement: str = (
                f"INSERT INTO nhl_2023.fantasy_points ({key}) VALUES ({value})"
            )

            cursor = self.connection.cursor()

            cursor.execute(insert_statement)

        self.connection.commit()

    def create_fantasy_point_table(self):
        create_statement: str = (
            "CREATE TABLE nhl_2023.fantasy_points (goals NUMERIC(3,2), assists NUMERIC(3,2), "
            "powerplay_goals NUMERIC(3,2), powerplay_assists NUMERIC(3,2), shorthanded_goals NUMERIC(3,2),"
            "shots_on_goal NUMERIC(3,2), faceoff_wins NUMERIC(3,2), hits NUMERIC(3,2), blocks NUMERIC(3,2), "
            "games_started NUMERIC(3,2), wins NUMERIC(3,2), goals_against NUMERIC(3,2), saves NUMERIC(3,2), "
            "shutouts NUMERIC(3,2))"
        )

        cursor = self.connection.cursor()

        cursor.execute(create_statement)

        self.connection.commit()