import map as m
from PIL import Image
FILE = "../../Images/mercat.jpg"

MAP_SIZE = (m.MAX_X, m.MAX_Y)
MATERIALS = {"diamond":50, "iron":200, "rock":600}

#TODO: Creer une SEED et methodes gerant meteo + carte

class Environment:
    def __init__(self):
        (x, y) = MAP_SIZE
        self.topography = m.Map(x, y)
        self.meteo = m.Map(20,20)


    def generate_topography(self):
        '''
        genere les hauteurs, TODO: rendre cela + accurate
        '''
        im = Image.open(FILE, mode='r')
        (x, y) = MAP_SIZE
        for i in range(x):
            for j in range(y):
                (r, g, b) = im.getpixel((i,j))
                if b > r:
                    h = -b*20 - g * 8
                else:
                    h = r * 20 + g * 40
                self.topography.set(i, j, h)
