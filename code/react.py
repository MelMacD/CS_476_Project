from code.factory import Element

class React(Element):
    def __init__(self, db, queryBuilder, blogName, attachedToId):
        self.reactions = self.buildReactions(db, queryBuilder, blogName, attachedToId)
    
    #@override
    def buildHtml(self):
        return """
        <div class="reactBar" style="bottom: 0px; height: 38px; background-color: lightgray; position: absolute; width: 100%;">
            <div class="reactions" style="position: absolute; left: 0px; width: 69%; font-size: 12px;">
                {reactions}
            </div>
            <div class="dropdown" style="position: absolute; top: 0px; right: 0px;">
                <button class="btn btn-secondary dropdown-toggle react" style="position: absolute; top: 0; right: 0; z-index: 1;" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">React</button>
                <div class="dropdown-menu">
                    <div style="margin-left: 13px;">
                        <button class="reactLike" type="button"><i class="em em---1"></i></button>
                        <button class="reactDislike" type="button"><i class="em em--1"></i></button>
                        <button class="reactClap" type="button"><i class="em em-clap"></i></button>
                    </div>
                    <div style="margin-left: 13px;">
                        <button class="reactHeart" type="button"><i class="em em-heart"></i></button>
                        <button class="reactSmile" type="button"><i class="em em-smile"></i></button>
                        <button class="reactCry" type="button"><i class="em em-sob"></i></button>
                    </div>
                    <div style="margin-left: 13px;">
                        <button class="reactSilly" type="button"><i class="em em-stuck_out_tongue_winking_eye"></i></button>
                        <button class="reactAngry" type="button"><i class="em em-angry"></i></button>
                        <button class="reactShock" type="button"><i class="em em-scream"></i></button>
                    </div>
                </div>
            </div>
        </div>
""".format(reactions=self.reactions)

    def buildReactions(self, db, queryBuilder, blogName, attachedToId):
        emotes = ['em---1', 'em--1', 'em-clap', 'em-heart', 'em-smile', 'em-sob', 'em-stuck_out_tongue_winking_eye', 'em-angry', 'em-scream']
        content = ""
        # get count for each type of reaction, only build emoji if count is not 0
        for emote in emotes:
            queryString = queryBuilder.selectCountFilter("blogName='{blogName}' and attachedToId='{id}' and emote='{emote}'".format(blogName=blogName, id=attachedToId, emote=emote))
            result = db.execute(False, queryString)
            if result[0][0] != 0:
                content += """
                <i class="em {emote} smallEmoji" style="position: relative; margin-left: 14px;">
                    <p style="position: absolute; left: -14px;">{count}</p>
                </i>""".format(count=result[0][0], emote=emote)
        return content
