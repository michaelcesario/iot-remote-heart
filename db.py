import psycopg2
import os
from urllib.parse import urlparse


class DatabaseConnection:
    @classmethod
    def getDBCursor(cls):

        dbConnection = psycopg2.connect(
            dbname=os.environ['DATABASE'],
            user=os.environ['USER'],
            password=os.environ['PASSWORD'],
            host=os.environ['HOST'],
            port=os.environ['PORT']
        )
        return dbConnection
