import vehicle

class Rover(vehicle.Vehicle):
    def __init__(self, pos, Height):
        self.ListeAnalyse = []
        vehicle.Vehicle.__init__(self, pos, Height)
