from code import app
from flask import request


class SignUp:
    def __init__(self):
        self.html = "Sign Up"
        
    def getHTML(self):
        return self.html
    
    def setHTML(self):
        self.html = """
<head>
<title>Sign-up Page</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="stylesheet" href="static/bootstrap.css" />
</head>
<body>
<nav class="navbar navbar-light bg-light">
  <div class="container-fluid">
  <div class="navbar-header">
  <a class="navbar-brand" href="/">Express Yourself</a>
  </div>
  <ul class="nav navbar-nav navbar-right">
    <li><a href="/login">Login</a></li>
    <li><a href="/signup">Sign Up</a></li>
  </ul>
  </div>
</nav>
<form id="SignUp" style="width:500px" method="post" enctype="multipart/form-data">
  <div class="container">
    <label><b>Email</b></label>
    <label id="email_msg" class="err_msg"></label>
    <input id="email" type="text" placeholder="Enter Email" size="30" name="email">
    </br>
    
    <label><b>Username</b></label>
    <label id="username_msg" class="err_msg"></label>
    <input id="username" type="text" placeholder="Enter Username" size="30" name="username">
    </br>
	
    <label><b>Password</b></label>
     <label id="pswd_msg" class="err_msg"></label>
    <input  type="password" placeholder="Enter Password" size="30" name="pwd">
    
    <label><b>Re-enter Password</b></label>
     <label id="reEnter_msg" class="err_msg"></label>
    <input  type="password" placeholder="Re-enter Password" size="30" name="pwd2">
     <input type="submit" name="Signup" value="Signup"/>
     <a class="dropdown-item" href="/signup">Already have an account? Sign in</a>
     </br>
  </div>
</form>
    
</body>
</html>
"""

@app.route("/signup", methods=['GET', 'POST'])

def signup():
    if request.method == 'POST':
        return "Sign up request received"
    else:
        signupHTML = SignUp()
        signupHTML.setHTML()
        return signupHTML.getHTML()
    
