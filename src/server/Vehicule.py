import Camera

MAX_Y = 384 #(6912//18)
MAX_X = 668 #(12032//18)

class Vehicle:
    def __init__(self, pos=(0,0), Height=0):
        self.Durability = 100
        self.Battery = 100
        self.Height = Height
        self.pos = pos
        self.storedImgList = []
        self.storedVidList = []
        self.Camera = Camera()
        self.directions {"up":0, "right":1, "down":2, "left":3}

    def move(self, direction, distance):
        dir = -1
        if direction in self.directions:
            dir = self.directions[direction]
        else:
             raise TypeError("Server->Vehicle->move : invalid direction.")
        (x,y) = self.pos
        if direction % 2 == 0 :
            distance = distance * (direction-1)
            y = y + distance
            if(y < 0):
                x = (x + (MAX_X/2) ) % MAX_X
                y = (-y) % MAX_Y
        else:
            distance = distance * (direction-2)
            x = ( x + distance ) % MAX_X
        self.pos = (x,y)
        
    def ChangeHealth(self, ammount):
    	self.Durability += ammount
    	
    def ChangeBattery(self, ammount):
    	self.Durability += ammount
    	
    
