import Camera

class Vehicule:
    def __init__(self, cam, pos=(0,0), Hauteur=0):
        self.Durabilite = 100
        self.Batterie = 100
        self.Hauteur = Hauteur
        self.pos = pos
        self.storedImgList = []
        self.storedVidList = []
        self.Camera = cam
        
