class Tile:
    def __init__(self,x,y,id,w):
        self.x = x
        self.y = y
        self.id = id
        self.w = w
        self.Pimg = loadImage("Player.png")
        
    def show(self):
        if self.id == 'H':
            fill(250,70,70)
        elif self.id == 'T':
            fill(70,250,70)
        elif self.id == 'P':
            fill(100,100,250)
        else:
            noFill()
            
        stroke(255)
        strokeWeight(2)
        
        rect(self.x,self.y,self.w,self.w)
            
