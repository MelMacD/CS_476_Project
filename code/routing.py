from code import app


@app.route("/")

def hello():

    return """
<p class="border border-dark rounded">
    <h1 contenteditable="true">
        What is the title?
    </h1>
    <div contenteditable="true">
        What is the content?
    </div>
</p>"""
