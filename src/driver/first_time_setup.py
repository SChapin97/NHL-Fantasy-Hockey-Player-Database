import psycopg2
from src.dao.goalie_dao import GoalieDao
from src.dao.skater_dao import SkaterDao
from src.dao.fantasy_point_dao import FantasyPointDao

# Create schema
create_schema_statement: str = "CREATE SCHEMA IF NOT EXISTS nhl_2023"

conn_string: str = "dbname=nhl user=postgres password=postgres host=127.0.0.1"
connection = psycopg2.connect(conn_string)
cursor = connection.cursor()

cursor.execute(create_schema_statement)

connection.commit()
connection.close()

# Create tables
goalie_dao = GoalieDao()
goalie_dao.create_goalie_table()

skater_dao = SkaterDao()
skater_dao.create_skater_table()

fantasy_point_dao = FantasyPointDao()
fantasy_point_dao.create_fantasy_point_table()


# Instantiate values
fantasy_point_dao.add_values_to_table()

