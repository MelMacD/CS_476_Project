 class Element:
     def __init__(self, row):
         self.id = self.setId(row)
         self.top = self.setTop(row)
         self.left = self.setLeft(row)
         self.width = self.setWidth(row)
         self.height = self.setHeight(row)
         self.depth = self.setDepth(row)
     #
     #def buildHtml(self):
     #    pass
     
     def setId(self, row):
        return row[1]
        
    def setTop(self, row):
        return row[2]
     
    def setLeft(self, row):
        return row[3]
    
    def setWidth(self, row):
        return row[4]
     
    def setHeight(self, row):
        return row[5]
    
    def setDepth(self, row):
        return row[6]
      
