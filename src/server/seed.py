import numpy as np

class Seed:
    def __init__(self, **kwargs):
        '''
        gestion de generation de la carte et des collectibles
        '''
        k = kwargs.keys()
        self.seed = 0
        if len(k) == 0:
            self.seed = self.createSeed()
        if len(k) == 1:
            self.seed = kwargs[seed]
        print("ca marchera +/-")


    def createSeed(self):
        #TODO: seed
        return 0
