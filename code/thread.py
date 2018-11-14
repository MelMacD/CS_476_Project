class Thread:
    def __init__(self, values):
        self.comments = self.buildComments(values)

    #@override
    def buildHtml(self):
        return """
<div class="newThread">
    <div style="height: 200px; overflow-y: scroll;">
        <ul class="list-group" style="font-size: 14px;">
            {commentHtml}
        </ul>
    </div>
    <div class="input-group">
        <input type="text" class="form-control" placeholder="Enter a comment">
        <div class="input-group-append">
            <button class="btn btn-outline-secondary submitComment" type="button" style="background-color: darkgray;">Enter</button>
        </div>
    </div>
</div>
""".format(commentHtml=self.comments)
      
    def buildComments(self, values):
        commentBlock = ""
        #for row in values:
        #    commentBlock += """
        #        <li class="list-group-item"><b>{username}:</b>    {comment}</li>
        #    """.format(username=row[2], comment=row[3])
        return commentBlock
