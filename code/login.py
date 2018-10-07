from code import app

class Login:
    def __init__(self):
        self.html = "Log In"
        
    def getHTML(self):
        print("Hey logger do you work?")
        return self.html
    
    def setHTML(self):
        self.html = """
<head>
<title>Login Page</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<body>
    
<form id="LogIn" style="width:500px" method="post" enctype="multipart/form-data">
  <div class="container">
    <label><b>Email</b></label>
    <label id="uname_msg" class="err_msg"></label>
    <input id="uname" type="text" placeholder="Enter Email" size="30" name="email">
	
    <label><b>Password</b></label>
     <label id="pswd_msg" class="err_msg"></label>
    <input  type="password" placeholder="Enter Password" size="30" name="pwd">
     <input type="submit" name="Login" value="Login"/>
     <a class="dropdown-item" href="#">Forgot password?</a>
     <a class="dropdown-item" href="/signup">New around here? Sign up</a>
  </div>
</form>
    
<script>
document.getElementById("LogIn").addEventListener("submit", LogInForm, false);
window.onload=document.getElementById("name").value= "";
</script>
</body>
</html>
"""

@app.route("/login")

def login():
    
    loginHTML = Login()

    return loginHTML.getHTML()
