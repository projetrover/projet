import vehicle

class Rover(vehicle.Vehicle):
    def __init__(self, pos, Height, durability = 100, battery = 100, ListeAnalyse = []):
        self.ListeAnalyse = ListeAnalyse
        vehicle.Vehicle.__init__(self, pos, Height, durability, battery)
