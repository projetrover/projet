#import serverInstructions
import userFactory
import environment
import vehicleFactory
import json

'''
TODO: BDD

'''
class Server:
    def __init__(self):
        self.userF = userFactory.UserFactory()
        self.vehicleF = vehicleFactory.VehicleFactory()
        self.environment = environment.Environment()


    def save(self):  #TODO: Finir save
        """Enregistre l'état du serveur"""
        dico = {}

        users = {}
        for iduser in self.userF.UserDict:       #TODO: PENSER A SAVE LA MAP ET L'ENVIRONEMENT
            users[iduser] = {"iduser" : iduser, "username" : self.userF.UserDict[iduser].username, "password" : self.userF.UserDict[iduser].password }
        dico["users"] = users

        roverlist = {}
        for idrover in self.vehicleF.roverList:
            roverlist[idrover] = self.vehicleF.roverList[idrover].__dict__

        helicolist = {}
        for idheli in self.vehicleF.helicoList:
            helicolist[idheli] = self.vehicleF.helicoList[idheli].__dict__

        vehicles = {"roverList" : roverlist, "helicoList" : helicolist}
        dico["vehicles"] = vehicles


        print("DICO = ",dico)

        json_object = json.dumps(dico, indent=4)
        with open("data.json", "w") as outfile:
            outfile.write(json_object)


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
            for userid in bd.accounts:
                if bd.accounts[userid][0] == username :
                    if bd.accounts[userid][1] == password :
                        answer["result"] = {"userid" : userid
                                             }  #TODO: Mettre toutes les infos du user
            else:
                answer["result"] = "incorrect user or passwd"




        elif action == "move_rover":
            #Si pas de rocher ni obstacle hauteur

            self.vehicles.roverList[idjoueur].move(value, 1)
            answer["result"] = "success"
        return answer
