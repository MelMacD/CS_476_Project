from code import app
from flask import request, render_template
from code.sql_query_builder import SQLQueryBuilder as query
from code.database import Database as database
from code.observer import Observer

class BlogList(Observer):
    def __init__(self):
        self.blogContent = self.displayBlogs()
        super().__init__()
      
    #abstract, inherited
    def buildContent(self):
        return """
<head>
<title>Blog List</title>
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
<script src="static/bloglist.js"></script>
<script src="static/logInOut.js"></script>
</head>
<body>
<!-- Navbar -->
<div class="w3-top">
  <div class="w3-bar w3-black w3-card">
    <a href="/" class="w3-bar-item w3-button w3-padding-large">Home</a>
    <a href="#" class="w3-bar-item w3-button w3-padding-large logout" style="display: none;">Logout</a>
    <a href="login" class="w3-bar-item w3-button w3-padding-large login">Login</a>
    <a href="signup" class="w3-bar-item w3-button w3-padding-large signup">Sign-up</a>
  </div>
</div>
    <div id="blogList" style="margin-top: 50px;">
        <h3 style="text-align: center;">Browse All of Our Blogs!</h3>
        {blogsListed}
    </div>
</div>
</body>""".format(blogsListed=self.blogContent)
    
    def displayBlogs(self):
        results = ""
        db = database()
        queryBuilder = query("blog")
        queryString = queryBuilder.selectAll()
        result = db.execute(False, queryString)
        for row in result:
            results += self.createElement(row)
        return """
<ul class="list-group" style="width: 800px; margin: auto;">
    <input type="text" id="search" placeholder="Search by blog name and hit enter">
    {blogs}
</ul>
""".format(blogs=results)
    
    def createElement(self, row):
        if row[2] is None or row[2] == "None":
            row[2] = "static/default.gif"
        return """
<li class="list-group-item list-group-item-action">
    <img src="{image}" style="height: 150px; width: 150px;">
    <h1 style="position: absolute; left: 175px; top: 0px; width: 600px;">{blogName}</h1>
    <p style="position: absolute; left: 175px; top: 70px; width: 600px; height: 100px;"">
        {description}
    </p>
</li>
""".format(image=row[2], blogName=row[1], description=row[3])

    
@app.route("/bloglist")

def bloglist():
    blogList = BlogList()
    return blogList.html
    
