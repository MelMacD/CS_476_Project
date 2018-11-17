
from code import app
from flask import request, render_template
from code.sql_query_builder import SQLQueryBuilder as query
from code.database import Database as database

    
@app.route("/bloglist", methods=['GET', 'POST'])

def bloglist():
    if request.method == 'POST':
        db = database()
         #querying the database and checking ""
        queryBuilder = query("blog")
        queryString = queryBuilder.selectAllFilter("blogName='test'")
        db.execute(False, queryString)
        return render_template('template/sample.html')
    else
        return "error"
 
  
  


