from code.factory import Element

class Post(Element):
    def __init__(self, row):
        super().__init__(row)
        self.title = self.setTitle(row)
        self.body = self.setBody(row)
        self.background = self.setBackground(row)
        self.fontColor = self.setFontColor(row)

    #@override
    def buildHtml(self):
        return """
<div id="{id}" class="border border-dark rounded draggable resizable post" style="width: {width}px; height: {height}px; position: absolute; z-index: {depth}; left: {left}px; top: {top}px;">
    <div class="dropdown edit">
        <button class="btn btn-secondary dropdown-toggle" style="position: absolute; top: 0; right: 0;" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Edit</button>
        <div class="dropdown-menu">
            <button class="editPost dropdown-item" type="button" data-toggle="modal" data-target="#exampleModal">Change Content</button>
            {{addRemoveThread}}
            <button type="button" class="dropdown-item deletePost">Delete</button>
        </div>
    </div>
    <div id="originalContent" style="position: absolute; width: 100%; height: 100%; background-color: {backgroundColor}; color: {fontColor};">
        <h3>{title}</h3>
        <p>{content}</p>
    </div>
    {{react}}
    {{thread}}
</div>""".format(id=self.id, top=self.top, left=self.left, width=self.width, height=self.height, depth=self.depth,
                title=self.title, content=self.body, backgroundColor=self.background, fontColor=self.fontColor)
      
    def setTitle(self, row):
        return row[7]
      
    def setBody(self, row):
        return row[8]

    def setBackground(self, row):
        return row[9]
     
    def setFontColor(self, row):
        return row[10]
     
