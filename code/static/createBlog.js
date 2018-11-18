// TODO: Enforce validation on input fields
$(document).ready(function() {
    $("#useUrl").on("change", function () {
        $(".urlChange").css( "display", "block" );
        $(".imageChange").css( "display", "none" );
    });
    $("#useLibrary").on("change", function () {
        $(".urlChange").css( "display", "none" );
        $(".imageChange").css( "display", "block" );
    });
  
    $("#imageUrl").on("change", function() {
        imageUrl = $(this).val();
        $("#imagePreview").attr("src", imageUrl);
    });
  
    $.getJSON("/getBlobImages", function(data) {
        let i;
        $("#imageBlobSelector").empty();
        $("#imageBlobSelector").append( "<option value='none'>None</option>" );
        for (i = 0; i < data.length; i++) {
            $("#imageBlobSelector").append( "<option value='" + data[i] + "'>" + data[i] + "</option>" );
        }
    });
    $("#imageBlobSelector").on("change", function() {
        libraryUrl = 'https://expressiveblob.blob.core.windows.net/images/' + $(this).val()
        $("#imagePreview").attr("src", libraryUrl);
    });
    
    $(".cancelbtn").on("click", function() {
        window.location.href = "https://expressyourself.azurewebsites.net/";
    });
    
    $("#create").submit(function(e) {// prevent default, change to form on submit
        e.preventDefault();
        $.ajax({
            url: "/createBlog",
            type: "post",
            data: "",
            success: function() {
                alert("Blog created.");
                //window.location.href = "https://expressyourself.azurewebsites.net/";
            },
            error: function() {
                alert("An error occurred. Could not create blog.");
            }
        });
    });
});
