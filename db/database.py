import psycopg2
from psycopg2 import sql

class Database:
    def __init__(self, host, dbname, user, password):
        self.connection = psycopg2.connect(
            host=host,
            dbname=dbname,
            user=user,
            password=password
        )
        self.cursor = self.connection.cursor()

    def fetch(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def execute(self, query, params=None):
        self.cursor.execute(query, params)
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()
