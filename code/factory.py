 import abc
 
 class Factory(metaclass=abc.ABCMeta):
     def __init__(self):
         self.html = self.appendReaction
         #db values?
     
     @abc.abstractmethod
     def buildHtml(self):
         pass
     
     @abc.abstractmethod
     def setLocation(self):
         pass
     
     @abc.abstractmethod
     def setSize(self):
         pass
     
     def buildReaction(self):
         pass
         #this might actually be implemented here
     
     def appendReaction(self):
         return self.buildHtml() + self.buildReaction()
     
