import libclient as lc
import dataUser
import tkinter as tk

class Authentification:
    def __init__(self):
        self.username = None
        self.password = None
        self.state = tk.BooleanVar()        #Valide ou invalide en fonction de la reponse du serveur
        self.state.set(False)

    def login(self, username, password):
        """Envoie une requete de connexion au serveur, met self.state à True si la connexion a reussie,
        False sinon, renvoie la reponse de la requete, contient toutes les infos de l'utilisateur si la connexion
        a reussie"""
        #methode appelee quand on clique sur le bouton connexion du GUI
        self.username = username
        self.password = password
        answer = lc.create_request(-1, "login", {"username" : username, "password" : password})
        if 'iduser' in answer['result'] :
            self.state.set(True)
        else:
            self.state.set(False)
        return answer


    def disconnect(self):
        #TODO: toute la fonction
        pass
