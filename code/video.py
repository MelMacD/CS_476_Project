from code.factory import Element

class Video(Element):
    def __init__(self, row):
        super().__init__(row)
        self.video = self.setVideo(row)

    #@override
    def buildHtml(self):
        if "youtube" not in self.video:
            return """
<div id="{id}" class="draggable resizableAspect video" style="width: {width}px; height: {height}px; position: absolute; z-index: {depth}; left: {left}px; top: {top}px;">
    <div class="dropdown edit">
        <button class="btn btn-secondary dropdown-toggle" style="position: absolute; top: 0; right: 0; z-index: 1;" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Edit</button>
            <div class="dropdown-menu">
                <button class="editVideo dropdown-item" type="button" data-toggle="modal" data-target="#exampleModal">Change Content</button>
                {{addRemoveThread}}
                <button type="button" class="dropdown-item deletePost">Delete</button>
            </div>
    </div>
    <div id="mask" class="edit"></div>
    <video id="libraryVideo" style="display: block; width: 100%; height: 100%;" controls="" src="{src}">
        <source src="" type="video/mp4">
    </video>
    <iframe id="youtubeVideo" allowfullscreen="allowFullScreen" src="" style="width: 100%; height: 100%; display: none;" <="" iframe="">
        </div>
        </div>
    </iframe>
    {{react}}
    {{thread}}
</div>""".format(id=self.id, top=self.top, left=self.left, width=self.width, height=self.height, depth=self.depth,
                src=self.video)
        else:
            return """
<div id="{id}" class="draggable resizableAspect video" style="width: {width}px; height: {height}px; position: absolute; z-index: {depth}; left: {left}px; top: {top}px;">
    <div class="dropdown edit">
        <button class="btn btn-secondary dropdown-toggle" style="position: absolute; top: 0; right: 0; z-index: 1;" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Edit</button>
        <div class="dropdown-menu">
            <button class="editVideo dropdown-item" type="button" data-toggle="modal" data-target="#exampleModal">Change Content</button>
            {{addRemoveThread}}
            <button type="button" class="dropdown-item deletePost">Delete</button>
        </div>
    </div>
    <div id="mask" class="edit"></div>
    <video id="libraryVideo" style="display: none; width: 100%; height: 100%;" controls="" src="">
        <source src="" type="video/mp4">
    </video>
    <iframe id="youtubeVideo" allowfullscreen="allowFullScreen" src="{src}" style="width: 100%; height: 100%; display: block;" <="" iframe="">
        </div>
        </div>
    </iframe>
    {{react}}
    {{thread}}
</div>""".format(id=self.id, top=self.top, left=self.left, width=self.width, height=self.height, depth=self.depth,
                src=self.video)
      
    def setVideo(self, row):
        return row[7]
         
