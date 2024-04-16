import json

def request_treatment(request):
    idjoueur = request.get("idjoueur")
    action = request.get("action")
    value = request.get("value")

    if "action" == "move_rover":
        return
