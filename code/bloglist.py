
from code import app
from flask import request
from code.sql_query_builder import SQLQueryBuilder as query
from code.database import Database as database

    
@app.route("/bloglist", methods=['GET', 'POST'])

def bloglist():
    if request.method == 'POST':
        
        return ""
    else:
        return """
 
 <!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title> Blog List</title>
<style>
html {
  box-sizing: border-box;
}

*, *:before, *:after {
  box-sizing: inherit;
}

.column {
  float: left;
  width: 33.3%;
  margin-bottom: 16px;
  padding: 0 8px;
}

@media screen and (max-width: 650px) {
  .column {
    width: 100%;
    display: block;
  }
}

.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
}

.container {
  padding: 0 16px;
}

.container::after, .row::after {
  content: "";
  clear: both;
  display: table;
}

.title {
  color: grey;
}

.button {
  border: none;
  outline: 0;
  display: inline-block;
  padding: 8px;
  color: white;
  background-color: #000;
  text-align: center;
  cursor: pointer;
  width: 100%;
}

.button:hover {
  background-color: #555;
}
</style>
  </head>
  <body>
  <div class="row">
  <div class="column">
    <div class="card">
    
    <img src="/w3images/team1.jpg" alt="Jane" style="width:100%">
      <div class="container">
        <h2>Jane Doe</h2>
        <p class="title">CEO & Founder</p>
        <p>Some text that describes me lorem ipsum ipsum lorem.</p>
        <p>example@example.com</p>
    
    
    <p><button class="button">View</button></p>
    </div>
    </div>
    </div>
  </body>
  </html>
  """.format(blogContent=buildBlogContent())
        
        
def buildBlogContent():
    db = database()
    content = ""
    content += buildElement(db, "blog")
return content


def buildElement(db, tableName):
    content = ""
    queryBuilder = query(tableName)
    queryString = queryBuilder.selectAllFilter("blogName='test'")
    result = db.execute(False, queryString)
    if result == []:
        return ""
    else:
        for row in result:
            if tableName == "blog":
                currentElement = blog(row)
                content += currentElement.buildHtml()
            else:
                content += "error"
return content
