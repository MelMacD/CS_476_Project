from code import app
import os
import json
from flask import request
from werkzeug.utils import secure_filename
from azure.storage.blob import BlockBlobService, PublicAccess

@app.route("/getBlobImages")

def getBlobImages():
    block_blob_service = BlockBlobService(account_name='expressiveblob', account_key='F2G8lu/eZ6PduDIJFksWvuItZdhf+GONR2wgwgSsJMUO4s0mMdFI6PiC7K7ypcMSOH6m5kPhn2C9ketBRQiyKA==')
    generator = block_blob_service.list_blobs('images')
    blobList = []
    for blob in generator:
        blobList.append(blob.name)
    return json.dumps(blobList)

@app.route("/getBlobVideos")

def getBlobVideos():
    block_blob_service = BlockBlobService(account_name='expressiveblob', account_key='F2G8lu/eZ6PduDIJFksWvuItZdhf+GONR2wgwgSsJMUO4s0mMdFI6PiC7K7ypcMSOH6m5kPhn2C9ketBRQiyKA==')
    generator = block_blob_service.list_blobs('videos')
    blobList = []
    for blob in generator:
        blobList.append(blob.name)
    return json.dumps(blobList)

@app.route("/uploadBlobImage", methods=['GET', 'POST'])

def uploadBlobImage():
    if request.method == 'POST':
        return "Well okay"
        #try:
        #    file = request.files['imageFile']
        #    if file:
        #        filename = secure_filename(file.filename)
        #        block_blob_service = BlockBlobService(account_name='expressiveblob', account_key='F2G8lu/eZ6PduDIJFksWvuItZdhf+GONR2wgwgSsJMUO4s0mMdFI6PiC7K7ypcMSOH6m5kPhn2C9ketBRQiyKA==')
        #        container = 'images'
        #        block_blob_service.create_blob_from_stream(container, filename, file)
        #        return "Success"
        #    else:
        #        return "Invalid File"
        #except Exception as e:
        #    return e
    else:
        return "Error"

@app.route("/", methods=['GET', 'POST'])

def hello():
    if request.method == 'POST':
        return str(request.form)
    else:
        return """
<head>
<title>Test Page</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="stylesheet" href="static/bootstrap.css" />
<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.2/css/bootstrap-theme.min.css">
<script
  src="https://code.jquery.com/jquery-3.3.1.min.js"
  integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8="
  crossorigin="anonymous"></script>
<script src="static/jquery-ui.min.js"></script>
<link rel="stylesheet" type="text/css" href="//ajax.googleapis.com/ajax/libs/jqueryui/1.7.1/themes/base/jquery-ui.css"/>
<script src="//netdna.bootstrapcdn.com/bootstrap/3.0.2/js/bootstrap.min.js"></script>
<script src="static/blogEditingHandlers.js"></script>
<link rel="stylesheet" href="static/blogEditingStyle.css" />
</head>
<body>
    <div id="buttons">
        <button id="enableEditing">Enable Edit Mode</button>
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
