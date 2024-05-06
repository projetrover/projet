import dataUser
import libclient

#TODO: Tout
class ControleRover:
    def __init__(self):
        self.rover = dataUser.data.rover

    def movereq(self, dir):
        """Envoie une requete de deplacement dans la direction dir (0 || 1 || 2 || 3)"""
        return libclient.create_request(dataUser.data.userid, 'move_rover', dir)

    def analysereq(self):
        """Envoie une requete d'analyse de rocher au serveur"""
        return libclient.create_request(dataUser.data.userid, 'analyse', 0)