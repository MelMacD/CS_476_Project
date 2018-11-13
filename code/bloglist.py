
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

  </head>
  <body>
  
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
