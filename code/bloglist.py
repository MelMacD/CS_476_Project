
from code import app
from flask import request
from code.sql_query_builder import SQLQueryBuilder as query
from code.database import Database as database

    
@app.route("/bloglist", methods=['GET', 'POST'])

def bloglist():
    if request.method == 'POST':
        db = database()
         #querying the database and checking ""
        queryBuilder = query("blog")
        queryString = queryBuilder.selectAllFilter("blogName='test'")
        db.execute(True, queryString)
             return ""
    else:
            return "error"
 
html = """ 
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
  <h2>The Blog-List Section</h2>
  <div class="row">
  <div class="column">
    <div class="card">
 <tr>
  <td>Username</td>
  <td>Blog-Name</td>
  <td>Image</td>
  <td>Description</td>
  </tr>
    
    {% for item in blog %}
<tr>
    <td>{{item[0]}}</td>
    <td>{{item[1]}}</td>
    ...
</tr>
{% endfor %}
    </div>
    </div>
        </div>
  </body>
  </html>
  """
        
  


