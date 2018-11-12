from code import app
from flask import request
from code.sql_query_builder import SQLQueryBuilder as query
from code.database import Database as database
    
@app.route("/blogView", methods=['GET', 'POST'])

def hello():
    if request.method == 'POST':
        requestData = request.get_json()#this is a dictionary
        #implement insert into table
        for key, value in requestData.items():
            if value.get("isUpdate") is False:
                if "post" in key:
                    return "post"
                elif "image" in key:
                    queryBuilder = query("images")
                    db = database("images")
                    queryString = queryBuilder.insertRow("'test', '{id}', {top}, {left}, {width}, {height}, {depth}, '{source}'".format(
                                    id=key, top=value.get("top"), left=value.get("left"), width=value.get("width"),
                                    height=value.get("height"), depth=value.get("depth"), source=value.get("source")))
                    return db.execute(True, queryString)
                elif "video" in key:
                    return "video"
                else:
                    return "error"
            else:
                #update
                return "update"
        return str(requestData)
    else:
        return """
<head>
<title>Test Page</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.2/css/bootstrap-theme.min.css">
<script
  src="https://code.jquery.com/jquery-3.3.1.min.js"
  integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8="
  crossorigin="anonymous"></script>
<script src="static/jquery-ui.min.js"></script>
<link rel="stylesheet" type="text/css" href="//ajax.googleapis.com/ajax/libs/jqueryui/1.7.1/themes/base/jquery-ui.css"/>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
<script src="static/blogEditingHandlers.js"></script>
<link rel="stylesheet" href="static/blogEditingStyle.css" />
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="dropdown edit">
        <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenu2" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Toolbar</button>
      <div class="dropdown-menu" style="min-width: 30rem;">
        <form class="px-4 py-3">
          <div class="form-group">
            <button type="button" id="addText" class="btn btn-default">Add Post</button>
            <button type="button" id="addImage" class="btn btn-default">Add Image</button>
            <button type="button" id="addVideo" class="btn btn-default">Add Video</button>
            </br>
            </br>
            <label for="changeBackground">Page Background Colour: </label>
              <input type="color" class="form-control" id="changeBackground" value="#000000">
            </br>
            <label for="changeFont">Page Font: </label>
            <select id="changeFont" class="form-control">
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
          </div>
        </form>
      </div>
      </div>
    </nav>
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
<div id="hiddenForm" style="display:none;">
  <form>
  </form>
</div>
<footer class="footer">
  <div class="container">
    <button type="button" id="enableEditing" class="btn btn-default">Enable Edit Mode</button>
    <button type="button" style="display:none;" id="disableEditing" class="btn btn-default">Exit Edit Mode</button>
    <button type="button" style="display:inline;" id="save" class="btn btn-success">Save Changes</button>
  </div>
</footer
</body>"""
