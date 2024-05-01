#import serverInstructions
import userFactory
import environment
import vehicleFactory
import userFactory
import random
import json

'''
TODO:

'''
class Server:
    def __init__(self):
        self.userF = userFactory.UserFactory()
        self.vehicleF = vehicleFactory.VehicleFactory()
        self.environment = environment.Environment()
        self.online_users = []          #Liste des id des utilisateurs connectes
        self.seed = random.randint(100000, 999999)
        self.serverTimer = 0

    def load(self):  #TODO: chargement map
        try:
            f = open("src/server/data.json")
        except :
            f = open("data.json")
        data = json.load(f)

        for iduser in data["users"]:
            user = data["users"][iduser]
            self.userF.UserDict[int(iduser)] = userFactory.user.User(user["username"],
                user["password"], int(user["iduser"]))

        for idrover in data["vehicles"]["roverList"]:
            rover = data["vehicles"]["roverList"][idrover]
            self.vehicleF.createVehicle(int(idrover), (int(rover["pos"][0]),
                int(rover["pos"][1])), "Rover", int(rover["durability"]),
                int(rover["battery"]), rover["analysisDict"])

        for idheli in data["vehicles"]["helicoList"]:
            heli = data["vehicles"]["helicoList"][idheli]
            self.vehicleF.createVehicle(int(idheli), (int(heli["pos"][0]),
                int(heli["pos"][1])), "Helico", int(heli["durability"]), int(heli["battery"]))
        self.seed = data["seed"]
        self.serverTimer = data["serverTimer"]


    def save(self):  #TODO: Finir save
        '''Enregistre l"état du serveur'''
        dico = {}

        users = {}
        for iduser in self.userF.UserDict:       #TODO: PENSER A SAVE LA MAP ET L"ENVIRONEMENT
            users[iduser] = {
                "iduser" : iduser,
                "username" : self.userF.UserDict[iduser].username,
                "password" : self.userF.UserDict[iduser].password }
        dico["users"] = users

        roverlist = {}
        for idrover in self.vehicleF.roverList:
            roverlist[idrover] = self.vehicleF.roverList[idrover].__dict__

        helicolist = {}
        for idheli in self.vehicleF.helicoList:
            helicolist[idheli] = self.vehicleF.helicoList[idheli].__dict__

        vehicles = {"roverList" : roverlist, "helicoList" : helicolist}
        dico["vehicles"] = vehicles

        env = {}
        env["mapSize"] = self.environment.mapSize
        #env["topography"] = self.environment.topography.tolist()
        env["materials"] = self.environment.materials
        env["lootDict"] = self.environment.lootDict     #a surveiller
        env["looted"] = self.environment.looted
        env["meteoDict"] = self.environment.meteoDict
        env["currentMeteos"] = self.environment.currentMeteos
        env["endedMeteos"] = self.environment.endedMeteos
        env["meteoMap"] = self.environment.meteoMap

        dico["environment"] = env

        dico["seed"] = self.seed
        dico["serverTimer"] = self.serverTimer

        #print("DICO = ",dico)

        json_object = json.dumps(dico, indent=4)

        try :
            with open("src/server/data.json", "w") as outfile:
                outfile.write(json_object)
        except :
            with open("data.json", "w") as outfile:
                outfile.write(json_object)


    def request_treatment(self, request):
        '''Traitement de la requete request (dict), renvoie la reponse a envoyer au client'''
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
                                            "rover" : {"analysisDict" : rover.analysisDict,
                                                       "durability" : rover.durability,
                                                       "battery" : rover.battery,
                                                       "height" : rover.height,
                                                       "pos" : rover.pos},

                                             }  #TODO: Mettre toutes les infos du user map discovered

                        if userid in self.vehicleF.helicoList :
                            helico = self.vehicleF.helicoList[userid]
                            answer["result"]["helico"] = {"durability" : helico.durability,
                                                       "battery" : helico.battery,
                                                       "height" : helico.height,
                                                       "pos" : helico.pos}
                        else:
                            answer["result"]["helico"] = "None"
                        return answer

            else:
                answer["result"] = "incorrect user or passwd"




        elif action == "move_rover":
            answer = self.moveRoverRequest(idjoueur, value)
            #Si pas de rocher ni obstacle hauteur


            self.vehicles.roverList[idjoueur].move(value, 1)
            answer["result"] = "success"


        return answer

        def serverTick(self, tick):
            self.serverTimer += tick

        def moveRoverRequest(self, Id, value):
            answer = {}
            if idjoueur in self.online_users:
                (x, y) = self.vehicleF.roverList[Id]
                #en supposant que value soit un vecteur x,y peut modifier pour que ca match
                dx,dy = x+ value[0], y+value[1]
                #TODO: check hauteur mieux
                if (self.environment.topography[x, y] > self.environment.topography[dx, dy] ) or (
                    self.environment.topography[dx, dy] < self.environment.topography[x, y] +30):
                    vehicleColision = False
                    for k in self.vehicleF.vehiclePos.keys():
                        if (dx,dy) == self.vehicleF.vehiclePos[k]:
                            vehicleColision = True
                    if vehicleColision:
                        #TODO: choisir les dgts sur les vehicles
                        answer["result"] = "collision vehicle"
                    else:
                        if (dx,dy) in self.environment.lootDict.keys():
                            self.vehicles.roverList[Id].analyze(self.environment.lootDict[(dx,dy)])
                            self.environment.collect((dx,dy))
                            alert = "recolte de" + self.environment.lootDict[(dx,dy)]
                            answer["result"]["alert"] = alert
                        self.vehicles.roverList[Id].move(value, 1)
                        answer["result"]["rover"] =  {"analysisDict" : rover.analysisDict,
                                   "durability" : rover.durability,
                                   "battery" : rover.battery,
                                   "height" : rover.height,
                                   "pos" : rover.pos}
                else:
                    #TODO: choisir les dgts sur les vehicles
                    answer["result"] = "collision mur trop haut"
            else:
                answer["result"] = "incorrect user or offline"
            return answer






















#end of file
