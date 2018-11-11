class Image:
    def __init__(self, row):
        self.html = self.buildHtml()
        #setId(row.get("id"));
        #setLocation(row.get("top"), row.get("left"))
        #setSize(row.get("width"), row.get("height"))
        #setDepth(row.get("depth"));
        #setImage(row.get("imageSource"));

    #@override
    def buildHtml(self):
        return """
<div id="{id}" class="draggable resizableAspect image" style="width: {width}px; height: {height}px; position: absolute; z-index: {depth}; left: {left}px; top: {top}px;">
    <button class="editImage edit" type="button" style="position: absolute; top: 0; right: 0;" data-toggle="modal" data-target="#exampleModal">Edit</button>
    <img src="{src}" style="width: 100%; height: 100%;">
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
      
    def setImage(self, source):
        self.html.format(src=source)
         
