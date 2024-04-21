import libclient as lc

class Authentification:
    def __init__(self):
        self.username = None
        self.password = None
        self.state = None        #Valide ou invalide en fonction de la reponse du serveur

    def login(self, username, password):
        """Envoie une requete de connexion au serveur"""
        #methode appelee quand on clique sur le bouton connexion du GUI
        self.username = username
        self.password = password
        self.state = lc.create_request(-1, "login", {"username" : username, "password" : password})

    def disconnect(self):
        #TODO: toute la fonction
        pass