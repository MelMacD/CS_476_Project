class Post:
    def __init__(self, row):
        self.html = self.buildHtml()
        #setLocation(row.get("top"), row.get("left"))
        #setSize(row.get("width"), row.get("height"))
        #setDepth(row.get("depth"));
        #setTitle(row.get("title"));
        #setBody(row.get("content"));
        #setBackground(row.get("backgroundColor"));
        #setFontColor(row.get("fontColor"));

    #@override
    def buildHtml(self):
        return """
<div class="border border-dark rounded draggable resizable" style="width: {width}px; height: {height}px; position: absolute; z-index: {depth}; left: {left}px; top: {top}px;">
    <button class="editPost edit" type="button" style="position: absolute; top: 0; right: 0;" data-toggle="modal" data-target="#exampleModal">Edit</button>
    <div id="originalContent" style="width: 100%; height: 100%; background-color: {backgroundColor}; color: {fontColor};">
        <h3>{title}</h3>
        <p>{content}</p>
    </div>
</div>"""
      
    #@override
    def setLocation(self, top, left):
         return self.html.format(top=top, left=left)
     
    #@override
    def setSize(self, width, height):
         return self.html.format(width=width, height=height)
     
    #@override
    def setDepth(self, depth):
        return self.html.format(depth=depth)
      
    def setTitle(self, title):
         return self.html.format(title=title)
      
    def setBody(self, content):
         return self.html.format(content=content)

    def setBackground(self, backgroundColor):
         return self.html.format(backgroundColor=backgroundColor)
     
    def setFontColor(self, fontColor):
         return self.html.format(fontColor=fontColor)
     
