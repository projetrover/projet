import camera
import map

MAX_Y = map.MAX_Y
MAX_X = map.MAX_X
DIRECTIONS={'up':0, 'right':1, 'down':2, 'left':3}
UP=0
RIGHT=3
DOWN=2
LEFT=1

class Vehicle:
    def __init__(self, pos, dir, Height, durability = 100, battery = 100):
        self.dir = dir
        self.durability = durability
        self.battery = battery
        self.height = Height
        self.pos = list(pos)
        #self.storedImgList = []
        #self.storedVidList = []
        #self.cam = camera.Camera()

    def move(self, direction, distance):
        dir = -1
        '''
        if direction in DIRECTIONS.keys():
            dir = DIRECTIONS[direction]'''
        if direction in range(0, 4):
            dir = direction
        else:
             raise TypeError("Server->Vehicle->move : invalid direction.")
        (x,y) = self.pos
        if dir % 2 == 0 :
            distance = distance * (dir-1)
            y = y + distance
            if(y < 0 or y > MAX_Y):
                x = (x + (MAX_X/2) ) % MAX_X
                y = (-y) % MAX_Y
        else:
            distance = distance * (dir-2)
            x = ( x - distance ) % MAX_X
        self.pos = (x,y)


    def ChangeHealth(self, ammount):
        self.durability += ammount

    def ChangeBattery(self, ammount):
        self.battery += ammount


    def __str__(self):
        out = 'Durability: ' + str(self.durability) + ' Battery : ' + str(self.battery)
        out += ' Height:' + str(self.height) + ' Pos: ' + str(self.pos)
        return out

if __name__ == "__main__":
    test = Vehicle((50,50), 0, 0, 100, 100)
    test.move(3, 1)
    print(test.pos)
