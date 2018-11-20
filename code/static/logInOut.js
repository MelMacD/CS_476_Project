$(document).ready(function() {
    let loginToken = document.cookie;
    // if logged in, hide login and signup in the navbar
    if (loginToken.indexOf("userId") != -1) {
        let values = loginToken.split("=");
        //values[1] is the user id
        $(".login").css("display", "none");
        $(".signup").css("display", "none");
        $(".logout").css("display", "block");
    }
    else {
        $(".login").css("display", "block");
        $(".signup").css("display", "block");
        $(".logout").css("display", "none");
    }
    
    $(".logout").on("click", function() {
        alert("logout");
    });
    // read cookie
    // if hit logout, remove cookie
});
