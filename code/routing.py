from code import app


@app.route("/")

def hello():

    return """
<p class="border border-dark rounded">
    <h1>
        What is the title?
    </h1>
    <div>
        What is the content?
    </div>
</p>"""
