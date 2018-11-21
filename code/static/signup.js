
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
    if ( $("#username").val() == "" || $("#username").val() > 15 ) {
        $("username_msg").text("Username must not be empty and not more than 15 characters.");
    }
    else {
        $("username_msg").text("");
    }
}
