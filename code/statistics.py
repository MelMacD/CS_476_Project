from code import app
from flask import request
from code.sql_query_builder import SQLQueryBuilder as query
from code.database import Database as database

class Statistics:
    def __init__(self):
        self.info = self.displayCurrentInfo()
        self.table = self.generateTable()
        self.html = self.buildContent()
        
    #abstract, inherited
    def buildContent(self):
        return """
<head>
<title>Statistics</title>
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
<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/v/dt/dt-1.10.18/datatables.min.css"/>
<script type="text/javascript" src="https://cdn.datatables.net/v/dt/dt-1.10.18/datatables.min.js"></script>
<script src="static/statistics.js"></script>
</head>
<body>
    <!-- Navbar -->
    <div class="w3-top" style="z-index: 1000;">
        <div class="w3-bar w3-black w3-card">
            <a class="w3-bar-item w3-button w3-padding-large w3-hide-medium w3-hide-large w3-right" href="javascript:void(0)" onclick="myFunction()" title="Toggle Navigation Menu"><i class="fa fa-bars"></i></a>
            <a href="/" class="w3-bar-item w3-button w3-padding-large">Home</a>
            <a href="login" class="w3-bar-item w3-button w3-padding-large w3-hide-small">Login</a>
            <a href="signup" class="w3-bar-item w3-button w3-padding-large w3-hide-small">Sign-up</a>
        </div>
    </div>
    <div id="blogList" style="margin-top: 50px;">
        <h3 style="text-align: center;">Statistics for Blog {blogName}</h3>
        {info}
        <h3 style="text-align: center; margin-top: 50px;">Global Statistics</h3>
        {table}
    </div>
</div>
</body>""".format(blogName="test", info=self.info, table=self.table)

    def displayCurrentInfo(self):
        return ""
        
    def generateTable(self):
        tableRows = ""
        db = database()
        #need to iterate for each blog in the blog table
        queryBuilder = query("blog")
        queryString = queryBuilder.selectAll()
        result = db.execute(False, queryString)
        for row in result:
            queryBuilder = query("comments")
            queryString = queryBuilder.selectCountFilter("blogName='{blog}'".format(blog=row[1]))
            numComments = db.execute(False, queryString)
            queryString = queryBuilder.selectCountDistinctFilter("username", "blogName='{blog}'".format(blog=row[1]))
            distinctNumComments = db.execute(False, queryString)
            queryBuilder = query("reactions")
            queryString = queryBuilder.selectCountFilter("blogName='{blog}'".format(blog=row[1]))
            numReactions = db.execute(False, queryString)
            tableRows += """
<tr>
    <td>{blogName}</td>
    <td>{owner}</td>
    <td>{numComments}</td>
    <td>{numCommenters}</td>
    <td>{numReactions}</td>
    <td class="ranking"></td>
</tr>""".format(blogName=row[1], owner=row[0], numComments=numComments[0][0],
                numCommenters=distinctNumComments[0][0], numReactions=numReactions[0][0])
        db.disconnect()
        return """
<table id="statsTable" class="display" style="width:100%">
    <thead>
        <tr>
            <th>Blog Name</th>
            <th>Owner</th>
            <th>Number of Comments</th>
            <th>Number of Commenters</th>
            <th>Number of Reactions</th>
            <th>Popularity</th>
        </tr>
    </thead>
    <tbody>
        {rows}
    </tbody>
</table>""".format(rows=tableRows)
      
@app.route("/statistics")

def statistics():
    statistics = Statistics()
    return statistics.html
      
