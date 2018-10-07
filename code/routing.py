from code import app


@app.route("/")

def hello():

    return "Hello World!"

@app.route("/login")

def login():

    return "Log In"

@app.route("/signup")

def signup():

    return "Sign Up"
