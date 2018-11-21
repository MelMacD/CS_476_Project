#interface class, no implemented functions
class Observer:
    def __init__(self):
        self.html = self.buildContent()
    
    #abstract, all children override
    def buildContent(self):
        pass
