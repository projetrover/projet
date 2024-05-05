import rover
import helico

class VehicleFactory:
    '''
    Rover casse -> nouveau rover au spawn
    Helico casse -> peut en recreer un mais met un cd pour les suivants
    '''
    def __init__(self):
        '''
        dictionaires au format {Id: Objet}
        L'Id est le meme s'il correspond au meme User
        '''
        self.roverList = {}
        self.helicoList = {}



    def newVehicles(self, Id, pos):
        self.roverList[Id] = rover.Rover(pos, 0)
        self.helicoList[Id] = helico.Helico(pos, 0)

    def createVehicle(self, Id, pos, dir, type, durability, battery, analysisDict={}):
        if type == 'Helico':
            self.helicoList[Id] = helico.Helico(pos, dir, 0, durability, battery)
        elif type == 'Rover':
            self.roverList[Id] = rover.Rover(pos, dir, 0, durability, battery, analysisDict)
        else:
            raise TypeError("Server->VehicleFactory->createVehicle : mauvais type.")


    def delVehicle(self, Id, type):
        if type == 'Rover': #TODO: blabla
            del self.roverList[Id]
        elif type == 'Helico':
            del self.helicoList[Id]
            del self.helicoPos[Id]
			#TODO: blabla
        else:
            raise TypeError("Server->VehicleFactory->delVehicle : mauvais type.")



    def __str__(self):
        rl = "rovers : ["
        hl = "helicos : ["
        for k in self.roverList:
            rl += " " + str(k)
        for k in self.helicoList:
            hl += " " + str(k)
        rl += " ]"
        hl += " ]"
        return rl + " " + hl
