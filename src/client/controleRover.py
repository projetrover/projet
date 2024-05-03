import dataUser
import libclient

#TODO: Tout
class ControleRover:
    def __init__(self):
        self.rover = dataUser.data.rover

    def move(self, dir):
        """Envoie une requete de deplacement dans la direction dir (0 || 1 || 2 || 3)"""
        libclient.create_request(dataUser.data.userid, 'move_rover', dir)

    def analyse(self, dir):
        """Envoie une requete d'analyse de rocher au serveur dans la direction dir (0 || 1 || 2 || 3)"""
        libclient.create_request(dataUser.data.userid, 'analyse', dir)