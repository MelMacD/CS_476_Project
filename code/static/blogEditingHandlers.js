let postId = 0;
let imageId = 0;
let videoId = 0;

var reactHtml = `<div class="reactBar" style="height: 38px; background-color: lightgray; position: absolute; width: 100%; bottom: 0px;">
                   <div class="dropdown">
                     <button class="btn btn-secondary dropdown-toggle react" style="position: absolute; top: 0; right: 0; z-index: 1;" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">React</button>
                     <div class="dropdown-menu">
                       <div style="margin-left: 13px;">
                         <button class="reactLike" type="button"><i class="em em---1"></i></button>
                         <button class="reactDislike" type="button"><i class="em em--1"></i></button>
                         <button class="reactClap" type="button"><i class="em em-clap"></i></button>
                       </div>
                       <div style="margin-left: 13px;">
                         <button class="reactHeart" type="button"><i class="em em-heart"></i></button>
                         <button class="reactSmile" type="button"><i class="em em-smile"></i></button>
                         <button class="reactCry" type="button"><i class="em em-sob"></i></button>
                       </div>
                       <div style="margin-left: 13px;">
                         <button class="reactSilly" type="button"><i class="em em-stuck_out_tongue_winking_eye"></i></button>
                         <button class="reactAngry" type="button"><i class="em em-angry"></i></button>
                         <button class="reactShock" type="button"><i class="em em-scream"></i></button>
                       </div>
                     </div>
                   </div>
                 </div>`;
var postHtml = `<div class="border border-dark rounded draggable resizable newPost" style="width: 350px; height: 400px; z-index: 0;">
                  <div class="dropdown edit">
                    <button class="btn btn-secondary dropdown-toggle" style="position: absolute; top: 0; right: 0;" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Edit</button>
                    <div class="dropdown-menu">
                      <button class="editPost dropdown-item" type="button" data-toggle="modal" data-target="#exampleModal">Change Content</button>
                      <button type="button" class="dropdown-item addThread">Add Thread</button>
                      <button type="button" class="dropdown-item deletePost">Delete</button>
                    </div>
                  </div>
                 <div id="originalContent" style="width: 100%; height: 100%; background-color: white;">
                   <h3>What is the title?</h3><p>What is the content?</p>
                 </div>
                 ${reactHtml}
               </div>`;
var imageHtml = `<div class="draggable resizableAspect newImage" style="width: 300px; height: 300px; z-index: 0;">
                   <div class="dropdown edit">
                     <button class="btn btn-secondary dropdown-toggle" style="position: absolute; top: 0; right: 0;" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Edit</button>
                     <div class="dropdown-menu">
                       <button class="editImage dropdown-item" type="button" data-toggle="modal" data-target="#exampleModal">Change Content</button>
                       <button type="button" class="dropdown-item addThread">Add Thread</button>
                       <button type="button" class="dropdown-item deletePost">Delete</button>
                     </div>
                   </div>
                    <img src="/static/default.gif" style="width: 100%; height: 100%;">
                   ${reactHtml}
                </div>`;
var videoHtml = `<div class="draggable resizableAspect newVideo" style="width: 420; height: 283; z-index: 0;">
                   <div class="dropdown edit">
                     <button class="btn btn-secondary dropdown-toggle" style="position: absolute; top: 0; right: 0; z-index: 1;" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Edit</button>
                     <div class="dropdown-menu">
                       <button class="editVideo dropdown-item" type="button" data-toggle="modal" data-target="#exampleModal">Change Content</button>
                       <button type="button" class="dropdown-item addThread">Add Thread</button>
                       <button type="button" class="dropdown-item deletePost">Delete</button>
                     </div>
                   </div>
                   <div id="mask" class="edit"></div>
                   ${reactHtml}
                   <video id="libraryVideo" style="display: none; width: 100%; height: 100%;"controls>
                   <source src="" type="video/mp4">
                   </video>
                   <iframe id="youtubeVideo" allowFullScreen='allowFullScreen' src="" style="width: 100%; height: 100%;"</iframe>
                 </div>`;
var threadHtml = `<div class="newThread">
                    <div style="height: 200px; overflow-y: scroll; background-color: white;">
                      <ul class="comments list-group" style="font-size: 14px;">
                      </ul>
                    </div>
                    <div class="input-group">
                      <input type="text" class="form-control" placeholder="Enter a comment">
                      <div class="input-group-append">
                        <button class="btn btn-outline-secondary submitComment" type="button" style="background-color: darkgray;">Enter</button>
                      </div>
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

function buildPost( post, action ) {
    hasThread = 0;
    if (post.find(".newThread").length !== 0) {
        hasThread = 1;
    }
    if (post.attr("delete") == "true") {
        action = "delete";
    }
    return {
        // parameter "10" implies decimal radix, as 0 could be treated as hex
        width: parseInt(post.css("width"), 10),
        height: parseInt(post.css("height"), 10),
        top: parseInt(post.css("top"), 10),
        left: parseInt(post.css("left"), 10),
        depth: parseInt(post.css("z-index"), 10),
        title: post.find("h3").text(),
        content: post.find("p").text(),
        backgroundColor: post.find("#originalContent").css("background-color"),
        fontColor: post.find("#originalContent").css("color"),
        action: action,
        hasThread: hasThread
    }
}

function buildImage( image, action ) {
    hasThread = 0;
    if (image.find(".newThread").length !== 0) {
        hasThread = 1;
    }
    if (image.attr("delete") == "true") {
        action = "delete";
    }
    return {
        // parameter "10" implies decimal radix, as 0 could be treated as hex
        width: parseInt(image.css("width"), 10),
        height: parseInt(image.css("height"), 10),
        top: parseInt(image.css("top"), 10),
        left: parseInt(image.css("left"), 10),
        depth: parseInt(image.css("z-index"), 10),
        source: image.find("img").attr("src"),
        action: action,
        hasThread: hasThread
    }
}

function buildVideo( video, action ) {
    hasThread = 0;
    if (video.find(".newThread").length !== 0) {
        hasThread = 1;
    }
    if (video.attr("delete") == "true") {
        action = "delete";
    }
    let videoSource = video.find("video").attr("src");
    let youtubeSource = video.find("iframe").attr("src");
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
        action: action,
        hasThread: hasThread
    }
}

function getNewElementId( selector ) {
    maxId = 0;
    selector.each(function() {
        if (parseInt($(this).attr("id").match(/(\d+)$/)[0], 10) > maxId) {
            maxId = parseInt($(this).attr("id").match(/(\d+)$/)[0], 10)
        }
    });
    //increment by 1 so new id is unique if post already exists
    maxId += 1;
    return maxId;
}

function logContent( action ) {
   // use different selector for new posts and already existing posts
    let postSelector = $(".post");
    let imageSelector = $(".image");
    let videoSelector = $(".video");
    if (action == "insert") {
        postSelector = $(".newPost");
        imageSelector = $(".newImage");
        videoSelector = $(".newVideo");
    }
    postSelector.each(function() {
        let id;
        if (action == "update") {
            id = $(this).attr("id");
        }
        else if (action == "insert"){
            id = "post" + postId;
            postId++;
        }
        hiddenFormData[id] = buildPost($(this), action);
    });
  
    imageSelector.each(function() {
        let id;
        if (action == "update") {
            id = $(this).attr("id");
        }
        else if (action == "insert") {
            id = "image" + imageId;
            imageId++;
        }
        hiddenFormData[id] = buildImage($(this), action);
    });
    videoSelector.each(function() {
        let id;
        if (action == "update") {
            id = $(this).attr("id");
        }
        else if (action == "insert") {
            id = "video" + videoId;
            videoId++;
        }
        hiddenFormData[id] = buildVideo($(this), action);
    });
    console.log(hiddenFormData);
}

function rgbToHex(rgb) {
  let a = rgb.split("(")[1].split(")")[0].split(",");
  return "#" + a.map(function(x) {
    x = parseInt(x).toString(16);
    return (x.length == 1) ? "0"+x : x;
  }).join("");
}

$(document).ready(function() {
    $(".edit").css("display", "none");
    $("#save").css("display", "none");
  
    postId = getNewElementId( $(".post") );
    imageId = getNewElementId( $(".image") );
    videoId = getNewElementId( $(".video") );
  
    $("#save").click(function() {
        logContent("insert");
        logContent("update");
        // add to the hiddenFormData the blog information
        hiddenFormData["blog"] = {
            backgroundColor: $("body").css("background-color"),
            font: $("#blogBody").css("font-family")
        };
        console.log(hiddenFormData);
        $.ajax({
            url: "/blogView",
            type: "post",
            data: JSON.stringify(hiddenFormData),
            contentType: "application/json",
            success: function(data) {
              alert("Changes saved");
              console.log(data);
              location.reload();
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
        $("#save").css("display", "inline");
        $("#enableEditing").css("display", "none");
        $("#disableEditing").css("display", "inline");
        $("#addText").css("display", "inline");
        $("#addImage").css("display", "inline");
        $("#addVideo").css("display", "inline");
        $("#changeBackground").css("display", "inline");
        $("#changeFont").css("display", "inline");
        setupDraggableResizable();
        $("div[contenteditable]").attr("contenteditable", "true");
        $(".submitComment").each( function() {
            $(this).prop("disabled", true);
        });
        $(".react").each( function() {
            $(this).prop("disabled", true);
        });
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
        $("#save").css("display", "none");
        $(".submitComment").each( function() {
            $(this).prop("disabled", false);
        });
        $(".react").each( function() {
            $(this).prop("disabled", false);
        });
    });
    
    $("#addText").click(function() {
        $("#blogBody").prepend(postHtml);
        setupDraggableResizable();
        $(".react").each( function() {
            $(this).prop("disabled", true);
        });
    });
  
    $("#addImage").click(function() {
        $("#blogBody").prepend(imageHtml);
        setupDraggableResizable();
        $(".react").each( function() {
            $(this).prop("disabled", true);
        });
    });
  
    $("#addVideo").click(function() {
        $("#blogBody").prepend(videoHtml);
        setupDraggableResizable();
        $(".react").each( function() {
            $(this).prop("disabled", true);
        });
    });
  
    $("#changeBackground").on("change", function() {
        $("body").css("background-color", $(this).val());
    });
  
    $("#changeFont").on("change", function() {
        $("#blogBody").css("font-family", $(this).val());
    });
  
    $("body").on("click", ".editPost", function() {
        let currentPost = $(this).parent().parent().parent();
        $("div.modal-body").html(postEditHtml);
      
        // initialize values on modal and preview according to previous values
        $("#postTitle").val(currentPost.find("#originalContent h3").text());
        $("#postContent").val(currentPost.find("#originalContent p").text());
        $("#postFontColor").val(rgbToHex(currentPost.find("#originalContent").css("color")));
        $("#postBackgroundColor").val(rgbToHex(currentPost.find("#originalContent").css("background-color")));
        $("#postPreviewTitle").text(currentPost.find("#originalContent h3").text());
        $("#postPreviewContent").text(currentPost.find("#originalContent p").text());
        $("#postPreviewTitle").css("color", currentPost.find("#originalContent").css("color"));
        $("#postPreviewContent").css("color", currentPost.find("#originalContent").css("color"));
        $("#postPreviewDiv").css("background-color", currentPost.find("#originalContent").css("background-color"));
      
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
            currentPost.find("#originalContent h3").text($("#postTitle").val());
            currentPost.find("#originalContent p").text($("#postContent").val());
            currentPost.find("#originalContent").css("color", $("#postFontColor").val());
            currentPost.find("#originalContent").css("background-color", $("#postBackgroundColor").val());
            $("#exampleModal").modal("hide");
        });
    });
  
    $("body").on("click", ".editImage", function() {
        let currentPost = $(this).parent().parent().parent();
        let imageUrl = '';
        let libraryUrl = '';
        $("div.modal-body").html(imageEditHtml);
      
        // initialize values on modal and preview according to previous values
        $("#imagePreview").attr("src", currentPost.find("img").attr("src"));
      
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
            currentPost.find("img").attr("src", url);
            currentPost.width($("#imagePreview").width());
            currentPost.height($("#imagePreview").height());
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
        let currentPost = $(this).parent().parent().parent();
        let youtubeUrl = '';
        let libraryUrl = '';
        $("div.modal-body").html(videoEditHtml);
      
        // initialize values on modal and preview according to previous values
        if (currentPost.find("#libraryVideo").attr("src") != "" && currentPost.find("#youtubeVideo").attr("src") == "") {
            $("#libraryVideoPreview").css("display", "block");
            $("#libraryVideoPreview").attr("src", currentPost.find("#libraryVideo").attr("src"));
        }
        else if (currentPost.find("#libraryVideo").attr("src") == "" && currentPost.find("#youtubeVideo").attr("src") != "") {
            $("#youtubeVideoPreview").attr("src", currentPost.find("#youtubeVideo").attr("src"));
        }
      
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
              currentPost.find("#libraryVideo").attr("src", libraryUrl);
              currentPost.find("#libraryVideo").css("display", "block");
              currentPost.find("#youtubeVideo").css("display", "none");
              currentPost.find("#youtubeVideo").attr("src", "");
            }
            else {
              currentPost.find("#youtubeVideo").attr("src", youtubeUrl);
              currentPost.find("#libraryVideo").css("display", "none");
              currentPost.find("#libraryVideo").attr("src", "");
              currentPost.find("#youtubeVideo").css("display", "block");
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
    $("body").on("click", ".deletePost", function() {
        let currentPost = $(this).parent().parent().parent();
        if (currentPost.hasClass("post") || currentPost.hasClass("image") || currentPost.hasClass("video")) {
            currentPost.attr("delete", "true");
            currentPost.css("display", "none");
        }
        else {
            currentPost.remove();
        }
    });
  
    $("body").on("click", ".addThread", function() {
        let current = $(this).parent().parent().parent();
        current.append(threadHtml);
        // change add thread button to remove thread
        $(this).removeClass("addThread");
        $(this).addClass("removeThread");
        $(this).text("Remove Thread");
        $(".submitComment").each( function() {
            $(this).prop("disabled", true);
        });
    });
  
    $("body").on("click", ".removeThread", function() {
        let current = $(this).parent().parent().parent();
        current.find(".newThread, .thread").remove();
        // change remove thread button to add thread
        $(this).removeClass("removeThread");
        $(this).addClass("addThread");
        $(this).text("Add Thread");
    });
  
    $("body").on("click", ".submitComment", function() {
        let current = $(this).parent().parent().parent().parent();
        formData = {
            attachedToId: current.attr("id"),
            comment: current.find("input").val()
        };
        $.ajax({
            url: "/uploadComment",
            type: "post",
            data: JSON.stringify(formData),
            contentType: "application/json",
            success: function(data) {
              alert("Comment upload successful");
              console.log(data);
              location.reload();
            },
            error: function(xhr, ajaxOptions, thrownError) {
              alert("An error occurred. Could not upload comment.");
              console.log(xhr.status);
              console.log(thrownError);
            }
        });
    });

    function uploadReaction(element, emoji) {
        let current = element.parent().parent().parent().parent().parent();
        formData = {
            attachedToId: current.attr("id"),
            emote: emoji
        };
        $.ajax({
            url: "/uploadReaction",
            type: "post",
            data: JSON.stringify(formData),
            contentType: "application/json",
            success: function(data) {
              alert("Reaction successful");
              console.log(data);
              location.reload();
            },
            error: function(xhr, ajaxOptions, thrownError) {
              alert("An error occurred. Could not react.");
              console.log(xhr.status);
              console.log(thrownError);
            }
        });
    }
  
    $("body").on("click", ".reactLike", function() {
        uploadReaction($(this), "em---1");
    });
    $("body").on("click", ".reactDislike", function() {
        uploadReaction($(this), "em--1");
    });
    $("body").on("click", ".reactClap", function() {
        uploadReaction($(this), "em-clap");
    });
    $("body").on("click", ".reactHeart", function() {
        uploadReaction($(this), "em-heart");
    });
    $("body").on("click", ".reactSmile", function() {
        uploadReaction($(this), "em-smile");
    });
    $("body").on("click", ".reactCry", function() {
        uploadReaction($(this), "em-sob");
    });
    $("body").on("click", ".reactSilly", function() {
        uploadReaction($(this), "em-stuck_out_tongue_winking_eye");
    });
    $("body").on("click", ".reactAngry", function() {
        uploadReaction($(this), "em-angry");
    });
    $("body").on("click", ".reactShock", function() {
        uploadReaction($(this), "em-scream");
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
