from code import app

class Login:
    def init(self):
        html = "Log In"
        return html

@app.route("/login")

def login():
    
    loginHTML = Login()

    return loginHTML
