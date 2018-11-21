#interface class, no implemented functions
class Subject:
    def __init__(self):
        self.connection = self.connect()

    #abstract, all children override
    def connect(self):
        pass
