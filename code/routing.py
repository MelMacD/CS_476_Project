from code import app


@app.route("/")

def hello():

    return """
<head>
<title>Test Page</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="stylesheet" href="static/bootstrap.css" />
<script src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.3.1.min.js"></script>
<script>
$( function() {
  $( "#draggable" ).draggable();
});
</script>
</head>
    
<div id="draggable" class="border border-dark rounded" contenteditable="true">
    <h3>
        What is the title?
    </h3>
    <p>
        What is the content?
    </p>
</div>"""
