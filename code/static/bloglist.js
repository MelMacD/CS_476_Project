$(document).ready(function() {
    $("li").on("click", function() {
        window.location = "https://expressyourself.azurewebsites.net/blogView?blogName=" + $(this).find("h1").text();
    });
    $("#search").on("change", function() {
        let parameter = $(this).val().toLowerCase();
        $("li").each( function() {
            if ($(this).find("h1").text().toLowerCase().indexOf(parameter) == -1) {
                $(this).css("display", "none");
            }
            else {
                $(this).css("display", "block");
            }
        });
    });
});
