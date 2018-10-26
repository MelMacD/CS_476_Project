var postHtml = '<div class="border border-dark rounded draggable resizable" contenteditable="true">' +
               '<h3>What is the title?</h3><p>What is the content?</p>' +
               '<p><small>Click here to drag</small></p>';

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
    });
});
