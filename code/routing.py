from code import app
import os
from flask import request
from werkzeug.utils import secure_filename
from azure.storage.blob import BlockBlobService, PublicAccess


@app.route("/", methods=['GET', 'POST'])

def hello():
    if request.method == 'POST':
        try:
            file = request.files['testFile']
            if file:
                filename = secure_filename(file.filename)
                block_blob_service = BlockBlobService(account_name='expressiveblob', account_key='F2G8lu/eZ6PduDIJFksWvuItZdhf+GONR2wgwgSsJMUO4s0mMdFI6PiC7K7ypcMSOH6m5kPhn2C9ketBRQiyKA==')
                container = 'videos'#or images
                block_blob_service.create_blob_from_stream(container, filename, file)
                ref =  'https://'+ 'expressiveblob' + '.blob.core.windows.net/' + container + '/' + filename
                return '<div class="draggable resizable">' +
                '<iframe class="resizable" width="420" height="315"' +
                'src="' + ref + '" </iframe></div>';
            else:
                return "Invalid file"
        except Exception as e:
            return e
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
