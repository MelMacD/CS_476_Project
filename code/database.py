import pyodbc

class Database:
    def __init__(self, tableName):
        self.table = tableName
        self.server = 'tcp:expressyourself.database.windows.net'
        self.database = 'expressyourself'
        self.username = 'cs476'
        self.password = '$up3rSecret'
        self.driver = '{ODBC Driver 13 for SQL Server}'
        #self.connection = connect()
      
    def connect(self):
        try:
            return pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
        except Exception as e:
            return e
    
    def execute(self, isModifying, command):
        try:
            cursor = self.connection.cursor()
            cursor.execute(command)
            if isModifying:
                self.connection.commit()
                return "Success"
            else:
                return cursor.fetchall()
        except pyodbc.Error as e:
            sqlstate = ex.args[1]
            return sqlstate
