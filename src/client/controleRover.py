import dataUser
import libclient

#TODO: Tout
class ControleRover:
    def __init__(self):
        self.rover = dataUser.data.rover

    def move(self, type, dir):
        """Envoie une requete de deplacement pour le type (0 : rover ou 1 : helico) dans la direction dir (0 || 1 || 2 || 3)"""
        if dir == 0 :       #up
            dx, dy = 0, 1
        elif dir == 1:      #right
            dx, dy = 1, 0
        elif dir == 2:      #down
            dx, dy = 0, -1
        elif dir == 3:      #left
            dx, dy = -1, 0
        else:
            raise Exception('Wrong direction')
        
        if type == 0:
            libclient.create_request(dataUser.data.userid, 'move_rover', (dx, dy))
        elif type == 1:
            libclient.create_request(dataUser.data.userid, 'move_helico', (dx, dy))
        else:
            raise Exception('Wrong type')
