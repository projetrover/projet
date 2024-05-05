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
    """Classe controleur principale du serveur"""
    def __init__(self):
        self.userF = userFactory.UserFactory()
        self.vehicleF = vehicleFactory.VehicleFactory()
        self.environment = environment.Environment()
        self.online_users = []          #Liste des id des utilisateurs connectes
        self.seed = random.randint(100000, 999999)
        self.serverTimer = 0


    def serverTick(self, tick):
       self.serverTimer += tick
       self.meteoCheck()
       self.environment.updateMeteo(self.serverTimer)

    def start(self, serviceDuration):
        self.environment.generate_topography()
        print(self.environment.topography[0][0], self.environment.topography[1][0], self.environment.topography[2][0], self.environment.topography[3][0])
        #self.environment.generate_meteoMap(self.seed, serviceDuration)
        self.environment.generate_loot(self.seed)
        print('Server is ready')

    def load(self):  #TODO: chargement map
        """Charge les donnees du serveur"""
        try:
            f = open("src/server/data.json")
        except :
            f = open("data.json")
        data = json.load(f)

        for iduser in data["users"]:
            user = data["users"][iduser]
            self.userF.UserDict[iduser] = userFactory.user.User(user["username"],
                user["password"], user["iduser"])

        for idrover in data["vehicles"]["roverList"]:
            rover = data["vehicles"]["roverList"][idrover]
            self.vehicleF.createVehicle(int(idrover), [int(rover["pos"][0]), int(rover["pos"][1])], int(rover['dir']),"Rover", int(rover["durability"]),
                                        int(rover["battery"]), rover["analysisDict"])

        for idheli in data["vehicles"]["helicoList"]:
            heli = data["vehicles"]["helicoList"][idheli]
            self.vehicleF.createVehicle(int(idheli), [int(heli["pos"][0]),
                int(heli["pos"][1])], int(heli['dir']), "Helico", int(heli["durability"]), int(heli["battery"]))
        self.seed = data["seed"]
        self.serverTimer = data["serverTimer"]

        denv = data['environment']
        self.environment.mapSize = (int(denv['mapSize'][0]), int(denv['mapSize'][0]))
        self.environment.materials = denv['materials']
        self.environment.lootDict = denv['lootDict']
        self.environment.looted = denv['looted']
        self.environment.meteoDict = denv['meteoDict']
        self.environment.currentMeteos = denv['currentMeteos']
        self.environment.endedMeteos = denv['endedMeteos']
        self.environment.meteoMap = denv['meteoMap']



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


    def loginRequest(self, value):
        """Traitement des requetes de connexion"""
        answer = {}
        username = value["username"]
        password = value["password"]
        for userid in self.userF.UserDict:
            user = self.userF.UserDict[userid]
            if user.username == username :
                if user.password == password :
                    self.online_users.append(int(userid))
                    rover = self.vehicleF.roverList[int(userid)]
                    answer["result"] = {"userid" : userid,
                                        "rover" : {"analysisDict" : rover.analysisDict,
                                                   "dir" : rover.dir,
                                                    "durability" : rover.durability,
                                                    "battery" : rover.battery,
                                                    "height" : rover.height,
                                                    "pos" : rover.pos},

                                            }  #TODO: Mettre toutes les infos du user map discovered

                    if userid in self.vehicleF.helicoList :
                        helico = self.vehicleF.helicoList[userid]
                        answer["result"]["helico"] = {"durability" : helico.durability,
                                                      "dir" : helico.dir,
                                                    "battery" : helico.battery,
                                                    "height" : helico.height,
                                                    "pos" : helico.pos}
                    else:
                        answer["result"]["helico"] = "None"
                    return answer

        else:
            answer["result"] = "incorrect user or passwd"

    def moveRoverRequest(self, Id, value):
        """Traitement des requtes de mouvement des rover"""
        #TODO: gerer les chutes
        MAX_X,MAX_Y = self.environment.mapSize
        value = int(value)
        answer = {}
        dmg = 5     #degats infliges en cas de Collision
        eng = 1     #energie perdue
        vehicleCollision = False
        if Id in self.online_users:
            rover = self.vehicleF.roverList[Id]
            rover.dir = value           #On change la direction dans laquelle regarde le rover
            (x, y) = int(rover.pos[0]), int(rover.pos[1])
            #print(x, y)
            #en supposant que value soit un vecteur x,y peut modifier pour que ca match
            if value >= 0 and value < 4: # 0:up 1:right 2:down 3:left
                if (value % 2) == 0:
                    dx, dy = x, y +(value-1)
                    if(y < 0 or y > MAX_Y):
                        #TODO: alerte tour du monde en Y
                        dx, dy = (x + (MAX_X/2) ) % MAX_X, (-y) % MAX_Y
                else:
                    #TODO: ne gere pas le tour du monde en X
                    dx, dy = x-(value-2), y
            else:
                raise Exception('Wrong direction')
            #TODO: check hauteur mieux
                                                                                                          #Si on est > ca passe, si on est <, on se donne une fourchette de 2500,
            #if (self.environment.topography[x][y] + 2500 >= self.environment.topography[dx % 122][dy % 86]):       #Si on devient > ca passe, sinon ca passe pas

            for k in self.vehicleF.roverList:           #Collision avec autre rover
                if (dx,dy) == self.vehicleF.roverList[k].pos:
                    vehicleCollision = True

            else:
                if (dx,dy) in self.environment.lootDict.keys():     #Collision avec rocher
                    vehicleCollision = True

            #else:
            #   vehicleCollision = True

            if vehicleCollision:
                    rover.ChangeHealth(-dmg)     #5 de dégâts
                    answer["result"] = {'state' : 'not moved', 'damage' : dmg, 'battery_lost' : eng, 'dir' : value}
            else :
                rover.move(value, 1)
                rover.height = self.environment.topography[dx][dy]      #Pas vraiment utile d'envoyer la hauteur au client je pense
                answer["result"] = {'state' : 'moved', 'pos' : rover.pos ,'battery_lost' : eng, 'dir'  : value}
            rover.ChangeBattery(-eng)
        else:
            answer["result"] = "incorrect user or offline"
        return answer
    
    def deployHelicoRequest(self, Id):
        """Traitement des requetes de deploiment des helicos"""
        if Id not in self.online_users:
            return {"result" : "incorrect user or offline"}
        self.vehicleF.createVehicle(Id, [self.vehicleF.roverList[Id].pos[0], self.vehicleF.roverList[Id].pos[1]], 0, "Helico", 100, 100)
        answer = {}
        helico = self.vehicleF.helicoList[Id]
        answer['result'] = {'state' : "helico deployed", "pos" : helico.pos, "battery" : helico.battery, "durability" : 100, "height": helico.height, "dir" : helico.dir}
        return answer
    
    def removeHelicoRequest(self, Id):
        """Traitement des requetes de rangement des helicos"""
        if Id not in self.online_users:
            return {"result" : "incorrect user or offline"}
        answer = {}
        print("------------",self.vehicleF.roverList[Id].pos, self.vehicleF.helicoList[Id].pos)
        if (self.vehicleF.roverList[Id].pos[0] != self.vehicleF.helicoList[Id].pos[0]) or (self.vehicleF.roverList[Id].pos[1] != self.vehicleF.helicoList[Id].pos[1]):
            answer['result'] = "Heli not on rover"
        else:
            del self.vehicleF.helicoList[Id]
            answer["result"] = "Heli removed"
        return answer

    def moveHelicoRequest(self, Id, value):
        """Traitement des requetes de mouvement des helico"""
        #TODO: gerer les chutes
        MAX_X,MAX_Y = self.environment.mapSize
        value = int(value)
        answer = {}
        dmg = 10     #degats infliges en cas de Collision
        eng = 2     #energie perdue
        vehicleCollision = False
        if Id in self.online_users:
            helico = self.vehicleF.helicoList[Id]
            helico.dir = value           #On change la direction dans laquelle regarde le rover
            (x, y) = int(helico.pos[0]), int(helico.pos[1])
            #print(x, y)
            #en supposant que value soit un vecteur x,y peut modifier pour que ca match
            if value >= 0 and value < 4: # 0:up 1:right 2:down 3:left
                if (value % 2) == 0:
                    dx, dy = x, y +(value-1)
                    if(y < 0 or y > MAX_Y):
                        #TODO: alerte tour du monde en Y
                        dx, dy = (x + (MAX_X/2) ) % MAX_X, (-y) % MAX_Y
                else:
                    #TODO: ne gere pas le tour du monde en X
                    dx, dy = x-(value-2), y
            else:
                raise Exception('Wrong direction')
            #TODO: check hauteur mieux
                                                                                                          #Si on est > ca passe, si on est <, on se donne une fourchette de 2500,
            #if (self.environment.topography[x][y] + 2500 >= self.environment.topography[dx % 122][dy % 86]):       #Si on devient > ca passe, sinon ca passe pas

            for k in self.vehicleF.helicoList:           #Collision avec autre rover
                if (dx,dy) == self.vehicleF.helicoList[k].pos:
                    vehicleCollision = True

            #else:
            #   vehicleCollision = True

            if vehicleCollision:
                    helico.ChangeHealth(-dmg)     #5 de dégâts
                    answer["result"] = {'state' : 'not moved', 'damage' : dmg, 'battery_lost' : eng, 'dir' : value}
            else :
                helico.move(value, 1)
                helico.height = self.environment.topography[dx][dy]      #Pas vraiment utile d'envoyer la hauteur au client je pense
                answer["result"] = {'state' : 'moved', 'pos' : helico.pos ,'battery_lost' : eng, 'dir'  : value}
            helico.ChangeBattery(-eng)
        else:
            answer["result"] = "incorrect user or offline"
        return answer


    def analyserRocherRequest(self, Id, value): #TODO:Toute la methode cote server + client
        """Traitement des requetes d'analyse de rocher"""
        MAX_X,MAX_Y = self.environment.mapSize
        answer = {}
        if Id in self.online_users:
            rover = self.vehicleF.roverList[Id]
            (x, y) = rover.pos
            if value >= 0 and value < 4: # 0:up 1:right 2:down 3:left
                if (value % 2) == 0:
                    dx, dy = x, y +(value-1)
                    if(y < 0):
                        dx, dy = (x + (MAX_X/2) ) % MAX_X, (-y) % MAX_Y
                else:
                    dx, dy = x-(value-2), y
            else:
                raise Exception('Wrong direction')
            # print(self.environment.lootDict[(60, 8)])
            # print(dx, dy)
            # print(self.environment.lootDict)
            if (dx, dy) in self.environment.lootDict:
                self.vehicleF.roverList[Id].analyze(self.environment.lootDict[(dx,dy)])
                alert = "recolte de" + self.environment.lootDict[(dx,dy)]           #TODO: eventuellement rajouter la perte d'energie
                self.environment.collect((dx,dy))
                answer["result"] = {"state" : "successful",
                                    "analysisDict" : rover.analysisDict,
                                    "alert" : alert}
            else :
                answer["result"] = {"state" : "failed"}
        else:
            answer["result"] = {"state" : "failed"}

        return answer

    def data_update(self):
        """Traitement des requetes de maj des infos client"""
        answer = {}
        answer['result'] = {
            'currentMeteos' : []
        }
        # for k in environment.currentMeteo.keys():
        #     answer['result']['currentMeteos']self.environment.currentMeteo[k]["pos"]

        lootDict=[]
        for k in self.environment.lootDict:
            lootDict.append(k)
        roverpos = []
        helicopos = []
        for k in self.online_users:
            roverpos.append(self.vehicleF.roverList[k].pos)
            if k in self.vehicleF.helicoList:
               helicopos.append(self.vehicleF.helicoList[k].pos)
        answer["result"]["lootDict"] = lootDict
        answer["result"]["roverPos"] = roverpos
        answer["result"]["helicoPos"] = helicopos

        return answer



    def request_treatment(self, request):
            '''Traitement de la requete request (dict), renvoie la reponse a envoyer au client'''
            idjoueur = request.get("idjoueur")
            action = request.get("action")
            value = request.get("value")

            if action == "data_update":
                answer = self.data_update()

            elif action == "login":
                answer = self.loginRequest(value)

            elif action == "move_rover":
                answer = self.moveRoverRequest(idjoueur, value)

            elif action == "analyse":
                answer = self.analyserRocherRequest(idjoueur, value)
            
            elif action == "move_helico":
                answer = self.moveHelicoRequest(idjoueur, value)
            
            elif action == "deploy_helico":
                answer = self.deployHelicoRequest(idjoueur)
            
            elif action == "remove_helico":
                answer = self.removeHelicoRequest(idjoueur)

            return answer

    def meteoCheck(self):
        for k in self.online_users:
            rovPos = self.vehicleF.roverList[k].pos
            helPos = self.vehicleF.helicoList[k].pos
            for m in self.environment.currentMeteos.keys():
                # IdMeteo 1 == tempete sable
                if self.environment.currentMeteos[m]["IdMeteo"] == 1:
                    if self.environment.checkDistance(m,helPos):
                        self.vehicleF.helicoList[k].ChangeHealth(-1)
                    if self.environment.checkDistance(m,rovPos):
                        self.vehicleF.roverList[k].ChangeHealth(-1)



#end of file
