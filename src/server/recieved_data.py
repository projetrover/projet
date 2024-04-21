#PROBABLEMENT INUTILE


#Je sais pas a quoi c'est cense servir, peut etre data_user ???

#fichier temporaire pour pouvoir executer server, a corriger des que possible
#import Serveur
#TODO: sauvegarde & lecture de sauvegarde
import environment    as en
import userFactory    as uf
import vehicleFactory as vf
'''
Endroit pour stoquer les messages recus cote client
'''
class RecievedData:
	def __init__(self):
		self.users = 0
		self.map = 0
