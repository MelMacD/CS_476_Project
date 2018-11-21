from code.factory import Element

class Image(Element):
    def __init__(self, row):
        super().__init__(row)
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
    {{react}}
    {{thread}}
</div>""".format(id=self.id, top=self.top, left=self.left, width=self.width, height=self.height, depth=self.depth,
                src=self.image)
      
    def setImage(self, row):
        return row[7]
         
