// TODO: Enforce validation on input fields
// TODO: Get upload image working
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
    
    $("#create").submit(function(e) {
        e.preventDefault();
        formData = {
            blogName: $("#username").val(),
            imageSource: $("#imagePreview").attr("src"),
            description: $("#description").val()
        };
        console.log(formData);
        $.ajax({
            url: "/createBlog",
            type: "post",
            data: JSON.stringify(formData),
            contentType: "application/json",
            success: function(data) {
                console.log(data);
                alert("Blog created.");
                window.location.href = "https://expressyourself.azurewebsites.net/";
            },
            error: function(xhr, ajaxOptions, thrownError) {
                alert("An error occurred. Could not create blog.");
                console.log(xhr.status);
                console.log(thrownError);
            }
        });
    });
    
        $("#submitImageUpload").submit( function (e) {
          e.preventDefault();
          let formData = new FormData(this);
          formData.append("file", $("#imageFile").get(0).files[0]);
          $.ajax({
            url: "/uploadBlobImage",
            type: "post",
            data: formData,
            cache: false,
            contentType: false,
            processData: false,
            success: function() {
              $.getJSON("/getBlobImages", function(data) {
                  let i;
                  $("#imageBlobSelector").empty();
                  $("#imageBlobSelector").append( "<option value='none'>None</option>" );
                  for (i = 0; i < data.length; i++) {
                      $("#imageBlobSelector").append( "<option value='" + data[i] + "'>" + data[i] + "</option>" );
                  }
              });
              alert("Upload successful.");
            },
            error: function() {
              alert("An error occurred. Could not upload image.");
            },
            beforeSend: function() {
              $("#loading").css("display", "block");
            },
            complete: function() {
              $("#loading").css("display", "none");
            }
          });
      });
});
