import libclient as lc
import dataUser
import tkinter as tk

class Authentification:
    def __init__(self):
        self.username = None
        self.password = None
        self.state = tk.BooleanVar(value = False)        #Valide ou invalide en fonction de la reponse du serveur

    def login(self, username, password):
        """Envoie une requete de connexion au serveur, met self.state à True si la connexion a reussie,
        False sinon, renvoie la reponse de la requete, met à jour dataUser.data si la connexion
        a reussie"""
        #methode appelee quand on clique sur le bouton connexion du GUI
        self.username = username
        self.password = password
        answer = lc.create_request(-1, "login", {"username" : username, "password" : password})
        if 'userid' in answer['result'] :
            self.state.set(True)
            result = answer['result']
            dataUser.data.userid = int(result['userid'])
            dataUser.data.rover = result['rover']   #On laisse en dico de str pour l'instant, on verra plus tard pour changer si besoin
            print(type(dataUser.data.rover['durability']))
            if 'helico' in result:
                dataUser.data.helico = result['helico']


    def disconnect(self):
        #TODO: toute la fonction
        pass
