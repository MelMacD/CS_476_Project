var postHtml = '<div class="border border-dark rounded draggable resizable" contenteditable="true">' +
               '<h3>What is the title?</h3><p>What is the content?</p>' +
               '</div>';
var imageHtml = '<div class="draggable">' +
                '<img class="resizable" src="static/very_important.jpg" width="500" height="500">' +
                '</div>';
var videoHtml = '<div class="draggable resizable">' +
                '<iframe class="resizable" width="420" height="315"' +
                'src="https://www.youtube.com/embed/h2Lw9Zs98Gg" </iframe></div>';

// Need default media
$(document).ready(function() {
    $("#enableEditing").click(function () {
        $("#enableEditing").css("display", "none");
        $("#disableEditing").css("display", "inline");
        $("#addText").css("display", "inline");
        $("#addImage").css("display", "inline");
        $("#addVideo").css("display", "inline");
    });
    
    $("#disableEditing").click(function() {
        $("#enableEditing").css("display", "inline");
        $("#disableEditing").css("display", "none");
        $("#addText").css("display", "none");
        $("#addImage").css("display", "none");
        $("#addVideo").css("display", "none");
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
