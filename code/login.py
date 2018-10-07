from code import app
from flask import request

class Login:
    def __init__(self):
        self.html = "Log In"
        
    def getHTML(self):
        return self.html
    
    def setHTML(self):
        self.html = """
<head>
<title>Login Page</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="stylesheet" href="static/bootstrap.css" />
</head>
<body>

<nav class="navbar navbar-light bg-light">
  <a class="navbar-brand" href="/">
    Home
  </a>
  <a class="navbar-item" href="/login">
    Login
  </a>
  <a class="navbar-item" href="/signup">
    Sign Up
  </a>
</nav>

<form id="LogIn" style="width:500px" method="post" enctype="multipart/form-data">
  <div class="container">
    <label><b>Username</b></label>
    <label id="uname_msg" class="err_msg"></label>
    <input id="uname" type="text" placeholder="Enter Username" size="30" name="email">
    </br>
	
    <label><b>Password</b></label>
     <label id="pswd_msg" class="err_msg"></label>
    <input  type="password" placeholder="Enter Password" size="30" name="pwd">
     <input type="submit" name="Login" value="Login"/>
     <a class="dropdown-item" href="#">Forgot password?</a>
     <a class="dropdown-item" href="/signup">New around here? Sign up</a>
     </br>
  </div>
</form>
    
<script>
document.getElementById("LogIn").addEventListener("submit", LogInForm, false);
window.onload=document.getElementById("name").value= "";
</script>
</body>
</html>
"""

@app.route("/login", methods=['GET', 'POST'])

def login():
    if request.method == 'POST':
        return "Request received"
    else:
        loginHTML = Login()
        loginHTML.setHTML()
        return loginHTML.getHTML()
