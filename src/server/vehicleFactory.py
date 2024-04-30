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
        vehiclePos sert a faciliter les calculs de colision entre vehicules
        {Id: [(posRover),(posHelico)]}
        '''
        self.roverList = {}
        self.helicoList = {}
        self.vehiclePos = {}



    def newVehicles(self, Id, pos):
        self.roverList[Id] = rover.Rover(pos, 0)
        self.helicoList[Id] = helico.Helico(pos, 0)
        self.vehiclePos[iD] = [self.helicoList[Id].pos, self.roverList[Id].pos]

    def createVehicle(self, Id, pos, type, durability = 100, battery = 100, ListeAnalyse = []):
        if type == 'Helico':
            self.helicoList[Id] = helico.Helico(pos, 0, durability, battery)
        elif type == 'Rover':
            self.roverList[Id] = rover.Rover(pos, 0, durability, battery, ListeAnalyse)
        else:
            raise TypeError("Server->VehicleFactory->createVehicle : mauvais type.")


    def delVehicle(self, Id, type):
        if type == 'Rover': #TODO: blabla
            del self.roverList[Id]
        elif type == 'Helico':
            del self.helicoList[Id]
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
