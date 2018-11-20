$(document).ready(function() {
    let loginToken = document.cookie;
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
        document.cookie = "userId=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    });
});
