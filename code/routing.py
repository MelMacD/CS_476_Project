from code import app


@app.route("/")

def hello():

    return """
<div class="border border-dark rounded">
    <h1>
        What is the title?
    </h1>
    <p>
        What is the content?
    </p>
</div>"""
