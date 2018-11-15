class Image:
    def __init__(self, row):
        self.id = self.setId(row)
        self.top = self.setTop(row)
        self.left = self.setLeft(row)#inherit base attributes with super
        self.width = self.setWidth(row)
        self.height = self.setHeight(row)
        self.depth = self.setDepth(row)
        self.image = self.setImage(row)

    #@override
    def buildHtml(self):
        return """
<div id="{id}" class="draggable resizableAspect image" style="width: {width}px; height: {height}px; position: absolute; z-index: {depth}; left: {left}px; top: {top}px;">
    <div class="dropdown edit">
        <button class="btn btn-secondary dropdown-toggle" style="position: absolute; top: 0; right: 0;" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Edit</button>
        <div class="dropdown-menu">
            <button class="editImage dropdown-item" type="button" data-toggle="modal" data-target="#exampleModal">Change Content</button>
            {{addRemoveThread}}
            <button type="button" class="dropdown-item deletePost">Delete</button>
        </div>
    </div>
    <img src="{src}" style="width: 100%; height: 100%;">
    {{thread}}
</div>""".format(id=self.id, top=self.top, left=self.left, width=self.width, height=self.height, depth=self.depth,
                src=self.image)
      
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
      
    def setImage(self, row):
        return row[7]
         
