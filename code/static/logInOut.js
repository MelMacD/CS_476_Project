$(document).ready(function() {
    let loginToken = document.cookie;
    // if logged in, hide login and signup in the navbar
    if (loginToken.indexOf("userId") != -1) {
        alert("Logged in");
        let values = loginToken.split("=");
        alert(values[1]);
    }
    // read cookie
    // if hit logout, remove cookie
});
