import vehicle

class Helico(vehicle.Vehicle):
    def __init__(self, pos, Height, durability = 100, battery = 100):
        vehicle.Vehicle.__init__(self, pos, Height, durability, battery)