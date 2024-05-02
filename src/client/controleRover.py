import dataUser
import libclient

#TODO: Tout
class ControleRover:
    def __init__(self):
        self.rover = dataUser.data.rover

    def move(self, dir):
        """Envoie une requete de deplacement pour le type (0 : rover ou 1 : helico) dans la direction dir (0 || 1 || 2 || 3)"""
        libclient.create_request(dataUser.data.userid, 'move_rover', dir)
