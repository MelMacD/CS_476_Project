class React:
    def __init__(self, values):
        self.reactions = self.buildReactions(values)
    
    #@override
    def buildHtml(self):
        return """
        <div class="reactBar" style="height: 38px; background-color: lightgray; position: absolute; width: 100%; bottom: 0px;">
            <div class="reactions" style="position: absolute; left: 0px; width: 70%; font-size: 12px;">
                <span>0<i class="em em---1 smallEmoji"></i></span>
                0<i class="em em--1 smallEmoji"></i>
                0<i class="em em-clap smallEmoji"></i>
                0<i class="em em-heart smallEmoji"></i>
                0<i class="em em-smile smallEmoji"></i>
                0<i class="em em-sob smallEmoji"></i>
                0<i class="em em-stuck_out_tongue_winking_eye smallEmoji"></i>
                <i class="em em-angry smallEmoji"></i>
                <i class="em em-scream smallEmoji" style="position: absolute; margin-left: 14px;"><p style="position: absolute; left: -14px;">0</p></i>
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
"""

    def buildReactions(self, values):
        return ""
