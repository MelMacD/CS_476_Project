class SQLQueryBuilder:
    def __init__(self, tableName):
        self.table = tableName
    
    def selectAll(self):
        return "SELECT * FROM {tableName}".format(tableName=self.table)
    
    def selectAllFilter(self, condition):
        return "SELECT * FROM {tableName} WHERE {condition}".format(tableName=self.table,
                                                                    condition=condition)
    
    def selectCountFilter(self, condition):
        return "SELECT COUNT(*) FROM {tableName} WHERE {condition}".format(tableName=self.table,
                                                                    condition=condition)
    
    def selectCountDistinctFilter(self, column, condition):
        return "SELECT COUNT(DISTINCT {column}) FROM {tableName} WHERE {condition}".format(tableName=self.table,
                                                                                           condition=condition,
                                                                                           column=column)
    
    def insertRow(self, values):
        return "INSERT INTO {tableName} VALUES ({values})".format(tableName=self.table,
                                                                  values=values)
    
    def update(self, keyValuePairs, condition):
        return "UPDATE {tableName} SET {keyValuePairs} WHERE {condition}".format(tableName=self.table,
                                                                                 keyValuePairs=keyValuePairs,
                                                                                 condition=condition)
    def delete(self, condition):
        return "DELETE FROM {tableName} WHERE {condition}".format(tableName=self.table,
                                                                  condition=condition)
    
