let errorPresent = false;

$(document).ready(function() {
    $("#SignUp").on("submit", function(e) {
        e.preventDefault();
        usernameValidation();
        emailValidation();
        pwdValidation();
        pwdReentryValidation();
        if ( errorPresent == true ) {
            //e.preventDefault()
        }
    });
});

function usernameValidation() {
    if ( $("#username").val().length > 15 ) {
        $("#username_msg").text("Username must not be more than 15 characters.");
    }
    else {
        $("#username_msg").text("");
    }
    errorPresent = true;
}

function emailValidation() {
    if ( $("#email").val().length > 30 ) {
        $("#email_msg").text("Email must not be more than 30 characters.");
    }
    else {
        $("#email_msg").text("");
    }
    errorPresent = true;
}

function pwdValidation() {
    if ( $("#password").val().length > 15 ) {
        $("#pswd_msg").text("Password must not be more than 15 characters.");
    }
    else {
        $("#pswd_msg").text("");
    }
    errorPresent = true;
}

function pwdReentryValidation() {
    if ( $("#rePassword").val() !== $("#password").val() ) {
        $("#reEnter_msg").text("Password fields must match.");
    }
    else {
        $("#reEnter_msg").text("");
    }
    errorPresent = true;
}
