from code import app


@app.route("/")

def hello():

    return """
<p>
    <h contenteditable="true">
        "What is the title?"
    </h>
    <div contenteditable="true">
        "What is the content?"
    </div>
</p>"""
