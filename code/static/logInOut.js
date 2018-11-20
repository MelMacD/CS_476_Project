$(document).ready(function() {
    let loginToken = document.cookie;
    // if logged in, hide login and signup in the navbar
    if (loginToken.indexOf("userId") != -1) {
        let values = loginToken.split("=");
        //values[1] is the user id
        $(".login").css("display", "none");
        $(".signup").css("display", "none");
    }
    // read cookie
    // if hit logout, remove cookie
});
