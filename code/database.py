import pyodbc

class Database:
    def __init__(self):
        self.server = 'tcp:expressyourself.database.windows.net'
        self.database = 'expressyourself'
        self.username = 'cs476'
        self.password = '$up3rSecret'
        self.driver = '{ODBC Driver 13 for SQL Server}'
        self.connection = self.connect()
        self.rowCount = 0
      
    def connect(self):
        return pyodbc.connect('DRIVER='+self.driver+';SERVER='+self.server+';PORT=1433;DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
    
    def execute(self, isModifying, command):
        self.rowCount = 0
        try:
            cursor = self.connection.cursor()
            cursor.execute(command)
            if isModifying:
                self.connection.commit()
                return "Success"
            else:
                self.rowCount = cursor.rowcount
                return cursor.fetchall()
        except pyodbc.Error as e:
            sqlstate = ex.args[1]
            return sqlstate

    def disconnect(self):
        self.connection.close()
        
    def getRowCount(self):
        return self.rowCount
