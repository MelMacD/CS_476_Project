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
<script>
$( function() {
  $( "#draggable" ).draggable().click(function() {
    $(this).draggable({ disabled: false });
    }).dblclick(function() {
      $(this).draggable({ disabled: true });
    });
    
  $( "#draggable" ).resizable();  
});
</script>
</head>
<body>
<div id="draggable" class="border border-dark rounded" contenteditable="true">
    <h3>
        What is the title?
    </h3>
    <p>
        What is the content?
    </p>
</div>
</body>"""
