from code import app
import os
from flask import request
from werkzeug.utils import secure_filename


@app.route("/", methods=['GET', 'POST'])

def hello():
    if request.method == 'POST':
        APP_ROOT = os.path.dirname(os.path.abspath(__file__))
        UPLOAD_FOLDER = os.path.join(APP_ROOT, 'uploads\images')
        #ALLOWED_EXTENSIONS
        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
        file = request.files['testFile']
        if file:
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            return str(path)
        else:
            return "Invalid file"
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
