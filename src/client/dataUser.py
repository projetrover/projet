#POTENTIEL PROBLEME IL RISQUE DE RECREER UN OBJET A CHAQUE FOIS, CE N'EST PAS CE QUE L'ON VEUT
#Mais visiblement on a pas de probleme, a surveiller

class DataUser:
    def __init__(self, userid = None, rover = None, helico = None, discoveredmap = None):
        self.userid = userid
        self.rover = rover          #Rover et helico seront ici directement des dicos pour gagner du temps
        self.helico = helico
        self.discoveredmap = discoveredmap
        
data = DataUser()