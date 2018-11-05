var postHtml = `<div class="border border-dark rounded draggable resizable" style="width: 350px; height: 400px;">
                 <button class="editPost" type="button" style="position: absolute; top: 0; right: 0;" data-toggle="modal" data-target="#exampleModal">Edit</button>
                 <div id="originalContent" style="width: 100%; height: 100%; background-color: white;">
                   <h3>What is the title?</h3><p>What is the content?</p>
                 </div>
               </div>`;
var imageHtml = `<div class="draggable resizable" style="width: 300px; height: 300px;">
                   <button class="editImage" type="button" style="position: absolute; top: 0; right: 0;" data-toggle="modal" data-target="#exampleModal">Edit</button>
                   <img src="/static/default.gif" style="width: 100%; height: 100%;">
                </div>`;
var videoHtml = `<div class="draggable resizable" style="width: 420; height: 315;">
                   <button class="editVideo" type="button" style="position: absolute; top: 0; right: 0;" data-toggle="modal" data-target="#exampleModal">Edit</button>
                   <div id="mask"></div>
                   <iframe src="https://www.youtube.com/embed/h2Lw9Zs98Gg" style="width: 100%; height: 100%;"</iframe>
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
var imageEditHtml = `<form>
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
            <input type="file" class="form-control" id="imageFile" disabled>
          </div>
          <div class="form-group">
            <label for="message-text" class="col-form-label">Preview:</label>
            <div>
              <img id="imagePreview" src="/static/default.gif">
            </div>
          </div>
        </form>`;
var videoEditHtml = `<form>
          <div class="form-group">
            <label for="recipient-name" class="col-form-label">Get video from YouTube URL:</label>
            <input type="text" class="form-control" id="videoUrl">
          </div>
          <div class="form-group">
            <label for="message-text" class="col-form-label">Choose image from library:</label>
            <select id="videoBlobSelector">
              <option value="none">None</option>
            </select>
          </div>
          <div class="form-group">
            <label for="message-text" class="col-form-label">Upload video from computer:</label>
            <input type="file" class="form-control" id="videoFile">
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

$(document).ready(function() {
    $("#enableEditing").click(function () {
        $("#enableEditing").css("display", "none");
        $("#disableEditing").css("display", "inline");
        $("#addText").css("display", "inline");
        $("#addImage").css("display", "inline");
        $("#addVideo").css("display", "inline");
        setupDraggableResizable();
        $("div[contenteditable]").attr("contenteditable", "true");
    });
    
    $("#disableEditing").click(function() {
        $("#enableEditing").css("display", "inline");
        $("#disableEditing").css("display", "none");
        $("#addText").css("display", "none");
        $("#addImage").css("display", "none");
        $("#addVideo").css("display", "none");
        $( ".draggable" ).draggable({ disabled: true });
        $( ".resizable").resizable({ disabled: true });
        $("div[contenteditable]").attr("contenteditable", "false");
    });
    
    $("#addText").click(function() {
        $(document.body).append(postHtml);
        setupDraggableResizable();
    });
  
    $("#addImage").click(function() {
        $(document.body).append(imageHtml);
        setupDraggableResizable();
    });
  
    $("#addVideo").click(function() {
        $(document.body).append(videoHtml);
        setupDraggableResizable();
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
        });
      
        $("#useLibrary").on("change", function () {
            $("#imageUrl").prop( "disabled", true );
            $("#imageBlobSelector").prop( "disabled", false );
            $("#imageFile").prop( "disabled", false );
        });
               
        $("#imageUrl").on("change", function() {
            imageUrl = $(this).val();
            $("#imagePreview").attr("src", imageUrl);
        });
        $.getJSON("/getBlobImages", function(data) {
            let i;
            for (i = 0; i < data.length; i++) {
              $("#imageBlobSelector").append( "<option value='" + data[i] + "'>" + data[i] + "</option>" );
            }
        });
        $("#imageBlobSelector").on("change", function() {
            libraryUrl = 'https://expressiveblob.blob.core.windows.net/images/' + $(this).val()
            $("#imagePreview").attr("src", libraryUrl);
        });
      // allow for preview of any sized image, maybe scale down if too big
        $("#saveChanges").off("click");
        $("#saveChanges").on("click", function () {
            let url = '';
            if($("#imageUrl").prop( "checked" )) {
              alert("this works dw");
              url = imageUrl;
            }
            else {
              url = libraryUrl;
            }
            currentPost.parent().find("img").attr("src", url);
            currentPost.parent().find("img").width($("#imagePreview").width());
            currentPost.parent().find("img").height($("#imagePreview").height());
            $("#exampleModal").modal("hide");
        });
    });
  
    $("body").on("click", ".editVideo", function() {
        let currentPost = $(this);
        $("div.modal-body").html(videoEditHtml);
        $("#videoUrl").on("change", function() {
            let processedUrl = $(this).val().replace("watch?v=", "embed/");
            $("#youtubeVideoPreview").css("display", "block");
            $("#youtubeVideoPreview").attr("src", processedUrl);
            $("#libraryVideoPreview").css("display", "none");
        });
        $.getJSON("/getBlobVideos", function(data) {
            let i;
            for (i = 0; i < data.length; i++) {
              $("#videoBlobSelector").append( "<option value='" + data[i] + "'>" + data[i] + "</option>" );
            }
        });
        $("#videoBlobSelector").on("change", function() {
            let url = 'https://expressiveblob.blob.core.windows.net/videos/' + $(this).val()
            $("#libraryVideoPreview").css("display", "block");
            $("#libraryVideoPreview").attr("src", url);
            $("#youtubeVideoPreview").css("display", "none");
        });
        $("#saveChanges").off("click");
        $("#saveChanges").on("click", function () {
            alert("Hello, I'll try to only execute for a video");
        });
    });
});

function setupDraggableResizable() {
    $( ".draggable" ).draggable().click(function() {
        $(this).draggable({ 
            disabled: false,
            snap: true,
            containment: "window",
            stack: ".draggable" });
    }).dblclick(function() {
        $(this).draggable({ disabled: true });
    });  
    $( ".resizable").resizable({
        aspectRatio: true,
        grid: [ 10, 10 ]
    });
}
