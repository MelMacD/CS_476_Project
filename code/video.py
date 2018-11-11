class Video:
    def __init__(self, row):
        self.html = self.buildHtml(row.get("videoSource"))
        #setId(row.get("id"));
        #setLocation(row.get("top"), row.get("left"))
        #setSize(row.get("width"), row.get("height"))
        #setDepth(row.get("depth"))
        #setVideo(row.get("videoSource"))

    #@override
    def buildHtml(self, src):
        if "youtube" not in src:
            return """
<div id="{id}" class="draggable resizableAspect video" style="width: {width}px; height: {height}px; position: absolute; z-index: {depth}; left: {left}px; top: {top}px;">
    <button class="editVideo edit" type="button" style="position: absolute; top: 0; right: 0; z-index: 1;" data-toggle="modal" data-target="#exampleModal">Edit</button>
    <div id="mask" class="edit"></div>
    <video id="libraryVideo" style="display: block; width: 100%; height: 100%;" controls="" src="{src}">
        <source src="" type="video/mp4">
    </video>
    <iframe id="youtubeVideo" allowfullscreen="allowFullScreen" src="" style="width: 100%; height: 100%; display: none;" <="" iframe="">
        </div>
        </div>
    </iframe>
</div>"""
        else:
            return """
<div id="{id}" class="draggable resizableAspect" style="width: {width}px; height: {height}px; position: absolute; z-index: {depth}; left: {left}px; top: {top}px;">
    <button class="editVideo edit" type="button" style="position: absolute; top: 0; right: 0; z-index: 1;" data-toggle="modal" data-target="#exampleModal">Edit</button>
    <div id="mask" class="edit"></div>
    <video id="libraryVideo" style="display: none; width: 100%; height: 100%;" controls="" src="">
        <source src="" type="video/mp4">
    </video>
    <iframe id="youtubeVideo" allowfullscreen="allowFullScreen" src="{src}" style="width: 100%; height: 100%; display: block;" <="" iframe="">
        </div>
        </div>
    </iframe>
</div>"""
      
    #@override
    def setId(self, id):
        self.html.format(id=id)
    
    #@override
    def setLocation(self, top, left):
        self.html.format(top=top, left=left)
     
    #@override
    def setSize(self, width, height):
        self.html.format(width=width, height=height)
     
    #@override
    def setDepth(self, depth):
        self.html.format(depth=depth)
      
    def setVideo(self, source):
        self.html.format(src=source)
         
