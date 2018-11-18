from code import app
from flask import request, redirect
import pyodbc


class CreateBlog:
    def __init__(self):
        self.html = self.setHtml()
    
    def getHtml(self):
        return self.html
    
    def setHtml(self):
        return """
<!DOCTYPE html>
<html lang="en">
<title>Sign-up Form</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.2/css/bootstrap-theme.min.css">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<script
  src="https://code.jquery.com/jquery-3.3.1.min.js"
  integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8="
  crossorigin="anonymous"></script>
<script src="static/jquery-ui.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
<script src="static/createBlog.js"></script>
<style>
body {font-family: "Lato", sans-serif}
.mySlides {display: none}
    
     {box-sizing: border-box
}
    /* Full-width input fields */
  input[type=text], input[type=password], textarea {
  width: 100%;
  padding: 15px;
  margin: 5px 0 22px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}
input[type=text]:focus, input[type=password]:focus, textarea:focus {
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
<form id="create" style="width:500px" method="post" enctype="multipart/form-data">
    <div class="w3-container">
           <p>Please fill in this form to create a blog.</p>
      <hr>
          <label><b>Blog Name</b></label>
    <label id="username_msg" class="err_msg"></label>
     <input id="username" type="text" placeholder="Enter a unique name for your blog" size="30" name="username">
    <label><b>Identifying Picture</b></label> 
    <form id="uploadImage" method="post" enctype="multipart/form-data">
          <div class="form-group">
            <label class="radio-inline">
              <input type="radio" id="useUrl" name="optradio" checked> Get image from URL
            </label>
            <label class="radio-inline">
              <input type="radio" id="useLibrary" name="optradio" value="library"> Get image from Library
            </label>
          </div>
          <div class="form-group urlChange">
            <label for="recipient-name" class="col-form-label">Enter URL:</label>
            <input type="text" class="form-control" id="imageUrl" placeholder="Link an image">
          </div>
          <div class="form-group imageChange" style="display: none;">
            <label for="message-text" class="col-form-label">Choose image:</label>
            <select id="imageBlobSelector" class="form-control">
              <option value="none">None</option>
            </select>
          </div>
          <div class="form-group imageChange" style="display: none;">
            <label for="message-text" class="col-form-label">Upload image to library:</label>
            <input type="file" name="imageFile" class="form-control" id="imageFile">
            </br>
            <input id="submitImageUpload" type="submit" name="upload" value="Upload Image"/>
            <p id="loading" style="display:none;">Uploading...</p>
          </div>
          <div class="form-group">
            <label for="message-text" class="col-form-label">Preview:</label>
            <div>
              <img id="imagePreview" src="/static/default.gif">
            </div>
          </div>
        </form>
      <label><b>Description</b></label>
     <div class="form-group">
         <textarea style="height: 200px;" id="description" placeholder="Enter the subject matter of your blog"></textarea>
     </div>
     <div class="clearfix">
      <button type="button" class="cancelbtn">Cancel</button>
      <button type="submit"  class="signup submitForm" name="Signup" value="submit">Submit</button>
        </div>
      </div>
  
</form>
    
</body>
</html>"""
      
@app.route("/createBlog", methods=['GET', 'POST'])

def createBlog():
    if request.method == 'POST':
        return str(requestData)
    else:
        form = CreateBlog()
        return form.getHtml()
