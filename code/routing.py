from code import app


@app.route("/")

def hello():

    return """
<head>
<title>Test Page</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="stylesheet" href="static/bootstrap.css" />
</head>
    
<div class="border border-dark rounded" contenteditable="true">
    <h3>
        What is the title?
    </h3>
    <p>
        What is the content?
    </p>
</div>"""
