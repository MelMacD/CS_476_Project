from code import app

class Login:
    def __init__(self):
        self.html = "Log In"
        
    def getHTML(self):
        print("Hey logger do you work?")
        return self.html

@app.route("/login")

def login():
    
    loginHTML = Login()

    return loginHTML.getHTML()
