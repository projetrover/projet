import VehiculeFactory
import Carte

class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.DiscoveredMap = []
        self.DisplayedMap = []
