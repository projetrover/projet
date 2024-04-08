import "app-server"

import ServeurInstructions
import UserFactory
import Environnement
import VehiculeFactory

'''
TODO: BDD

'''
class Serveur:
    def __init__(self, users, vehicules, environnement):
        self.users = users
        self.vehicules = vehicules
        self.environnement = environnement
