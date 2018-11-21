class Observer:

    def __init__(self):
        self._subject = None
        self._observerState = None
    
    @abc.abstractmethod
    def update(self, arg):
        pass
