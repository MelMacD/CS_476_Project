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
                return '<div><h1>' + ref + '</h1><video width="420" height="315"><source src="' + ref + '" type="video/mp4"></video></div>'
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
<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.2/css/bootstrap-theme.min.css">
<script src="https://code.jquery.com/jquery-1.12.4.js"></script>
<script src="static/jquery-ui.min.js"></script>
<link rel="stylesheet" type="text/css" href="//ajax.googleapis.com/ajax/libs/jqueryui/1.7.1/themes/base/jquery-ui.css"/>
<script src="//netdna.bootstrapcdn.com/bootstrap/3.0.2/js/bootstrap.min.js"></script>
<script src="static/blogEditingHandlers.js"></script>
<link rel="stylesheet" href="static/blogEditingStyle.css" />
</head>
<body>
    <div id="buttons">
        <button id="enableEditing">Enable Edit Mode</button>
        <button id="editPost" type="button" data-toggle="modal" data-target="#exampleModal">Edit Post</button>
        <button id="editImage" type="button" data-toggle="modal" data-target="#exampleModal">Edit Image</button>
        <button id="editVideo" type="button" data-toggle="modal" data-target="#exampleModal">Edit Video</button>
        <button style="display:none;" id="disableEditing">Exit Edit Mode</button>
        <button style="display:none;" id="addText">Add Post</button>
        <button style="display:none;" id="addImage">Add Image</button>
        <button style="display:none;" id="addVideo">Add Video</button>
    </div>
    
<!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Edit</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        Error
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <button id="saveChanges" type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
</body>"""
