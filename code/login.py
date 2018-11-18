from code import app
from flask import request, make_response, redirect
from code.sql_query_builder import SQLQueryBuilder as query
from code.database import Database as database

class Login:
    def __init__(self):
        self.html = "Log In"
        
    def getHTML(self):
        return self.html
    
    def setHTML(self):
        self.html = """
<!DOCTYPE html>
<html lang="en">
<title>Login Form</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
    
    input[type=text], input[type=password] {
    width: 100%;
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    box-sizing: border-box;
}
        
  /* Set a style for all buttons */
button {
    background-color: #4CAF50;
    color: white;
    padding: 14px 20px;
    margin: 8px 0;
    border: none;
    cursor: pointer;
    width: 100%;
}
   /* Add a hover effect for buttons */
button:hover {
    opacity: 0.8;
}     
.imgcontainer {
    text-align: center;
    margin: 24px 0 12px 0;
    position: relative;
}
         img.avatar2 {
    width: 40%;
    border-radius: 50%;
}
        
    </style>
    <body>
<!-- Navbar -->
<div class="w3-top">
  <div class="w3-bar w3-black w3-card">
    <a class="w3-bar-item w3-button w3-padding-large w3-hide-medium w3-hide-large w3-right" href="javascript:void(0)" onclick="myFunction()" title="Toggle Navigation Menu"><i class="fa fa-bars"></i></a>
    <a href="/" class="w3-bar-item w3-button w3-padding-large">Home</a>
    <a href="login" class="w3-bar-item w3-button w3-padding-large w3-hide-small">Login</a>
    <a href="signup" class="w3-bar-item w3-button w3-padding-large w3-hide-small">Sign-up</a>
</div>

<!-- Navbar on small screens (remove the onclick attribute if you want the navbar to always show on top of the content when clicking on the links) -->
<div id="navDemo" class="w3-bar-block w3-black w3-hide w3-hide-large w3-hide-medium w3-top" style="margin-top:46px">
  <a href="login" class="w3-bar-item w3-button w3-padding-large" onclick="myFunction()">Login</a>
  <a href="signup" class="w3-bar-item w3-button w3-padding-large" onclick="myFunction()">Sign-up</a>

</div>
</div>

<form id="LogIn" style="width:500px; margin-left: 35%; margin-top: 50px;" method="post" enctype="multipart/form-data">
<h3 style="text-align: center;">Login</h3>
<div class="imgcontainer">
      <img src="static/img_avatar2.png" alt="Avatar" class="avatar">
    </div>

  <div class="container">
  <label><b>Email</b></label>
    <label id="email_msg" class="err_msg"></label>
    <input id="email" type="text" placeholder="Enter Email" size="30" name="email" required>
    </br>
  
 

    <label><b>Password</b></label>
     <label id="pswd_msg" class="err_msg"></label>
    <input  type="password" placeholder="Enter Password" size="30" name="pwd" required>

    <button type="submit" name="Login" value="Login" >Login</button>
    <label>
      <input type="checkbox" checked="checked" name="remember"> Remember me
    </label>
    <a class="dropdown-item" href="/signup">Don't have an account? Sign up</a>
    </br>
  </div>
  </form>
    
    </body>
    
</html>

"""

@app.route("/login", methods=['GET', 'POST'])

def login():
    if request.method == 'POST':
        #if not successful, append error message to page
        db = database()
        queryBuilder = query("users")
        queryString = queryBuilder.selectAllFilter("email='{email}' and pwd='{password}'".format(
                email=request.form.get("email"), password=request.form.get("pwd")))
        result = db.execute(False, queryString)
        if result == []:
            errorMessage = """
                <p style="color: red; font-size: 15px; margin-left: 35%; margin-top: 50px;">The email or password was incorrect</p>"""
            loginHTML = Login()
            loginHTML.setHTML()
            return errorMessage + loginHTML.getHTML()
        else:
            redirectTo = redirect('/')
            resp = make_response(redirectTo)
            resp.set_cookie('userId', result[0][0])
            return resp
    else:
        loginHTML = Login()
        loginHTML.setHTML()
        return loginHTML.getHTML()
