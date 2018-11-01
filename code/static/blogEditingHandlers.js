var postHtml = '<div class="border border-dark rounded draggable resizable">' +
               //'<button type="button" data-toggle="modal" data-target="#exampleModal">Edit Post</button>' +
               '<h3>What is the title?</h3><p>What is the content?</p>' +
               '</div>';
var imageHtml = '<div class="draggable">' +
                '<img class="resizable" src="static/very_important.jpg" width="500" height="500">' +
                '</div>';
var videoHtml = '<div class="draggable resizable">' +
                '<iframe class="resizable" width="420" height="315"' +
                'src="https://www.youtube.com/embed/h2Lw9Zs98Gg" </iframe></div>';
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
            <label for="message-text" class="col-form-label">Upload image from computer:</label>
            <input type="file" class="form-control" id="imageFile">
          </div>
        </form>`;
var videoEditHtml = `<form>
          <div class="form-group">
            <label for="recipient-name" class="col-form-label">Get video from YouTube URL:</label>
            <input type="text" class="form-control" id="videoUrl">
          </div>
          <div class="form-group">
            <label for="message-text" class="col-form-label">Upload video from computer:</label>
            <input type="file" class="form-control" id="videoFile">
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
  
    $("#editPost").click(function() {
        $("div.modal-body").html(postEditHtml);
        $("#postTitle").on("blur", function() {
            alert($(this).val());
        });
        $("#postContent").on("blur", function() {
            alert($(this).val());
        });
        $("#postFontColor").on("change", function() {
            alert($(this).val());
        });
        $("#postBackgroundColor").on("change", function() {
            alert($(this).val());
        });
    });
  
    $("#editImage").click(function() {
        $("div.modal-body").html(imageEditHtml);
    });
  
    $("#editVideo").click(function() {
        $("div.modal-body").html(videoEditHtml);
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
