class Post:
    def __init__(self, row):
        self.id = setId(row)
        self.top = setTop(row)
        self.left = setLeft(row)#inherit base attributes with super
        self.width = setWidth(row)
        self.height = setHeight(row)
        self.depth = setDepth(row)
        self.title = setTitle(row)
        self.body = setBody(row)
        self.background = setBackground(row)
        self.fontColor = setFontColor(row)

    #@override
    def buildHtml(self):
        return """
<div id="{id}" class="border border-dark rounded draggable resizable post" style="width: {width}px; height: {height}px; position: absolute; z-index: {depth}; left: {left}px; top: {top}px;">
    <button class="editPost edit" type="button" style="position: absolute; top: 0; right: 0;" data-toggle="modal" data-target="#exampleModal">Edit</button>
    <div id="originalContent" style="width: 100%; height: 100%; background-color: {backgroundColor}; color: {fontColor};">
        <h3>{title}</h3>
        <p>{content}</p>
    </div>
</div>""".format(id=self.id, top=self.top, left=self.left, width=self.width, height=self.height, depth=self.depth,
                title=self.title, content=self.body, backgroundColor=self.background, fontColor=self.fontColor)
      
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
      
    def setTitle(self, row):
        return row[7]
      
    def setBody(self, row):
        return row[8]

    def setBackground(self, row):
        return row[9]
     
    def setFontColor(self, row):
        return row[10]
     
