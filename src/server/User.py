import VehiculeFactory
import Carte

class User:
    def __init__(name, password, roverId, helicoId):
        self.name = name
        self.password = password
        self.roverId = rover #probablement un id qui ramene a VehiculeFactory
        self.helicoId = helico #probablement un id qui ramene a VehiculeFactory
        self.DiscoveredMap = []
        self.DisplayedMap = []
