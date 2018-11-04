var postHtml = `<div id="mask" class="border border-dark rounded draggable resizable" style="width: 350px; height: 400px;">
                 <button class="editPost" type="button" style="position: absolute; top: 0; right: 0;" data-toggle="modal" data-target="#exampleModal">Edit Post</button>
                 <div id="originalContent">
                   <h3>What is the title?</h3><p>What is the content?</p>
                 </div>
               </div>`;
var imageHtml = `<div class="draggable">
                <img class="resizable" src="static/very_important.jpg" width="500" height="500">
                </div>`;
var videoHtml = `<div class="draggable resizable">
                <iframe class="resizable" width="420" height="315"
                src="https://www.youtube.com/embed/h2Lw9Zs98Gg" </iframe></div>`;
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
            <label for="recipient-name" class="col-form-label">Get image from URL:</label>
            <input type="text" class="form-control" id="imageUrl">
          </div>
          <div class="form-group">
            <label for="message-text" class="col-form-label">Choose image from library:</label>
            <select id="imageBlobSelector">
              <option value="none">None</option>
            </select>
          </div>
          <div class="form-group">
            <label for="message-text" class="col-form-label">Upload image from computer:</label>
            <input type="file" class="form-control" id="imageFile">
          </div>
          <div class="form-group">
            <label for="message-text" class="col-form-label">Preview:</label>
            <div>
              <img id="imagePreview" src="" width="300" height="300">
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

// Need default media
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
        $("#saveChanges").click(function () {
            alert("Hello, I'll try to only execute for a text post");
        });
    });
  
    $("#editImage").click(function() {
        $("div.modal-body").html(imageEditHtml);
        $("#imageUrl").on("change", function() {
            $("#imagePreview").attr("src", $(this).val());
        });
        $.getJSON("/getBlobImages", function(data) {
            let i;
            for (i = 0; i < data.length; i++) {
              $("#imageBlobSelector").append( "<option value='" + data[i] + "'>" + data[i] + "</option>" );
            }
        });
        $("#imageBlobSelector").on("change", function() {
            let url = 'https://expressiveblob.blob.core.windows.net/images/' + $(this).val()
            $("#imagePreview").attr("src", url);
        });
      // allow for preview of any sized image, maybe scale down if too big
        $("#saveChanges").click(function () {
            alert("Hello, I'll try to only execute for an image");
        });
    });
  
    $("#editVideo").click(function() {
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
        $("#saveChanges").click(function () {
            alert("Hello, I'll try to only execute for a video");
        });
    });
});

function setupDraggableResizable() {
    $( ".draggable" ).draggable().click(function() {
        $(this).draggable({ 
            disabled: false,
            iframeFix: true,
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
