import map as m

MAP_SIZE = (500, 700)
MATERIALS = {"diamond":50, "iron":200, "rock":600}

class Environment:
    def __init__(self):
        (x, y) = MAP_SIZE
        self.topography = m.Map(x, y)
        self.meteo = meteo


    def generate_topography(self):
        (x, y) = MAP_SIZE
        for i in range(x):
            for j in range(y):
                self.topography[i][j] = i*j
                
