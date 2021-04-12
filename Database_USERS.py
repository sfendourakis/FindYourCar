import sqlite3
from sqlite3 import Error


def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"C:\sqlite\db\pythonsqlite.db"

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS USERS (
                                        user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                        user_name text NOT NULL,
                                        user_password text NOT NULL,
                                        email text
                                    ); """

    sql_create_roles_table = """CREATE TABLE IF NOT EXISTS ROLES (
                                    role_id INTEGER NOT NULL PRIMARY KEY,
                                    role_name text NOT NULL
                                );"""

    sql_create_user_roles_table = """CREATE TABLE IF NOT EXISTS USERS_ROLES (
                                    user_id INTEGER NOT NULL PRIMARY KEY,
                                    role_id INTEGER NOT NULL,
                                    FOREIGN KEY (user_id) REFERENCES USERS (user_id)
                                    FOREIGN KEY (role_id) REFERENCES ROLES (role_id)
                                );"""
    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_users_table)

        # create tasks table
        create_table(conn, sql_create_roles_table)

        # create tasks table
        create_table(conn, sql_create_user_roles_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()