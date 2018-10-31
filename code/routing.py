from code import app
import os
from flask import request


@app.route("/", methods=['GET', 'POST'])

def hello():
    if request.method == 'POST':
        return str(os.path.basename('uploads'))
    else:
        return """
<head>
<title>Test Page</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="stylesheet" href="static/bootstrap.css" />
<script src="https://code.jquery.com/jquery-1.12.4.js"></script>
<script src="static/jquery-ui.min.js"></script>
<script src="static/blogEditingHandlers.js"></script>
<link rel="stylesheet" type="text/css" href="//ajax.googleapis.com/ajax/libs/jqueryui/1.7.1/themes/base/jquery-ui.css"/>
</head>
<body>
    <div id="buttons">
        <button id="enableEditing">Enable Edit Mode</button>
        <button style="display:none;" id="disableEditing">Exit Edit Mode</button>
        <button style="display:none;" id="addText">Add Post</button>
        <button style="display:none;" id="addImage">Add Image</button>
        <button style="display:none;" id="addVideo">Add Video</button>
    </div>
    <div>
        <form id="LogIn" method="post" enctype="multipart/form-data">
            <input type="file" name="testFile">
            <input type="submit" name="Login" value="Login"/>
        </form>
    </div>
</body>"""
