import mysql.connector

class DBBroker:
    _Instance = None
    _connection = None

    def __init__(self):
        DBBroker._connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="databases1122",
            database="FormulaOne"
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
            

#agent = DBBroker.GetBroker()
#agent.Read("CREATE TABLE COUNTRIES ( `CountryID` CHAR(3) NOT NULL PRIMARY KEY , `CountryName` VARCHAR(45) NOT NULL , `CountryPopulation` INT NOT NULL);")
#agent.Read("CREATE TABLE GPs ( `GPID` INT NOT NULL AUTO_INCREMENT PRIMARY KEY , `GPName` VARCHAR(80) NOT NULL , `CountryID` CHAR(3) NOT NULL , FOREIGN KEY (`CountryID`) REFERENCES COUNTRIES(`CountryID`));")
#agent.Read("CREATE TABLE TEAMS ( `TeamID` INT NOT NULL AUTO_INCREMENT PRIMARY KEY , `TeamName` VARCHAR(45) NOT NULL , `TeamCountry` CHAR(3) NOT NULL , `CreationDate` DATE NOT NULL, FOREIGN KEY (TeamCountry) REFERENCES COUNTRIES(CountryID));")
#agent.Read("ALTER TABLE GPs CHANGE COLUMN GPCountry GPCountry CHAR(3) NOT NULL,ADD FOREIGN KEY (GPCountry) REFERENCES COUNTRIES(CountryID);")
