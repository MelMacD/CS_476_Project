from code import app
from flask import request
    
@app.route("/", methods=['GET', 'POST'])

def main():
    if request.method == 'POST':
        return "error"
    else:
        return """
<!DOCTYPE html>
<html lang="en">
<title>Express Yourself</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<script
  src="https://code.jquery.com/jquery-3.3.1.min.js"
  integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8="
  crossorigin="anonymous"></script>
<script src="static/logInOut.js"></script>
<style>
body {font-family: "Lato", sans-serif}
.mySlides {display: none}
 
</style>
<body>

<!-- Navbar -->
<div class="w3-top">
  <div class="w3-bar w3-black w3-card">
    <a href="/" class="w3-bar-item w3-button w3-padding-large">Home</a>
    <a href="#" class="w3-bar-item w3-button w3-padding-large logout" style="display: none;">Logout</a>
    <a href="login" class="w3-bar-item w3-button w3-padding-large login">Login</a>
    <a href="signup" class="w3-bar-item w3-button w3-padding-large signup">Sign-up</a>
  </div>
</div>

<!-- Page content -->
<div class="w3-content" style="max-width:2000px;margin-top:46px">

  <!-- Automatic Slideshow Images -->
  <div class="mySlides w3-display-container w3-center">
    <img src="static/picture1.jpg" style="width:100%">
    <div class="w3-display-bottommiddle w3-container w3-text-white w3-padding-32 w3-hide-small">
      <h3>Create your own Personal Space</h3>
    </div>
  </div>
  <div class="mySlides w3-display-container w3-center">
    <img src="static/picture2.jpg" style="width:100%">
    <div class="w3-display-bottommiddle w3-container w3-text-white w3-padding-32 w3-hide-small">
      <h3>Express Yourself in Your Own Blog</h3>  
    </div>
  </div>
  <div class="mySlides w3-display-container w3-center">
    <img src="static/picture3.jpg" style="width:100%">
    <div class="w3-display-bottommiddle w3-container w3-text-white w3-padding-32 w3-hide-small">
      <h3>View Content Created by Others</h3>  
    </div>
  </div>

  <!-- express yourself -->
  <div class="w3-container w3-content w3-center w3-padding-64" style="max-width:800px" id="band">
    <h2 class="w3-wide">Express Yourself </h2>
    <p class="w3-opacity"><i>We love the freedom of you expressing your thought in own way</i></p>
    <p class="w3-justify">We have created an easy way of creating your blog. We believe that anything is possible the right blog builder. Whether you are a begginner at creating your website or a pro, we have got you covered. </p>
    <div class="w3-row w3-padding-32">
      <div class="w3-third">
        <p>Freedom of Thought</p>
        <img src="static/tea.jpg" class="w3-round w3-margin-bottom" alt="Random Name" style="width:60%">
      </div>
      <div class="w3-third">
        <p>Creative Blog</p>
        <img src="static/holiday.jpg" class="w3-round w3-margin-bottom" alt="Random Name" style="width:60%">
      </div>
      <div class="w3-third">
        <p>Own Your Webpage</p>
        <img src="static/travel.jpg" class="w3-round" alt="Random Name" style="width:60%">
      </div>
    </div>
  </div>

  <!-- The blog Section -->
  <div class="w3-black" id="tour">
    <div class="w3-container w3-content w3-padding-64" style="max-width:800px">
      <h2 class="w3-wide w3-center">CREATE YOUR OWN BLOG</h2>
      
      <div class="w3-row-padding w3-padding-32" style="margin:0 -16px">
        <div class="w3-third w3-margin-bottom">
          <img src="static/picture4.jpg" alt="Paris" style="width:100%" class="w3-hover-opacity">
          <div class="w3-container w3-white">
            <p><b>CREATE BLOG</b></p>
            <button id="createBlog" class="w3-button w3-black w3-margin-bottom">Get Started</button>
          </div>
        </div>
        <div class="w3-third w3-margin-bottom">
          <img src="static/forest.jpg" alt="San Francisco" style="width:100%" class="w3-hover-opacity">
          <div class="w3-container w3-white">
            <p><b>VIEW BLOG LIST</b></p>
<a href="bloglist" class="w3-button w3-black w3-margin-bottom">VIEW </a>
          </div>
        
        </div>
      </div>
    </div>
  </div>
  </div>
  
<!-- End Page Content -->
</div>

<!-- Footer -->
<footer class="w3-container w3-padding-64 w3-center w3-opacity w3-light-grey w3-xlarge">
  <i class="fa fa-facebook-official w3-hover-opacity"></i>
  <i class="fa fa-instagram w3-hover-opacity"></i>
  <i class="fa fa-snapchat w3-hover-opacity"></i>
  <i class="fa fa-pinterest-p w3-hover-opacity"></i>
  <i class="fa fa-twitter w3-hover-opacity"></i>
  <i class="fa fa-linkedin w3-hover-opacity"></i>
  <p class="w3-medium">Powered by <a href="https://www.w3schools.com/w3css/default.asp" target="_blank">w3.css</a></p>
    <p> Created by MEL & IYANU</p>
</footer>

<script>
// Automatic Slideshow - change image every 4 seconds
var myIndex = 0;
carousel();

function carousel() {
    var i;
    var x = document.getElementsByClassName("mySlides");
    for (i = 0; i < x.length; i++) {
       x[i].style.display = "none";  
    }
    myIndex++;
    if (myIndex > x.length) {myIndex = 1}    
    x[myIndex-1].style.display = "block";  
    setTimeout(carousel, 4000);    
}

// Used to toggle the menu on small screens when clicking on the menu button
function myFunction() {
    var x = document.getElementById("navDemo");
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
    } else { 
        x.className = x.className.replace(" w3-show", "");
    }
}

// When the user clicks anywhere outside of the modal, close it
var modal = document.getElementById('ticketModal');
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
    var modal = document.getElementById('blogModal');
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
}
</script>

</body>
</html>
"""
