from code import app


@app.route("/")

def hello():

    return """
<div class="panel panel-default">
  <div class="panel-body">
    <h1>
        What is the title?
    </h1>
    <p>
        What is the content?
    </p>
  </div>  
</div>"""
