import MySQLdb

class SQLDataSender:
    def __init__(self):
        self.host = "localhost"
        self.user = "CS476"
        self.password = "$up3rSecret"
        self.databaseName = "express-yourself-db"
        self.database = connect();
    
    def connect(self):#implement some error handling
        try:
            return MySQLdb.connect(self.host,
                                   self.user,
                                   self.password,
                                   self.databaseName)
        except MySQLdb.Error as e:
            print("Error occurred while attempting to connect")
            return e
    
    def execute(self, command):
        try:
            cursor = db.cursor()
        
            cursor.execute(command)
            return cursor.fetchall()
        except MySQLdb.Error as e:
            print("Error occurred while executing command")
            return e
