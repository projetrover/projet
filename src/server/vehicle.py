import camera
import map

MAX_Y = map.MAX_Y
MAX_X = map.MAX_X
DIRECTIONS={'up':0, 'right':1, 'down':2, 'left':3}
UP=0
RIGHT=1
DOWN=2
LEFT=3

class Vehicle:
    def __init__(self, pos, Height):
        self.durability = 100
        self.battery = 100
        self.height = Height
        self.pos = pos
        self.storedImgList = []
        self.storedVidList = []
        self.cam = camera.Camera()

    def move(self, direction, distance):
        dir = -1
        if direction in DIRECTIONS.keys():
            dir = DIRECTIONS[direction]
        elif direction in range(0, 4):
            dir = direction
        else:
             raise TypeError("Server->Vehicle->move : invalid direction.")
        (x,y) = self.pos
        if dir % 2 == 0 :
            distance = distance * (dir-1)
            y = y + distance
            if(y < 0):
                x = (x + (MAX_X/2) ) % MAX_X
                y = (-y) % MAX_Y
        else:
            distance = distance * (dir-2)
            x = ( x + distance ) % MAX_X
        self.pos = (x,y)

    def ChangeHealth(self, ammount):
        self.durability += ammount

    def ChangeBattery(self, ammount):
        self.durability += ammount


    def __str__(self):
        out = 'Durability: ' + str(self.durability) + ' Battery : ' + str(self.battery)
        out += ' Height:' + str(self.height) + ' Pos: ' + str(self.pos)
        return out
