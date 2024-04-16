import Rover
import Helico

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
        self.RoverList = {}
        self.HelicoList = {}


	def NewVehicles(self, Id, pos):
		self.RoverList[Id] = Rover(pos, 0)
		self.RoverList[Id] = Helico(pos, 0)
		
	
	def DelVehicle(self, Id, type):
		if type == "Rover":
			#TODO: blabla
		elif type == "Helico":
			#TODO: blabla
		else:
			raise TypeError("Server->VehicleFactory->DelVehicle : mauvais type.")
			
		
		
		
        
