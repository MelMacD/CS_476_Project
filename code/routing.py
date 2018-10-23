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
  $( "#draggable" ).draggable().resizable().click(function() {
    $(this).draggable({ disabled: false });
    }).dblclick(function() {
      $(this).draggable({ disabled: true });
    });  
});
</script>
</head>
<body>
<div id="draggable" class="border border-dark rounded">
    <h3 contenteditable="true">
        What is the title?
    </h3>
    <p contenteditable="true">
        What is the content?
    </p>
</div>
</body>"""
