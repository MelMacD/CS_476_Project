$(document).ready(function() {
    //Tasks:
    // 1. Populate empty sources with the default image
    $("img").each( function() {
        if ($(this).attr("src") === "") {
            $(this).attr("src", "/static/default.js");
        }
    });
    // 2. Make tab clickable
    $("li").on("click", function() {
        alert("clicked list item");
        alert($(this).find("h1").text());
        //window.location = "https://expressyourself.azurewebsites.net/bloglist?blogName=test";
    });
    // 3. Implement searching
});
