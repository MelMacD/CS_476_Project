# additional: order by? num rows to return? can also join, group by
class SQLQueryBuilder:
    def __init__(self, tableName):
        self.table = tableName
    
    def selectAll(self):
        return "SELECT * FROM {tableName}".format(tableName=self.table)
    
    def selectAllFilter(self, condition):
        return "SELECT * FROM {tableName} WHERE {condition}".format(tableName=self.table,
                                                                    condition=condition)
    
    def selectColumn(self, column):
        return "SELECT {column} FROM {tableName}".format(column=column, tableName=self.table)
    
    def selectColumnFilter(self, column, condition):
        return "SELECT {column} FROM {tableName} WHERE {condition}".format(column=column,
                                                                                   tableName=self.table,
                                                                                   fieldName=condition)
    
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
    
