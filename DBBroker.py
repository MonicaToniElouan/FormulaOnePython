import mysql.connector

class DBBroker:
    _Instance = None
    _connection = None

    def __init__(self):
        DBBroker._connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="databases1122",
            database="mydb"
        )

    @staticmethod
    def GetBroker():
        if DBBroker._Instance is None:
            DBBroker._Instance = DBBroker()
        return DBBroker._Instance
    
    def Read(self,sql: str):
        self._Connect()
        com = DBBroker._connection.cursor()
        com.execute(sql)
        result = com.fetchall()
        return result
    
    def Change(self,sql: str):
        self._Connect()
        cursor = DBBroker._connection.cursor()
        cursor.execute(sql)
        DBBroker._connection.commit()
        self._Disconnect()
    
    def _Connect(self):
        if DBBroker._connection.is_connected() == False:
            try:
                DBBroker._connection.connect()
            except Exception as ex:
                print(ex)
                exit()

    def _Disconnect(self):
        if DBBroker._connection.is_connected():
            DBBroker._connection.close()
            
        
agent = DBBroker.GetBroker()
agent1 = DBBroker.GetBroker()
print(agent.Read("SELECT * FROM PERSONS"))
agent1.Change("INSERT INTO PERSONS (PersonID, PersonName) VALUES ('36', 'Miguel')")



