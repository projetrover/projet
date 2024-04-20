import map

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.discoveredMap = map.Map(map.MAX_X, map.MAX_Y)
        #tres couteux, besoin d'optimiser pour scale

    def discover(self, x, y, chunk):
        self.discoveredMap.set(x, y, chunk)
        pass

    def __str__(self):
        s = 'Username : ' + self.username + ' Password: ' + self.password
        return s
