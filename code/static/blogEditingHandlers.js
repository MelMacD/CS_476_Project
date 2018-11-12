let postId = 0;
let imageId = 0;
let videoId = 0;

var postHtml = `<div class="border border-dark rounded draggable resizable newPost" style="width: 350px; height: 400px; z-index: 0;">
                 <button class="editPost edit" type="button" style="position: absolute; top: 0; right: 0;" data-toggle="modal" data-target="#exampleModal">Edit</button>
                 <div id="originalContent" style="width: 100%; height: 100%; background-color: white;">
                   <h3>What is the title?</h3><p>What is the content?</p>
                 </div>
               </div>`;
var imageHtml = `<div class="draggable resizableAspect newImage" style="width: 300px; height: 300px; z-index: 0;">
                   <button class="editImage edit" type="button" style="position: absolute; top: 0; right: 0;" data-toggle="modal" data-target="#exampleModal">Edit</button>
                   <img src="/static/default.gif" style="width: 100%; height: 100%;">
                </div>`;
var videoHtml = `<div class="draggable resizableAspect newVideo" style="width: 420; height: 283; z-index: 0;">
                   <button class="editVideo edit" type="button" style="position: absolute; top: 0; right: 0; z-index: 1;" data-toggle="modal" data-target="#exampleModal">Edit</button>
                   <div id="mask" class="edit"></div>
                   <video id="libraryVideo" style="display: none; width: 100%; height: 100%;"controls>
                   <source src="" type="video/mp4">
                   </video>
                   <iframe id="youtubeVideo" allowFullScreen='allowFullScreen' src="" style="width: 100%; height: 100%;"</iframe>
             </div>
                 </div>`;
var postEditHtml = `<form>
          <div class="form-group">
            <label for="recipient-name" class="col-form-label">Header:</label>
            <input type="text" class="form-control" id="postTitle">
          </div>
          <div class="form-group">
            <label for="message-text" class="col-form-label">Content:</label>
            <textarea class="form-control" id="postContent"></textarea>
          </div>
          <div class="form-group">
            <label for="message-text" class="col-form-label">Font Colour:</label>
            <input type="color" class="form-control" id="postFontColor" value="#000000">
          </div>
          <div class="form-group">
            <label for="message-text" class="col-form-label">Background Colour:</label>
            <input type="color" class="form-control" id="postBackgroundColor" value="#ffffff">
          </div>
          <div class="form-group">
            <label for="message-text" class="col-form-label">Preview:</label>
            <div id="postPreviewDiv" class="border border-dark rounded">
              <h3 id="postPreviewTitle"></h3>
              <p id="postPreviewContent"></p>
            </div>
          </div>
        </form>`;
var imageEditHtml = `<form id="uploadImage" method="post" enctype="multipart/form-data">
          <div class="form-group">
            <label class="radio-inline">
              <input type="radio" id="useUrl" name="optradio" checked> Get image from URL
            </label>
            <label class="radio-inline">
              <input type="radio" id="useLibrary" name="optradio" value="library"> Get image from Library
            </label>
          </div>
          <div class="form-group">
            <label for="recipient-name" class="col-form-label">Enter URL:</label>
            <input type="text" class="form-control" id="imageUrl">
          </div>
          <div class="form-group">
            <label for="message-text" class="col-form-label">Choose image:</label>
            <select id="imageBlobSelector" class="form-control" disabled>
              <option value="none">None</option>
            </select>
          </div>
          <div class="form-group">
            <label for="message-text" class="col-form-label">Upload image to library:</label>
            <input type="file" name="imageFile" class="form-control" id="imageFile" disabled>
            </br>
            <input id="submitImageUpload" type="submit" name="upload" value="Upload Image" disabled/>
            <p id="loading" style="display:none;">Uploading...</p>
          </div>
          <div class="form-group">
            <label for="message-text" class="col-form-label">Preview:</label>
            <div>
              <img id="imagePreview" src="/static/default.gif">
            </div>
          </div>
        </form>`;
var videoEditHtml = `<form id="uploadVideo" method="post" enctype="multipart/form-data">
          <div class="form-group">
            <label class="radio-inline">
              <input type="radio" id="useUrlVideo" name="optradio" checked> Get video from YouTube
            </label>
            <label class="radio-inline">
              <input type="radio" id="useLibraryVideo" name="optradio" value="library"> Get video from Library
            </label>
          </div>
          <div class="form-group">
            <label for="recipient-name" class="col-form-label">Enter URL:</label>
            <input type="text" class="form-control" id="videoUrl">
          </div>
          <div class="form-group">
            <label for="message-text" class="col-form-label">Choose video:</label>
            <select id="videoBlobSelector" class="form-control" disabled>
              <option value="none">None</option>
            </select>
          </div>
          <div class="form-group">
            <label for="message-text" class="col-form-label">Upload video from computer:</label>
            <input type="file" class="form-control" id="videoFile" disabled>
            </br>
            <input id="submitVideoUpload" type="submit" name="upload" value="Upload Video" disabled/>
            <p id="loading" style="display:none;">Uploading...</p>
          </div>
          <div class="form-group">
            <label for="message-text" class="col-form-label">Preview:</label>
            <div>
              <video id="libraryVideoPreview" style="display: none;" width="420" height="315" controls>
                <source src="" type="video/mp4">
              </video>
              <iframe id="youtubeVideoPreview" width="420" height="315" src="" </iframe>
             </div>
          </div>
        </form>`;

let hiddenFormData = {};

function buildPost( post, update ) {
    return {
        // parameter "10" implies decimal radix, as 0 could be treated as hex
        width: parseInt(post.css("width"), 10),
        height: parseInt(post.css("height"), 10),
        top: parseInt(post.css("top"), 10),
        left: parseInt(post.css("left"), 10),
        depth: parseInt(post.css("z-index"), 10),
        title: post.find("h3").text(),
        content: post.find("p").text(),
        backgroundColor: post.find("div").css("background-color"),
        fontColor: post.find("div").css("color"),
        isUpdate: update
    }
}

function buildImage( image, update ) {
    return {
        // parameter "10" implies decimal radix, as 0 could be treated as hex
        width: parseInt(image.css("width"), 10),
        height: parseInt(image.css("height"), 10),
        top: parseInt(image.css("top"), 10),
        left: parseInt(image.css("left"), 10),
        depth: parseInt(image.css("z-index"), 10),
        source: image.find("img").attr("src"),
        isUpdate: update
    }
}

function buildVideo( video, update ) {
    let videoSource = video.find("video").attr("src")
    let youtubeSource = video.find("iframe").attr("src")
    let setSource = "";
    if (videoSource == "" && youtubeSource != "") {
        setSource = youtubeSource;
    }
    else if (youtubeSource == "" && videoSource != "") {
        setSource = videoSource;
    }
    else {
        alert("Cannot submit a video without a source defined.");
    }
    return {
        // parameter "10" implies decimal radix, as 0 could be treated as hex
        width: parseInt(video.css("width"), 10),
        height: parseInt(video.css("height"), 10),
        top: parseInt(video.css("top"), 10),
        left: parseInt(video.css("left"), 10),
        depth: parseInt(video.css("z-index"), 10),
        source: setSource,
        isUpdate: update
    }
}

function getNewElementId( selector ) {
    maxId = 0;
    selector.each(function() {
        alert("found post");
        if (parseInt($(this).attr("id"), 10) > maxId) {
            maxId = parseInt($(this).attr("id"), 10)
            alert(maxId);
        }
    });
    //increment by 1 so new id is unique if post already exists
    maxId += 1;
    alert(maxId);
    return maxId;
}

function logContent( update ) {
   // use different selector for new posts and already existing posts
    let postSelector = $(".post");
    let imageSelector = $(".image");
    let videoSelector = $(".video");
    if (!update) {
        postSelector = $(".newPost");
        imageSelector = $(".newImage");
        videoSelector = $(".newVideo");
    }
    postSelector.each(function() {
        let id;
        if (update) {
            id = $(this).attr("id")
        }
        else {
            id = "post" + postId;
            alert(id);
            postId++;
        }
        hiddenFormData[id] = buildPost($(this), update);
    });
  
    imageSelector.each(function() {
        let id;
        if (update) {
            id = $(this).attr("id")
        }
        else {
            id = "image" + imageId;
            imageId++;
        }
        hiddenFormData[id] = buildImage($(this), update);
    });
    videoSelector.each(function() {
        let id;
        if (update) {
            id = $(this).attr("id")
        }
        else {
            id = "video" + videoId;
            videoId++;
        }
        hiddenFormData[id] = buildVideo($(this), update);
    });
    console.log(hiddenFormData);
}

$(document).ready(function() {
    $(".edit").css("display", "none");
  
    postId = getNewElementId( $(".post") );
    imageId = getNewElementId( $(".image") );
    videoId = getNewElementId( $(".video") );
  
    $("#save").click(function() {
        logContent(false);
        logContent(true);
        $.ajax({
            url: "/blogView",
            type: "post",
            data: JSON.stringify(hiddenFormData),
            contentType: "application/json",
            success: function(data) {
              alert("Changes saved.");
              console.log(data)
              //location.reload();
            },
            error: function(xhr, ajaxOptions, thrownError) {
              alert("An error occurred. Could not save changes.");
              console.log(xhr.status);
              console.log(thrownError);
            },
        });
    });
  
    $("#enableEditing").click(function () {
        $(".edit").css("display", "block");
        $("#enableEditing").css("display", "none");
        $("#disableEditing").css("display", "inline");
        $("#addText").css("display", "inline");
        $("#addImage").css("display", "inline");
        $("#addVideo").css("display", "inline");
        $("#changeBackground").css("display", "inline");
        $("#changeFont").css("display", "inline");
        setupDraggableResizable();
        $("div[contenteditable]").attr("contenteditable", "true");
    });
    
    $("#disableEditing").click(function() {
        $("#enableEditing").css("display", "inline");
        $("#disableEditing").css("display", "none");
        $("#addText").css("display", "none");
        $("#addImage").css("display", "none");
        $("#addVideo").css("display", "none");
        $("#changeBackground").css("display", "none");
        $("#changeFont").css("display", "none");
        $( ".draggable" ).draggable({ disabled: true });
        $( ".resizable").resizable({ disabled: true });
        $( ".resizableAspect").resizable({ disabled: true });
        $("div[contenteditable]").attr("contenteditable", "false");
        $(".edit").css("display", "none");
    });
    
    $("#addText").click(function() {
        $("#blogBody").prepend(postHtml);
        setupDraggableResizable();
    });
  
    $("#addImage").click(function() {
        $("#blogBody").prepend(imageHtml);
        setupDraggableResizable();
    });
  
    $("#addVideo").click(function() {
        $("#blogBody").prepend(videoHtml);
        setupDraggableResizable();
    });
  
    $("#changeBackground").on("change", function() {
        $("body").css("background-color", $(this).val());
    });
  
    $("#changeFont").on("change", function() {
        $("#blogBody").css("font-family", $(this).val());
    });
  
    $("body").on("click", ".editPost", function() {
        let currentPost = $(this);
        $("div.modal-body").html(postEditHtml);
      
        $("#postTitle").on("change", function() {
            $("#postPreviewTitle").text($(this).val());
        });
        $("#postContent").on("change", function() {
            $("#postPreviewContent").text($(this).val());
        });
        $("#postFontColor").on("change", function() {
            $("#postPreviewTitle").css("color", $(this).val());
            $("#postPreviewContent").css("color", $(this).val());
        });
        $("#postBackgroundColor").on("change", function() {
            $("#postPreviewDiv").css("background-color", $(this).val());
        });
        $("#saveChanges").off("click");
        $("#saveChanges").on("click", function () {
            currentPost.parent().find("#originalContent h3").text($("#postTitle").val());
            currentPost.parent().find("#originalContent p").text($("#postContent").val());
            currentPost.parent().find("#originalContent").css("color", $("#postFontColor").val());
            currentPost.parent().find("#originalContent").css("background-color", $("#postBackgroundColor").val());
            $("#exampleModal").modal("hide");
        });
    });
  
    $("body").on("click", ".editImage", function() {
        let currentPost = $(this);
        let imageUrl = '';
        let libraryUrl = '';
        $("div.modal-body").html(imageEditHtml);
      
        $("#useUrl").on("change", function () {
            $("#imageUrl").prop( "disabled", false );
            $("#imageBlobSelector").prop( "disabled", true );
            $("#imageFile").prop( "disabled", true );
            $("#submitImageUpload").prop( "disabled", true );
        });
      
        $("#useLibrary").on("change", function () {
            $("#imageUrl").prop( "disabled", true );
            $("#imageBlobSelector").prop( "disabled", false );
            $("#imageFile").prop( "disabled", false );
            $("#submitImageUpload").prop( "disabled", false );
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

        $("#saveChanges").off("click");
        $("#saveChanges").on("click", function () {
            let url = '';
            if($("#useUrl").prop( "checked" )) {
              url = imageUrl;
            }
            else {
              url = libraryUrl;
            }
            currentPost.parent().find("img").attr("src", url);
            currentPost.parent().width($("#imagePreview").width());
            currentPost.parent().height($("#imagePreview").height());
            $("#exampleModal").modal("hide");
        });
      
        $("#uploadImage").submit( function (e) {
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
  
    $("body").on("click", ".editVideo", function() {
        let currentPost = $(this);
        let youtubeUrl = '';
        let libraryUrl = '';
        $("div.modal-body").html(videoEditHtml);
      
        $("#useUrlVideo").on("change", function () {
            $("#videoUrl").prop( "disabled", false );
            $("#videoBlobSelector").prop( "disabled", true );
            $("#videoFile").prop( "disabled", true );
            $("#submitVideoUpload").prop( "disabled", true );
        });
      
        $("#useLibraryVideo").on("change", function () {
            $("#videoUrl").prop( "disabled", true );
            $("#videoBlobSelector").prop( "disabled", false );
            $("#videoFile").prop( "disabled", false );
            $("#submitVideoUpload").prop( "disabled", false );
        });
      
        $("#videoUrl").on("change", function() {
            youtubeUrl = $(this).val().replace("watch?v=", "embed/");
            $("#youtubeVideoPreview").css("display", "block");
            $("#youtubeVideoPreview").attr("src", youtubeUrl);
            $("#libraryVideoPreview").css("display", "none");
        });
        $.getJSON("/getBlobVideos", function(data) {
            let i;
            $("#videoBlobSelector").empty();
            $("#videoBlobSelector").append( "<option value='none'>None</option>" );
            for (i = 0; i < data.length; i++) {
              $("#videoBlobSelector").append( "<option value='" + data[i] + "'>" + data[i] + "</option>" );
            }
        });
        $("#videoBlobSelector").on("change", function() {
            libraryUrl = 'https://expressiveblob.blob.core.windows.net/videos/' + $(this).val()
            $("#libraryVideoPreview").css("display", "block");
            $("#libraryVideoPreview").attr("src", libraryUrl);
            $("#youtubeVideoPreview").css("display", "none");
        });
        $("#saveChanges").off("click");
        $("#saveChanges").on("click", function () {
            if ($("#useLibraryVideo").prop( "checked" )) {
              currentPost.parent().find("#libraryVideo").attr("src", libraryUrl);
              currentPost.parent().find("#libraryVideo").css("display", "block");
              currentPost.parent().find("#youtubeVideo").css("display", "none");
            }
            else {
              currentPost.parent().find("#youtubeVideo").attr("src", youtubeUrl);
              currentPost.parent().find("#libraryVideo").css("display", "none");
              currentPost.parent().find("#youtubeVideo").css("display", "block");
            }
            $("#exampleModal").modal("hide");
        });
      
        $("#uploadVideo").submit( function (e) {
          e.preventDefault();
          let formData = new FormData(this);
          formData.append("file", $("#videoFile").get(0).files[0]);
          $.ajax({
            url: "/uploadBlobVideo",
            type: "post",
            data: formData,
            cache: false,
            contentType: false,
            processData: false,
            success: function() {
              $.getJSON("/getBlobVideos", function(data) {
                  let i;
                  $("#videoBlobSelector").empty();
                  $("#videoBlobSelector").append( "<option value='none'>None</option>" );
                  for (i = 0; i < data.length; i++) {
                      $("#videoBlobSelector").append( "<option value='" + data[i] + "'>" + data[i] + "</option>" );
                  }
              });
              alert("Upload successful.");
            },
            error: function() {
              alert("An error occurred. Could not upload video.");
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
});

function setupDraggableResizable() {
    $( ".draggable" ).draggable({
            disabled: false,
            snap: true,
            containment: "window",
            stack: ".draggable"
    });
    $( ".resizableAspect").resizable({
        disabled: false,
        aspectRatio: true
    });
    $( ".resizable").resizable({
        disabled: false,
        aspectRatio: false
    });
    $( ".draggable" ).css("position", "absolute");
}
