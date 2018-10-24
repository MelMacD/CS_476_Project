from code import app


@app.route("/")

def hello():

    return """
<head>
<title>Test Page</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="stylesheet" href="static/bootstrap.css" />
<script src="https://code.jquery.com/jquery-1.12.4.js"></script>
<script src="static/jquery-ui.min.js"></script>
<link rel="stylesheet" type="text/css" href="//ajax.googleapis.com/ajax/libs/jqueryui/1.7.1/themes/base/jquery-ui.css"/>
<script>
$( function() {
  $( ".draggable" ).draggable().click(function() {
    $(this).draggable({ disabled: false });
    }).dblclick(function() {
      $(this).draggable({ disabled: true });
    });  
  $( ".resizable").resizable();
  
  $("div.video").mousedown( function() {
      $("#mask").show();
    }).mouseup( function() {
      $("#mask").hide();
    }).resizable();
});
</script>

<style>
    #mask {
        z-index: 5;
        position: absolute;
        top: 0;
        left: 0;
        width: 100%
        height: 100%
        display: none;
    }
</style>

</head>
<body>
<div class="border border-dark rounded draggable resizable">
    <h3 contenteditable="true">
        What is the title?
    </h3>
    <p contenteditable="true">
        What is the content?
    </p>
    <p contenteditable="false">
    <small>Click here to drag</small>
    </p>
</div>

<div class="draggable">
    <img class="resizable" src="static/very_important.jpg" width="500" height="500">
</div>

<div class="video">
  <div id="mask"></div>
    <iframe class="draggable" width="420" height="315" 
    src="https://www.youtube.com/embed/h2Lw9Zs98Gg" allowfullscreen</iframe>
</div>
</body>"""
