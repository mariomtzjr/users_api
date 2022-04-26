import requests
import os
import sys

import sqlite3
from sqlite3 import Error


def main():
    '''Get argument value'''

    if len(sys.argv) >= 2:
        users_option = sys.argv[1]
        users_number = sys.argv[2]
        if users_option and users_number:
            if users_option in  ["-t", "--total"] and users_number.isnumeric():
                return int(users_number)
            else:
                print("Wrong arguments, you need to specify the number (positive integer) of users with option -t <total> or --total <total>")
                sys.exit(1)
    return 150
    
    
def get_users(users_number: int):
    """Get github users from github api"""

    url = os.getenv('GITHUB_API_URL')
    return requests.get(url).json()[:users_number]


def populate_database(users_number: int, conn: sqlite3.Connection):
    """Function to populate the database with github users api data"""

    INSERT_USERS_QUERY = """INSERT INTO github_users
                          (username, avatar_url, type, url) 
                           VALUES
                           (?, ?, ?, ?)"""
    if conn:
        users = get_users(users_number)
        for user in users:
            data_tuple = (
                user.get('login'),
                user.get('avatar_url'),
                user.get('type'),
                user.get('url')
            )
            try:
                cursor = conn.cursor()
                cursor.execute(INSERT_USERS_QUERY, data_tuple)
                conn.commit()
            except sqlite3.IntegrityError:
                print(f"User {user.get('login')} already exists in the database")
        conn.close()


def get_database_path(db_file):
    """Get the path of the database file"""

    db_file_path = os.path.join(os.path.dirname(__file__), f'../app/main/database/{db_file}')
    normalized_db_file_path = os.path.normpath(db_file_path)

    return normalized_db_file_path


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None

    try:
        database_file_path = get_database_path(db_file)

        conn = sqlite3.connect(database_file_path)
        print(f"Connection to {db_file} was successful")
        cursor = conn.cursor()
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS github_users(
                    id integer PRIMARY KEY,
                    username VARCHAR(255) NOT NULL UNIQUE,
                    avatar_url VARCHAR(500) NOT NULL,
                    type VARCHAR(50) NOT NULL,
                    url VARCHAR(700) NOT NULL
                );
                """
        )
        return conn
    except Error as e:
        print(e)
    # finally:
    #     if conn:
    #         conn.close()
    #         print("The connection to the database was closed")



if __name__ == '__main__':
    
    users_number = main()
    conn = create_connection(r"github_users.db")

    populate_database(users_number, conn)

    
