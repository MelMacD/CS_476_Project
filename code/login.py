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
<style>
/* Center the image  */
.imgcontainer {
    text-align: center;
    margin: 24px 0 12px 0;
    position: relative;
}

img.avatar {
    width: 40%;
    border-radius: 50%;
}
</style>
</head>
<body>

<nav class="navbar navbar-light bg-light">
  <div class="container-fluid">
  <div class="navbar-header">
  <a class="navbar-brand" href="/">Express Yourself</a>
  <div class="imgcontainer">
      <img src="img_avatar2.png" alt="Avatar" class="avatar">
    </div>
  </div>
  <ul class="nav navbar-nav navbar-right">
    <li><a href="/login">Login</a></li>
    <li><a href="/signup">Sign Up</a></li>
  </ul>
  </div>
</nav>

<form id="LogIn" style="width:500px" method="post" enctype="multipart/form-data">
  <div class="container">
    <label><b>Email</b></label>
    <label id="email_msg" class="err_msg"></label>
    <input id="email" type="text" placeholder="Enter Email" size="30" name="email">
    </br>
	
    <label><b>Password</b></label>
     <label id="pswd_msg" class="err_msg"></label>
    <input  type="password" placeholder="Enter Password" size="30" name="pwd">
     <input type="submit" name="Login" value="Login"/>
     <label>
        <input type="checkbox" checked="checked" name="remember" value="Remember me">
     </label>
     <a class="dropdown-item" href="/signup">Don't have an account? Sign up</a>
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
        return str(request.form.get("email") + " " + request.form.get("pwd"))
    else:
        loginHTML = Login()
        loginHTML.setHTML()
        return loginHTML.getHTML()
