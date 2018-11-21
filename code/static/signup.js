let errorPresent;

$(document).ready(function() {
    $("#SignUp").on("submit", function(e) {
        errorPresent = false;
        usernameValidation();
        emailValidation();
        pwdValidation();
        pwdReentryValidation();
        if ( errorPresent == true ) {
            e.preventDefault()
        }
    });
});

function usernameValidation() {
    if ( $("#username").val().length > 15 ) {
        $("#username_msg").text("Username must not be more than 15 characters.");
        errorPresent = true;
    }
    else {
        $("#username_msg").text("");
    }
}

function emailValidation() {
    if ( $("#email").val().length > 30 ) {
        $("#email_msg").text("Email must not be more than 30 characters.");
        errorPresent = true;
    }
    else {
        $("#email_msg").text("");
    }
}

function pwdValidation() {
    if ( $("#password").val().length > 15 ) {
        $("#pswd_msg").text("Password must not be more than 15 characters.");
        errorPresent = true;
    }
    else {
        $("#pswd_msg").text("");
    }
}

function pwdReentryValidation() {
    if ( $("#rePassword").val() !== $("#password").val() ) {
        $("#reEnter_msg").text("Password fields must match.");
        errorPresent = true;
    }
    else {
        $("#reEnter_msg").text("");
    }
}
