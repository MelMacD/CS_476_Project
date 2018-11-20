$(document).ready(function() {
    //Tasks:
    // 1. Populate empty sources with the default image
    $("img").each( function() {
        if ($(this).attr("src") === "") {
            $(this).attr("src", "/static/default.js");
        }
    });
    // 2. Make tab clickable
    // 3. Implement searching
});
