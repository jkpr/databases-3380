from pathlib import Path

import psycopg2
from psycopg2 import sql


DATABASE_NAME = "healthcare_db"
DATABASE_SCHEMA = "schema.sql"
DATABASE_DATA = "data.sql"


def create_db():
    con = psycopg2.connect(host="localhost", user="postgres")
    con.set_session(autocommit=True)
    cur = con.cursor()
    cur.execute(
        sql.SQL("DROP DATABASE IF EXISTS {};").format(sql.Identifier(DATABASE_NAME))
    )
    cur.execute(
        sql.SQL("CREATE DATABASE {};").format(sql.Identifier(DATABASE_NAME))
    )
    cur.close()
    con.close()
    print(f"Created DB: {DATABASE_NAME}")


def create_tables():
    con = psycopg2.connect(dbname=DATABASE_NAME, host="localhost", user="postgres")
    cur = con.cursor()
    cur.execute(Path(DATABASE_SCHEMA).read_text(encoding="utf-8"))
    con.commit()
    cur.close()
    con.close()
    print(f"Created tables from {DATABASE_SCHEMA}")


def populate_data():
    con = psycopg2.connect(dbname=DATABASE_NAME, host="localhost", user="postgres")
    cur = con.cursor()
    cur.execute(Path(DATABASE_DATA).read_text(encoding="utf-8"))
    con.commit()
    cur.close()
    con.close()
    print(f"Inserted data from {DATABASE_DATA}")



def main():
    create_db()
    create_tables()
    populate_data()


if __name__ == "__main__":
    main()