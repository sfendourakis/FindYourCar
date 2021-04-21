import Database
from dotenv import load_dotenv
load_dotenv()
import os

database = os.getenv("DATABASE_DIR")


def main():
    create_users = """CREATE TABLE IF NOT EXISTS USERS (
                                        user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                        user_name text NOT NULL,
                                        user_password text NOT NULL,
                                        email text,
                                        role text NOT NULL
                                    ); """

    conn = Database.create_connection(database)
    if conn is not None:
        Database.create_table(conn, create_users)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
