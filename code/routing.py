from code import app


@app.route("/")

def hello():

    return """
<head>
<title>Test Page</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="stylesheet" href="static/bootstrap.css" />
</head>
    
<div class="border border-dark rounded">
    <h1>
        What is the title?
    </h1>
    <p>
        What is the content?
    </p>
</div>"""
