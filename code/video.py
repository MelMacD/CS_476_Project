class Video:
    def __init__(self, row):
        self.id = self.setId(row)
        self.top = self.setTop(row)
        self.left = self.setLeft(row)#inherit base attributes with super
        self.width = self.setWidth(row)
        self.height = self.setHeight(row)
        self.depth = self.setDepth(row)
        #self.video = self.setVideo(row)

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
</div>""".format(id=self.id, top=self.top, left=self.left, width=self.width, height=self.height, depth=self.depth,
                src="")
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
</div>""".format(id=self.id, top=self.top, left=self.left, width=self.width, height=self.height, depth=self.depth,
                src="")
      
    #@override
    def setId(self, row):
        return row[1]
        
    #@override
    def setTop(self, row):
        return row[2]
     
    #@override
    def setLeft(self, row):
        return row[3]
    
    #@override
    def setWidth(self, row):
        return row[4]
     
    #@override
    def setHeight(self, row):
        return row[5]
    
    #@override
    def setDepth(self, row):
        return row[6]
      
    def setVideo(self, row):
        return row[7]
         
