from code import app
from flask import request, redirect
import pyodbc


class SignUp:
    def __init__(self):
        self.html = "Sign Up"
        
    def getHTML(self):
        return self.html
    
    def setHTML(self):
        self.html = """
<!DOCTYPE html>
<html lang="en">
<title>Sign-up Form</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
body {font-family: "Lato", sans-serif}
.mySlides {display: none}
    
     {box-sizing: border-box
}
    /* Full-width input fields */
  input[type=text], input[type=password] {
  width: 100%;
  padding: 15px;
  margin: 5px 0 22px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}

input[type=text]:focus, input[type=password]:focus {
  background-color: #ddd;
  outline: none;
}

hr {
  border: 1px solid #f1f1f1;
  margin-bottom: 25px;
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
  opacity: 0.9;
}

button:hover {
  opacity:1;
}

/* Extra styles for the cancel button */
.cancelbtn {
  padding: 14px 20px;
  background-color: #f44336;
}

/* Float cancel and signup buttons and add an equal width */
.cancelbtn, .signup {
  float: left;
  width: 50%;
}

/* Add padding to container elements */
.container {
  padding: 16px;
}

/* Clear floats */
.clearfix::after {
  content: "";
  clear: both;
  display: table;
}

/* Change styles for cancel button and signup button on extra small screens */
@media screen and (max-width: 300px) {
  .cancelbtn, .signup {
    width: 100%;
  }
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
</div>

<form id="SignUp" style="width:700px; margin: auto; margin-top: 50px;" method="post" enctype="multipart/form-data">
    <h3 style="text-align: center;">Sign Up and Start Creating Today!</h3>
    <div class="w3-container">
 
            
           <p>Please fill in this form to create an account.</p>
      <hr>
          <label><b>Username</b></label>
    <label id="username_msg" class="err_msg"></label>
     <input class="w3-input w3-border" id="username" type="text" placeholder="Enter Username" size="30" name="username">
          
      <label><b>Email</b></label>
    <label id="email_msg" class="err_msg"></label>
      <input class="w3-input w3-border" id="email" type="text" placeholder="Enter Email" size="30" name="email" required>

      <label><b>Password</b></label>
     <label id="pswd_msg" class="err_msg"></label>
        
      <input class="w3-input w3-border" type="password" placeholder="Enter Password" size="30" name="pwd" required>

      <label><b>Re-enter Password</b></label>
     <label id="reEnter_msg" class="err_msg"></label>
        
      <input class="w3-input w3-border" type="password" placeholder="Re-enter Password" size="30"   name="pwd2" required>
    
     <div class="clearfix">
      <button type="button" class="cancelbtn">Cancel</button>
      <button type="submit"  class="signup" name="Signup" value="Signup">Sign-up</button>
        </div>

          <a class="dropdown-item" href="login.py">Already have an account? Sign in</a>
      </div>
  
</form>
    
</body>
</html>

"""

@app.route("/signup", methods=['GET', 'POST'])

def signup():
    if request.method == 'POST':
        server = 'tcp:expressyourself.database.windows.net'
        database = 'expressyourself'
        username = 'cs476'
        password = '$up3rSecret'
        driver= '{ODBC Driver 13 for SQL Server}'
        cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = cnxn.cursor()
        try:
            cursor.execute("INSERT INTO users VALUES ('{username}', '{email}', '{password}', 0, null)".format(
                username=str(request.form.get("username")),
                email=str(request.form.get("email")),
                password=str(request.form.get("pwd"))))
            cnxn.commit()
            return redirect('/login')
        except pyodbc.Error as ex:
            sqlstate = ex.args[1]
            return sqlstate
        return "Sign up request received"
    else:
        signupHTML = SignUp()
        signupHTML.setHTML()
        return signupHTML.getHTML()
    
