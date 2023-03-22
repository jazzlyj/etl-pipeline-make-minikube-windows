import os
from pathlib import Path
from dotenv import load_dotenv

import psycopg2
import psycopg2.extras as extras

env_path = str(Path.home()) + '\dev.env'
print(env_path)
load_dotenv(dotenv_path=env_path)

DBHost = os.getenv("DATABASE_HOST")
DBUser = os.getenv("DATABASE_USER")
DBPassword = os.getenv("DATABASE_PASSWORD")
DBPort = os.getenv("DATABASE_PORT")
DBSchema = os.getenv("DATABASE_NAME")


def pg_conn():
    """Create a connection to Postgres DB."""
    try:
        pgconn = psycopg2.connect(
            host=DBHost,
            port=DBPort,
            database=DBSchema,
            user=DBUser,
            password=DBPassword)
        print("Info: Opened Postgres DB connection")
        return pgconn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def pg_load(conn, query, df, page_size=100):
    """
    Using psycopg2.extras.execute_batch() to load the data into the database 
    """
    tuples = [tuple(x) for x in df.to_numpy()]
    query = query
    cursor = conn.cursor()
    try:
        extras.execute_batch(cursor, query, tuples, page_size)
        conn.commit()
        print("Loaded: Uploaded data; pg_load() done.")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    cursor.close()
    conn.close()