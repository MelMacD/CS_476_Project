from code import app
from flask import request
    
@app.route("/", methods=['GET', 'POST'])

def main():
    if request.method == 'POST':
        return "nothing"
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
<style>
body {font-family: "Lato", sans-serif}
.mySlides {display: none}
 
</style>
<body>

<!-- Navbar -->
<div class="w3-top">
  <div class="w3-bar w3-black w3-card">
    <a class="w3-bar-item w3-button w3-padding-large w3-hide-medium w3-hide-large w3-right" href="javascript:void(0)" onclick="myFunction()" title="Toggle Navigation Menu"><i class="fa fa-bars"></i></a>
    <a href="main.py" class="w3-bar-item w3-button w3-padding-large">Home</a>
    <a href="login.py" class="w3-bar-item w3-button w3-padding-large w3-hide-small">Login</a>
    <a href="signup.py" class="w3-bar-item w3-button w3-padding-large w3-hide-small">Sign-up</a>
    <a href="#contact" class="w3-bar-item w3-button w3-padding-large w3-hide-small">Contact</a>
    
    </div>
    <a href="javascript:void(0)" class="w3-padding-large w3-hover-red w3-hide-small w3-right"><i class="fa fa-search"></i></a>
  </div>
</div>

<!-- Navbar on small screens (remove the onclick attribute if you want the navbar to always show on top of the content when clicking on the links) -->
<div id="navDemo" class="w3-bar-block w3-black w3-hide w3-hide-large w3-hide-medium w3-top" style="margin-top:46px">
  <a href="login.py" class="w3-bar-item w3-button w3-padding-large" onclick="myFunction()">Login</a>
  <a href="signup.py" class="w3-bar-item w3-button w3-padding-large" onclick="myFunction()">Sign-up</a>
  <a href="#contact" class="w3-bar-item w3-button w3-padding-large" onclick="myFunction()">CONTACT</a>

</div>

<!-- Page content -->
<div class="w3-content" style="max-width:2000px;margin-top:46px">

  <!-- Automatic Slideshow Images -->
  <div class="mySlides w3-display-container w3-center">
    <img src="static/picture1.jpg" style="width:100%">
    <div class="w3-display-bottommiddle w3-container w3-text-white w3-padding-32 w3-hide-small">
      <h3>Create the Website You want</h3>
      <p><b>Write Something</b></p>   
    </div>
  </div>
  <div class="mySlides w3-display-container w3-center">
    <img src="static/picture2.jpg" style="width:100%">
    <div class="w3-display-bottommiddle w3-container w3-text-white w3-padding-32 w3-hide-small">
      <h3>Express Yourself in Your Own Blog</h3>
      <p><b>Write Something</b></p>    
    </div>
  </div>
  <div class="mySlides w3-display-container w3-center">
    <img src="static/picture3.jpg" style="width:100%">
    <div class="w3-display-bottommiddle w3-container w3-text-white w3-padding-32 w3-hide-small">
      <h3>View professional Website and Blog</h3>
      <p><b>Write something</b></p>    
    </div>
  </div>

  <!-- express yourself -->
  <div class="w3-container w3-content w3-center w3-padding-64" style="max-width:800px" id="band">
    <h2 class="w3-wide">Express Yourself </h2>
    <p class="w3-opacity"><i>We love the freedom of you expressing your thought in own way</i></p>
    <p class="w3-justify">We have created an easy way of creating your blog. We believe that anything is possible the right website or blog builder. Whether you are cbegginner at creating your website or a pro, we have got you covered. </p>
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
        <p>Own Your Website</p>
        <img src="static/travel.jpg" class="w3-round" alt="Random Name" style="width:60%">
      </div>
    </div>
  </div>

  <!-- The blog Section -->
  <div class="w3-black" id="tour">
    <div class="w3-container w3-content w3-padding-64" style="max-width:800px">
      <h2 class="w3-wide w3-center">CREATE YOUR OWN BLOG</h2>
      <p class="w3-opacity w3-center"><i>WRITE SOMETHING</i></p><br>


      <div class="w3-row-padding w3-padding-32" style="margin:0 -16px">
        <div class="w3-third w3-margin-bottom">
          <img src="static/art.jpg" alt="New York" style="width:100%" class="w3-hover-opacity">
          <div class="w3-container w3-white">
            <p><b>PROFFESIONAL WEBSITE</b></p>
            <p class="w3-opacity">BEGINNING</p>
            <p>WRITE SOMETHING</p>
            <button class="w3-button w3-black w3-margin-bottom" onclick="document.getElementById('ticketModal').style.display='block'">Get Started</button>
          </div>
        </div>
        <div class="w3-third w3-margin-bottom">
          <img src="static/picture4.jpg" alt="Paris" style="width:100%" class="w3-hover-opacity">
          <div class="w3-container w3-white">
            <p><b>CREATIVE BLOG</b></p>
            <p class="w3-opacity">BEGINNING</p>
            <p>WRITE SOMETHING</p>
            <button class="w3-button w3-black w3-margin-bottom" onclick="document.getElementById('ticketModal').style.display='block'">Get Started</button>
          </div>
        </div>
        <div class="w3-third w3-margin-bottom">
          <img src="static/forest.jpg" alt="San Francisco" style="width:100%" class="w3-hover-opacity">
          <div class="w3-container w3-white">
            <p><b>VIEW BLOG LIST</b></p>
            <p class="w3-opacity">WELCOME</p>
            <p>WRITE SOMETHING</p>
<a href="bloglist.html" class="w3-button w3-black w3-margin-bottom">VIEW </a>
          </div>
        
        </div>
      </div>
    </div>
  </div>


  <div id="ticketModal" class="w3-modal">
    <div class="w3-modal-content w3-animate-top w3-card-4">
      <header class="w3-container w3-teal w3-center w3-padding-32"> 
        <span onclick="document.getElementById('ticketModal').style.display='none'" 
       class="w3-button w3-teal w3-xlarge w3-display-topright">×</span>
        <h2 class="w3-wide"><i class="fa fa-male w3-margin-right"></i>Sign-up</h2>
      </header>
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
      <input class="w3-input w3-border" type="password" placeholder="Enter Password" size="30" name="pwd" required>

       <label><b>Re-enter Password</b></label>
     <label id="reEnter_msg" class="err_msg"></label>
        
      <input class="w3-input w3-border" type="password" placeholder="Re-enter Password" size="30"   name="pwd2" required>
      
    
        
        <button class="w3-button w3-block w3-teal w3-padding-16 w3-section w3-right"  type="submit"  class="signup" name="Signup" value="Signup">Signup <i class="fa fa-check"></i></button>
        <button class="w3-button w3-red w3-section" onclick="document.getElementById('ticketModal').style.display='none'">Close <i class="fa fa-remove"></i></button>
          <a class="dropdown-item" href="login.py">Already have an account? Sign in</a>
        <p class="w3-right">Need <a href="#" class="w3-text-blue">help?</a></p>
      </div>
    </div>
  </div>

    

          
  <!-- The Contact Section -->
  <div class="w3-container w3-content w3-padding-64" style="max-width:800px" id="contact">
    <h2 class="w3-wide w3-center">CONTACT</h2>
    <p class="w3-opacity w3-center"><i> Drop a note!</i></p>
    <div class="w3-row w3-padding-32">
      <div class="w3-col m6 w3-large w3-margin-bottom">
        <i class="fa fa-map-marker" style="width:30px"></i> Regina, Canada<br>
        <i class="fa fa-phone" style="width:30px"></i> Phone: +3605551792<br>
        <i class="fa fa-envelope" style="width:30px"> </i> Email: mail@mail.com<br>
      </div>
      <div class="w3-col m6">
        <form action="/action_page.php" target="_blank">
          <div class="w3-row-padding" style="margin:0 -16px 8px -16px">
            <div class="w3-half">
              <input class="w3-input w3-border" type="text" placeholder="Name" required name="Name">
            </div>
            <div class="w3-half">
              <input class="w3-input w3-border" type="text" placeholder="Email" required name="Email">
            </div>
          </div>
          <input class="w3-input w3-border" type="text" placeholder="Message" required name="Message">
          <button class="w3-button w3-black w3-section w3-right" type="submit">SEND</button>
        </form>
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
    <p> Created by MEl & IYANU</p>
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