
$(document).ready(function() {
    $("#SignUp").on("submit", function(e) {
        e.preventDefault();
        let errorPresent = false;
        usernameValidation();
        
        if ( errorPresent == true ) {
            //e.preventDefault()
        }
    });
});

function usernameValidation() {
    alert ($("#username").val().length);
    if ( $("#username").val().length > 15 ) {
        $("username_msg").text("Username must not be empty and not more than 15 characters.");
    }
    else {
        $("username_msg").text("");
    }
}

function emailValidation() {
    if ( $("#email").val().length > 30 ) {
        $("email_msg").text("Email must not be empty and not more than 30 characters.");
    }
    else {
        $("email_msg").text("");
    }
}
