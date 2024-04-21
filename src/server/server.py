import serverInstructions
import userFactory
import environment
import vehicleFactory
import json
import BDD_temp as bd

'''
TODO: BDD

'''
class Server:
    def __init__(self):
        self.userF = userFactory.UserFactory()
        self.vehicleF = vehicleFactory.VehicleFactory()
        self.environment = environment.Environment()



    def request_treatment(self, request):
        """Traitement de la requete request (dict), renvoie la reponse a envoyer au client"""
        idjoueur = request.get("idjoueur")
        action = request.get("action")
        value = request.get("value")
        answer = {'idjoueur' : idjoueur,
                'action' : action,
                'value' : value}
        
        if action == "login":
            username = value["username"]
            password = value["password"]
            #TODO: FINIR TRAITEMENT LOGIN



        elif action == "move_rover":
            #Si pas de rocher ni obstacle hauteur
            
            self.vehicles.roverList[idjoueur].move(value, 1)
            answer["result"] = "success"
        return answer
