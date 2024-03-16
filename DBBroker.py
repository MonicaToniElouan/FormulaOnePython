import mysql.connector

class DBBroker:
    def __init__(self):
        self.conn = None