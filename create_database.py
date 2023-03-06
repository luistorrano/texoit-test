import sqlite3

def create_database(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(f"Error on create database {e}")

if __name__ == '__main__':
    create_database("./movieslist.db")