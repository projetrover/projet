import Vehicule

class Rover(vehicule):
    def __init__(self, pos=(0,0), Height=0):
        self.ListeAnalyse = []
        vehicule.__init__(self, pos, Height)