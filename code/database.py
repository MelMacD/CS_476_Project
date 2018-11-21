import pyodbc
from code.sql_query_builder import SQLQueryBuilder as query
from code.subject import Subject

class Database(Subject):
    def __init__(self):
        self.server = 'tcp:expressyourself.database.windows.net'
        self.database = 'expressyourself'
        self.username = 'cs476'
        self.password = '$up3rSecret'
        self.driver = '{ODBC Driver 13 for SQL Server}'
        super().__init__()
      
    #override
    def connect(self):
        return pyodbc.connect('DRIVER='+self.driver+';SERVER='+self.server+';PORT=1433;DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
    
    def buildQuery(self, tableName, selection, *args):
        queryBuilder = query(tableName)
        queryString = "error"
        if selection == "selectAll":
            queryString = queryBuilder.selectAll()
        elif selection == "selectAllFilter":
            queryString = queryBuilder.selectAllFilter(args[0])
        elif selection == "selectCountFilter":
            queryString = queryBuilder.selectCountFilter(args[0])
        elif selection == "selectCountDistinctFilter":
            queryString = queryBuilder.selectCountDistinctFilter(args[0], args[1])
        elif selection == "insertRow":
            queryString = queryBuilder.insertRow(args[0])
        elif selection == "update":
            queryString = queryBuilder.update(args[0], args[1])
        elif selection == "delete":
            queryString = queryBuilder.delete(args[0])
        return queryString
    
    def execute(self, isModifying, command):
        self.rowCount = 0
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

    def disconnect(self):
        self.connection.close()
