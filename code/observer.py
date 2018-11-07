import abc

class Observer(metaclass=abc.ABCMeta):

    def __init__(self):
        self._subject = None
        self._observerState = None
    
    @abc.abstractmethod
    def update(self, arg):
        pass
