import json

def request_treatment(request):
    global serv

    print("REQ TREAT")
    idjoueur = request.get("idjoueur")
    action = request.get("action")
    value = request.get("value")
    answer = {'idjoueur' : idjoueur,
            'action' : action,
            'value' : value}
    
    #TODO: acceder a l'objet server
    #if action == "move_rover":
                #Si pas de rocher ni obstacle hauteur
        
        #serv.vehicles.roverlist[idjoueur].move(value, 1)
        #answer["result"] = "success"
        #return answer
