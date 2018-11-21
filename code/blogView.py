from code import app
from flask import request
from code.sql_query_builder import SQLQueryBuilder as query
from code.database import Database as database
from code.post import Post as post
from code.image import Image as image
from code.video import Video as video
from code.thread import Thread as thread
from code.react import React as react

blogColor = ""
blogFont = ""
blogUrlName = ""

@app.route("/uploadComment", methods=['GET', 'POST'])

def uploadComment():
    global blogUrlName
    if request.method == 'POST':
        requestData = request.get_json()
        db = database()
        queryBuilder = query("comments")
        queryString = queryBuilder.insertRow("'{blogName}', '{attachedToId}', '{currentUser}', '{comment}'".format(blogName=blogUrlName,
                attachedToId=requestData.get("attachedToId"), currentUser=request.cookies.get('userId'), comment=requestData.get("comment")))
        db.execute(True, queryString)
        db.disconnect()
        return str(requestData)
    else:
        db.disconnect()
        return "error"

@app.route("/uploadReaction", methods=['GET', 'POST'])

def uploadReaction():
    global blogUrlName
    if request.method == 'POST':
        requestData = request.get_json()
        db = database()
        queryBuilder = query("reactions")
        #need to check if user has reacted to that element before; if so, update instead of insert
        queryString = queryBuilder.selectCountFilter("blogName='{blogName}' and attachedToId='{id}' and username='{currentUser}'".format(
                blogName=blogUrlName, id=requestData.get("attachedToId"), currentUser=request.cookies.get('userId')));
        result = db.execute(False, queryString);
        if result[0][0] == 0:
            queryString = queryBuilder.insertRow("'{blogName}', '{attachedToId}', '{currentUser}', '{emote}'".format(
                    blogName=blogUrlName, attachedToId=requestData.get("attachedToId"), currentUser=request.cookies.get('userId'), emote=requestData.get("emote")))
        else:
            queryString = queryBuilder.update("emote='{emote}'".format(emote=requestData.get("emote")),
                                              "blogName='{blogName}' and attachedToId='{id}' and username='{currentUser}'".format(blogName=blogUrlName, id=requestData.get("attachedToId"), currentUser=request.cookies.get('userId')))
        db.execute(True, queryString)
        db.disconnect()
        return str(requestData)
    else:
        db.disconnect()
        return "error"
    
@app.route("/blogView", methods=['GET', 'POST'])

def hello():
    global blogUrlName
    if request.method == 'POST':
        requestData = request.get_json()#this is a dictionary
        db = database()
        for key, value in requestData.items():
            #check if action is present, if not, must be blog update
            if "not present" in value.get("action", "not present"):
                queryBuilder = query("blog")
                queryString = queryBuilder.update("backgroundColor='{color}', font='{font}'".format(
                    color=value.get("backgroundColor"), font=value.get("font")),
                                                  "blogName='{blogName}'".format(blogName=blogUrlName))
                db.execute(True, queryString)
            elif "insert" in value.get("action"):
                if "post" in key:
                    queryBuilder = query("posts")
                    queryString = queryBuilder.insertRow("'{blogName}', '{id}', {top}, {left}, {width}, {height}, {depth}, '{title}', '{body}', '{backgroundColor}', '{fontColor}', {hasThread}".format(
                                    blogName=blogUrlName, id=key, top=value.get("top"), left=value.get("left"), width=value.get("width"),
                                    height=value.get("height"), depth=value.get("depth"), title=value.get("title"),
                                    body=value.get("content"), backgroundColor=value.get("backgroundColor"), fontColor=value.get("fontColor"), hasThread=value.get("hasThread")))
                    db.execute(True, queryString)
                elif "image" in key:
                    queryBuilder = query("images")
                    queryString = queryBuilder.insertRow("'{blogName}', '{id}', {top}, {left}, {width}, {height}, {depth}, '{source}', {hasThread}".format(
                                    blogName=blogUrlName, id=key, top=value.get("top"), left=value.get("left"), width=value.get("width"),
                                    height=value.get("height"), depth=value.get("depth"), source=value.get("source"), hasThread=value.get("hasThread")))
                    db.execute(True, queryString)
                elif "video" in key:
                    queryBuilder = query("videos")
                    queryString = queryBuilder.insertRow("'{blogName}', '{id}', {top}, {left}, {width}, {height}, {depth}, '{source}', {hasThread}".format(
                                    blogName=blogUrlName, id=key, top=value.get("top"), left=value.get("left"), width=value.get("width"),
                                    height=value.get("height"), depth=value.get("depth"), source=value.get("source"), hasThread=value.get("hasThread")))
                    db.execute(True, queryString)
                else:
                    return "error"
            elif "update" in value.get("action"):
                if value.get("hasThread") == 0:
                    queryBuilder = query("comments")
                    queryString = queryBuilder.delete("blogName='{blogName}' AND attachedToId='{id}'".format(blogName=blogUrlName, id=key))
                    db.execute(True, queryString)
                if "post" in key:
                    queryBuilder = query("posts")
                    queryString = queryBuilder.update("topVal={top}, leftVal={left}, width={width}, height={height}, depth={depth}, title='{title}', body='{body}', backgroundColor='{backgroundColor}', fontColor='{fontColor}', hasThread={hasThread}".format(
                                    top=value.get("top"), left=value.get("left"), width=value.get("width"),
                                    height=value.get("height"), depth=value.get("depth"), title=value.get("title"),
                                    body=value.get("content"), backgroundColor=value.get("backgroundColor"), fontColor=value.get("fontColor"), hasThread=value.get("hasThread")),
                                                     "blogName='{blogName}' AND id='{id}'".format(blogName=blogUrlName, id=key))
                    db.execute(True, queryString)
                elif "image" in key:
                    queryBuilder = query("images")
                    queryString = queryBuilder.update("topVal={top}, leftVal={left}, width={width}, height={height}, depth={depth}, imageSource='{source}', hasThread={hasThread}".format(
                                    top=value.get("top"), left=value.get("left"), width=value.get("width"),
                                    height=value.get("height"), depth=value.get("depth"), source=value.get("source"), hasThread=value.get("hasThread")),
                                                     "blogName='{blogName}' AND id='{id}'".format(blogName=blogUrlName, id=key))
                    db.execute(True, queryString)
                elif "video" in key:
                    queryBuilder = query("videos")
                    queryString = queryBuilder.update("topVal={top}, leftVal={left}, width={width}, height={height}, depth={depth}, videoSource='{source}', hasThread={hasThread}".format(
                                    top=value.get("top"), left=value.get("left"), width=value.get("width"),
                                    height=value.get("height"), depth=value.get("depth"), source=value.get("source"), hasThread=value.get("hasThread")),
                                                     "blogName='{blogName}' AND id='{id}'".format(blogName=blogUrlName, id=key))
                    db.execute(True, queryString)
                else:
                    return "error"
            elif "delete" in value.get("action"):
                if value.get("hasThread") == 1:
                    queryBuilder = query("comments")
                    queryString = queryBuilder.delete("blogName='{blogName}' AND attachedToId='{id}'".format(blogName=blogUrlName, id=key))
                    db.execute(True, queryString)
                if "post" in key:
                    queryBuilder = query("posts")
                    queryString = queryBuilder.delete("blogName='{blogName}' AND id='{id}'".format(blogName=blogUrlName, id=key))
                    db.execute(True, queryString)
                    #delete all comments for a deleted element
                    queryBuilder = query("reactions")
                    queryString = queryBuilder.delete("blogName='{blogName}' AND attachedToId='{id}'".format(blogName=blogUrlName, id=key))
                    db.execute(True, queryString)
                elif "image" in key:
                    queryBuilder = query("images")
                    queryString = queryBuilder.delete("blogName='{blogName}' AND id='{id}'".format(blogName=blogUrlName, id=key))
                    db.execute(True, queryString)
                    #delete all comments for a deleted element
                    queryBuilder = query("reactions")
                    queryString = queryBuilder.delete("blogName='{blogName}' AND attachedToId='{id}'".format(blogName=blogUrlName, id=key))
                    db.execute(True, queryString)
                elif "video" in key:
                    queryBuilder = query("videos")
                    queryString = queryBuilder.delete("blogName='{blogName}' AND id='{id}'".format(blogName=blogUrlName, id=key))
                    db.execute(True, queryString)
                    #delete all comments for a deleted element
                    queryBuilder = query("reactions")
                    queryString = queryBuilder.delete("blogName='{blogName}' AND attachedToId='{id}'".format(blogName=blogUrlName, id=key))
                    db.execute(True, queryString)
                else:
                    return "error"
            else:
                return "error"
        db.disconnect()
        return str(requestData)
    else:
        blogUrlName = request.args.get("blogName", "error")
        buildBlogSpecs()
        #if current user token is not owner of blog, don't display edit
        editBlogButton = ""
        currentUser = request.cookies.get('userId', "")
        if currentUser != "":
            db = database()
            queryBuilder = query("blog")
            queryString = queryBuilder.selectAllFilter("blogName='{blogName}' AND username='{username}'".format(blogName=blogUrlName, username=currentUser))
            result = db.execute(False, queryString)
            db.disconnect()
            if result != []:
                editBlogButton = """
<button type="button" id="enableEditing" style="position: absolute; left: 20px;" class="btn btn-default">Enable Edit Mode</button>
"""
        return """
<head>
<title>{blogName}</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.2/css/bootstrap-theme.min.css">
<link href="https://afeld.github.io/emoji-css/emoji.css" rel="stylesheet">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<script
  src="https://code.jquery.com/jquery-3.3.1.min.js"
  integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8="
  crossorigin="anonymous"></script>
<script src="static/jquery-ui.min.js"></script>
<link rel="stylesheet" type="text/css" href="//ajax.googleapis.com/ajax/libs/jqueryui/1.7.1/themes/base/jquery-ui.css"/>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
<script src="static/blogEditingHandlers.js"></script>
<script src="static/logInOut.js"></script>
<link rel="stylesheet" href="static/blogEditingStyle.css" />
</head>
<body style="background-color: {backgroundColor};">
    <!-- Navbar -->
    <div class="w3-top" style="z-index: 1000;">
        <div class="w3-bar w3-black w3-card">
            <a href="/" class="w3-bar-item w3-button w3-padding-large">Home</a>
            <a href="#" class="w3-bar-item w3-button w3-padding-large logout" style="display: none;">Logout</a>
            <a href="login" class="w3-bar-item w3-button w3-padding-large login">Login</a>
            <a href="signup" class="w3-bar-item w3-button w3-padding-large signup">Sign-up</a>
        </div>
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
        <!-- Navbar on small screens (remove the onclick attribute if you want the navbar to always show on top of the content when clicking on the links) -->
        <div id="navDemo" class="w3-bar-block w3-black w3-hide w3-hide-large w3-hide-medium w3-top" style="margin-top:46px">
            <a href="login" class="w3-bar-item w3-button w3-padding-large" onclick="myFunction()">Login</a>
            <a href="signup" class="w3-bar-item w3-button w3-padding-large" onclick="myFunction()">Sign-up</a>
        </div>
    </div>
    <div id="blogBody" style="font-family: {font}; margin-top: 46px;">
      {blogContent}
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
    {editButton}
    <button type="button" style="display:none; position: absolute; left: 20px;" id="disableEditing" class="btn btn-default">Exit Edit Mode</button>
    <a style="position: relative; left: 45%;" href="https://expressyourself.azurewebsites.net/statistics?blogName={blog}" id="seeStatistics" class="btn btn-default" role="button">Statistics</a>
    <button type="button" style="display:inline; position: absolute; right: 20px;" id="save" class="btn btn-success">Save Changes</button>
  </div>
</footer
</body>""".format(blogName=blogUrlName,
                  blog=blogUrlName,
                  blogContent=buildBlogContent(),
                  backgroundColor=blogColor,
                  font=blogFont,
                  editButton=editBlogButton)

def buildBlogSpecs():
    global blogUrlName
    global blogColor
    global blogFont
    db = database()
    queryBuilder = query("blog")
    queryString = queryBuilder.selectAllFilter("blogName='{blogName}'".format(blogName=blogUrlName))
    result = db.execute(False, queryString)
    db.disconnect()
    if result == []:
        blogColor = "rgb(255, 255, 255)"
        blogFont = "arial"
    else:
        for row in result:
            blogColor = row[4]
            blogFont = row[5].replace('"', '')
 
def buildBlogContent():
    db = database()
    content = ""
    content += buildElement(db, "posts")
    content += buildElement(db, "images")
    content += buildElement(db, "videos")
    db.disconnect()
    return content

def buildElement(db, tableName):
    global blogUrlName
    content = ""
    addThreadButton = """<button type="button" class="dropdown-item addThread">Add Thread</button>"""
    removeThreadButton = """<button type="button" class="dropdown-item removeThread">Remove Thread</button>"""
    queryBuilder = query(tableName)
    queryString = queryBuilder.selectAllFilter("blogName='{blogName}'".format(blogName=blogUrlName))
    result = db.execute(False, queryString)
    if result == []:
        return ""
    else:
        for row in result:
            if tableName == "posts":
                currentElement = post(row)
                #if has thread, format with content, otherwise ""
                if row[11] == 1:
                    content += currentElement.buildHtml().format(thread=buildThread(db, row[1]),
                                                                 addRemoveThread=removeThreadButton,
                                                                 react=buildReactions(db, row[1]))
                else:
                    content += currentElement.buildHtml().format(thread="",
                                                                 addRemoveThread=addThreadButton,
                                                                 react=buildReactions(db, row[1]))
            elif tableName == "images":
                currentElement = image(row)
                if row[8] == 1:
                    content += currentElement.buildHtml().format(thread=buildThread(db, row[1]),
                                                                 addRemoveThread=removeThreadButton,
                                                                 react=buildReactions(db, row[1]))
                else:
                    content += currentElement.buildHtml().format(thread="",
                                                                 addRemoveThread=addThreadButton,
                                                                 react=buildReactions(db, row[1]))
            elif tableName == "videos":
                currentElement = video(row)
                if row[8] == 1:
                    content += currentElement.buildHtml().format(thread=buildThread(db, row[1]),
                                                                 addRemoveThread=removeThreadButton,
                                                                 react=buildReactions(db, row[1]))
                else:
                    content += currentElement.buildHtml().format(thread="",
                                                                 addRemoveThread=addThreadButton,
                                                                 react=buildReactions(db, row[1]))
            else:
                content += "error"
        return content

def buildThread(db, key):
    global blogUrlName
    queryBuilder = query("comments")
    queryString = queryBuilder.selectAllFilter("blogName='{blogName}' and attachedToId='{elementId}'".format(blogName=blogUrlName, elementId=key))
    result = db.execute(False, queryString)
    obj = thread(result)
    return obj.buildHtml()

def buildReactions(db, key):
    global blogUrlName
    queryBuilder = query("reactions")
    obj = react(db, queryBuilder, blogUrlName, key)
    return obj.buildHtml()
