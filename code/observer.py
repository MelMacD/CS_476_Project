import abc
class Subject:

    def __init__(self):
        self._observers = set()
        self._subject_state = None

    def attach(self, observer):
        observer._subject = self
        self._observers.add(observer)

    def detach(self, observer):
        observer._subject = None
        self._observers.remove(observer)

    def _notify(self):
        for observer in self._observers:
            observer.update(self._subject_state)
            
class SQL(Subject):
      def __init__(self, name=''): 
            Subject.__init__(self)
            self.name = name
            self.sql = 0
            
      
     def getData(self):
        return self.sql





class Observer(metaclass=abc.ABCMeta):

    def __init__(self):
        self._subject = None
        self._observerState = None
    
    @abc.abstractmethod
    def update(self, arg):
        pass
