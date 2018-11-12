class Post:
    def __init__(self, row):
        self.html = self.buildHtml()
        setId(row[1]);
        #setLocation(row[2], row[3])
        #setSize(row[4], row[5])
        #setDepth(row[6]);
        #setTitle(row[7]);
        #setBody(row[8]);
        #setBackground(row[9]);
        #setFontColor(row[10]);

    #@override
    def buildHtml(self):
        return """
<div id="{id}" class="border border-dark rounded draggable resizable post" style="width: {{width}}px; height: {{height}}px; position: absolute; z-index: {{depth}}; left: {{left}}px; top: {{top}}px;">
    <button class="editPost edit" type="button" style="position: absolute; top: 0; right: 0;" data-toggle="modal" data-target="#exampleModal">Edit</button>
    <div id="originalContent" style="width: 100%; height: 100%; background-color: {{backgroundColor}}; color: {{fontColor}};">
        <h3>{{title}}</h3>
        <p>{{content}}</p>
    </div>
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
      
    def setTitle(self, title):
        self.html.format(title=title)
      
    def setBody(self, content):
        self.html.format(content=content)

    def setBackground(self, backgroundColor):
        self.html.format(backgroundColor=backgroundColor)
     
    def setFontColor(self, fontColor):
        self.html.format(fontColor=fontColor)
     
