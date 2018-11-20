$(document).ready(function() {
    //Tasks:
    // 2. Make tab clickable
    $("li").on("click", function() {
        window.location = "https://expressyourself.azurewebsites.net/blogView?blogName=" + $(this).find("h1").text();
    });
    // 3. Implement searching
});
