import pandas as pd
import Database


database = r"C:\sqlite\db\pythonsqlite.db"
dataset = pd.read_csv('cars.csv')


def main():
    conn = Database.create_connection(database)
    if conn is not None:
        # create CARS table
        dataset.to_sql('CARS', conn)


if __name__ == '__main__':
    main()
