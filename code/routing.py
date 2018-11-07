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
        try:
            file = request.files['imageFile']
            if file:
                filename = secure_filename(file.filename)
                block_blob_service = BlockBlobService(account_name='expressiveblob', account_key='F2G8lu/eZ6PduDIJFksWvuItZdhf+GONR2wgwgSsJMUO4s0mMdFI6PiC7K7ypcMSOH6m5kPhn2C9ketBRQiyKA==')
                container = 'images'
                block_blob_service.create_blob_from_stream(container, filename, file)
                return "Success"
            else:
                return "Invalid File"
        except Exception as e:
            return e
    else:
        return "Error"

@app.route("/uploadBlobVideo", methods=['GET', 'POST'])

def uploadBlobVideo():
    if request.method == 'POST':
        try:
            file = request.files['videoFile']
            if file:
                filename = secure_filename(file.filename)
                block_blob_service = BlockBlobService(account_name='expressiveblob', account_key='F2G8lu/eZ6PduDIJFksWvuItZdhf+GONR2wgwgSsJMUO4s0mMdFI6PiC7K7ypcMSOH6m5kPhn2C9ketBRQiyKA==')
                container = 'videos'
                block_blob_service.create_blob_from_stream(container, filename, file)
                return "Success"
            else:
                return "Invalid File"
        except Exception as e:
            return e
    else:
        return "Error"
    
@app.route("/blogView", methods=['GET', 'POST'])

def hello():
    if request.method == 'POST':
        return str(request.files)
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
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
        <a class="navbar-brand" href="#">Hidden brand</a>
        <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
          <li class="nav-item active">
            <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled" href="#">Disabled</a>
          </li>
        </ul>
        <form class="form-inline my-2 my-lg-0">
          <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
      </div>
    </nav>
    <div id="toolbar" class="border border-dark rounded" style="background-color: lightgray;">
      <h5>Toolbar</h5>
      <form class="form-inline">
        <button type="button" style="display:none;" id="addText" class="btn btn-default">Add Post</button>
        <button type="button" style="display:none;" id="addImage" class="btn btn-default">Add Image</button>
        <button type="button" style="display:none;" id="addVideo" class="btn btn-default">Add Video</button>
        <input type="color" style="display:none;" class="form-control" id="changeBackground" value="#000000">
        <select id="changeFont" style="display:none;" class="form-control">
              <option style="font-family: Arial;" value="arial">Arial</option>
              <option style="font-family: Times;" value="times">Times New Roman</option>
              <option style="font-family: Courier New;" value="courier new">Courier New</option>
              <option style="font-family: Verdana;" value="verdana">Verdana</option>
              <option style="font-family: Georgia;" value="georgia">Georgia</option>
              <option style="font-family: Garamond;" value="garamond">Garamond</option>
              <option style="font-family: Comic Sans MS;" value="comic sans ms">Comic Sans MS</option>
              <option style="font-family: Trebuchet MS;" value="trebuchet ms">Trebuchet MS</option>
              <option style="font-family: Arial Black;" value="arial black">Arial Black</option>
              <option style="font-family: Impact;" value="impact">Impact</option>
        </select>
      </form>
    </div>
    <div id="blogBody">
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

<footer class="footer">
  <div class="container">
    <button type="button" id="enableEditing" class="btn btn-default">Enable Edit Mode</button>
    <button type="button" style="display:none;" id="disableEditing" class="btn btn-default">Exit Edit Mode</button>
  </div>
</footer
</body>"""
