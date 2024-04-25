class DataUser:
    def __init__(self, userid, rover, helico = None, discoveredmap = None):
        self.userid = userid
        self.rover = rover          #Rover et helico seront ici directement des dicos pour gagner du temps
        self.helico = helico
        self.discoveredmap = discoveredmap
        
