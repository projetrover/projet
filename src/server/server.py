#import serverInstructions
import userFactory
import environment
import vehicleFactory
import userFactory
import json

'''
TODO: TESTER LOGIN

'''
class Server:
    def __init__(self):
        self.userF = userFactory.UserFactory()
        self.vehicleF = vehicleFactory.VehicleFactory()
        self.environment = environment.Environment()
        self.online_users = []          #Liste des id des utilisateurs connectes

    def load(self):  #TODO: chargement map
        try:
            f = open('src/server/data.json')
        except :
            f = open('data.json')
        data = json.load(f)

        for iduser in data['users']:
            user = data['users'][iduser]
            self.userF.UserDict[int(iduser)] = userFactory.user.User(user['username'], user['password'], int(user['iduser']))
        
        for idrover in data['vehicles']['roverList']:
            rover = data['vehicles']['roverList'][idrover]
            self.vehicleF.createVehicle(int(idrover), (int(rover['pos'][0]), int(rover['pos'][1])), "Rover", int(rover['durability']), int(rover['battery']), rover['ListeAnalyse'])

        for idheli in data['vehicles']['helicoList']:
            heli = data['vehicles']['helicoList'][idheli]
            self.vehicleF.createVehicle(int(idheli), (int(heli['pos'][0]), int(heli['pos'][1])), "Helico", int(heli['durability']), int(heli['battery']))

            

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
        
        try :
            with open("src/server/data.json", "w") as outfile:
                outfile.write(json_object)
        except :
            with open("data.json", "w") as outfile:
                outfile.write(json_object)


    def request_treatment(self, request):
        """Traitement de la requete request (dict), renvoie la reponse a envoyer au client"""
        idjoueur = request.get("idjoueur")
        action = request.get("action")
        value = request.get("value")
        answer = {}

        if action == "login":               #Login
            username = value["username"]
            password = value["password"]
            for userid in self.userF.UserDict:
                user = self.userF.UserDict[userid]
                if user.username == username :
                    if user.password == password :
                        self.online_users.append(userid)
                        rover = self.vehicleF.roverList[userid]
                        answer["result"] = {"userid" : userid,
                                            "rover" : {'ListeAnalyse' : rover.ListeAnalyse,
                                                       'durability' : rover.durability,
                                                       'battery' : rover.battery,
                                                       'height' : rover.height,
                                                       'pos' : rover.pos},
                                                
                                             }  #TODO: Mettre toutes les infos du user map discovered
                        
                        if userid in self.vehicleF.helicoList :
                            helico = self.vehicleF.helicoList[userid]
                            answer['result']['helico'] = {'durability' : helico.durability,
                                                       'battery' : helico.battery,
                                                       'height' : helico.height,
                                                       'pos' : helico.pos}
                        else: 
                            answer["result"]['helico'] = 'None'
                        return answer

            else:
                answer["result"] = "incorrect user or passwd"




        elif action == "move_rover":
            #Si pas de rocher ni obstacle hauteur

            self.vehicles.roverList[idjoueur].move(value, 1)
            answer["result"] = "success"
        
        
        return answer
