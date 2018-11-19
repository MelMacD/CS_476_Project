 import abc
 
 class Factory(metaclass=abc.ABCMeta):
     def __init__(self):
         self.html = ""
     
     @abc.abstractmethod
     def buildHtml(self):
         pass
     
     @abc.abstractmethod
     def setId(self, row):
         pass
     
     @abc.abstractmethod
     def setTop(self, row):
         pass
     
     @abc.abstractmethod
     def setLeft(self, row):
         pass
      
     @abc.abstractmethod
     def setWidth(self, row):
         pass 
     
     @abc.abstractmethod
     def setHeight(self, row):
         pass

     @abc.abstractmethod
     def setDepth(self, row):
         pass
      
