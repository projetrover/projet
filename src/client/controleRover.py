import dataUser
import libclient

#TODO: Tout
class ControleRover:
    def __init__(self):
        self.rover = dataUser.data.rover

    def move(self, dir):
        """Envoie une requete de deplacement pour le rover dans la direction dir (up || down || left || right)"""
        #libclient.message._create_message(...)
        pass
