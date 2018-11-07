from code import app
from flask import request

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
         
        
    </style>
    <body>


  <div class="container">
    <label for="uname"><b>Username</b></label>
    <input type="text" placeholder="Enter Username" name="uname" required>

    <label for="psw"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="psw" required>

    <button type="submit">Login</button>
    <label>
      <input type="checkbox" checked="checked" name="remember"> Remember me
    </label>
  </div>

  <div class="container" style="background-color:#f1f1f1">
    <button type="button" class="cancelbtn">Cancel</button>
    <span class="psw">Forgot <a href="#">password?</a></span>
  </div>

    
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
