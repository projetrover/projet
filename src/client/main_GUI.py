import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from os.path import exists
import appliUser
import controleRoverGUI
import controleHelicoGUI
import alerteGUI
import miniCarteGUI
import carteGUI
import libclient
import dataUser



def checkimg(image):
    '''Cherche l'image image et retourne son chemin, None si introuvable'''

    if exists("../../Images/"+image):
        return "../../Images/"+image
    elif exists("Images/"+image):
        return "Images/"+image
    return None

class MainGUI():
    '''Classe de l'interface principale'''

    def __init__(self, window):
        '''Initialise les attributs de l'interface: la fenêtre principale, le canvas, l'image de fond (carte), le rover et les autres sprites et les jauges de "points de vie" et d'énergie.
        vehicle_dir est le sens vers lequel le rover est tourné, utilisé pour les rotations. Le rover est positionné au milieu de l'écran'''
    
        imgmap = checkimg("map.jpg")
        imgrocher = checkimg("rock.png")
        imgdrone = checkimg("drone.png")
        imgrover = checkimg("rover.png")
        imgwind = checkimg("Wind_Storm.png")
        imgsand = checkimg("Sandstorm.png")
        
        

        
        self.window = window
        self.Canvas = tk.Canvas(self.window, width=1920, height=1080, bg="black")
        
        
        
        self.bg = ImageTk.PhotoImage(Image.open(imgmap))
        self.rock = ImageTk.PhotoImage(Image.open(imgrocher).resize((80, 80), Image.LANCZOS))
        self.drone = ImageTk.PhotoImage(Image.open(imgdrone).resize((80, 80), Image.LANCZOS))
        self.wind = ImageTk.PhotoImage(Image.open(imgwind).resize((80, 80), Image.LANCZOS))
        self.sand = ImageTk.PhotoImage(Image.open(imgsand).resize((80, 80), Image.LANCZOS))
        self.rover = ImageTk.PhotoImage(Image.open(imgrover).resize((80, 80), Image.LANCZOS))
       # print(920 - (dataUser.data.rover['pos'][0] * 80), 500 - (dataUser.data.rover['pos'][1] * 80))
        self.bg_id = self.Canvas.create_image(920 - (dataUser.data.rover['pos'][0] * 80), 500 - (dataUser.data.rover['pos'][1] * 80), image=self.bg, anchor = tk.NW)
        #self.Canvas.create_image(100, 100, image=self.rock)
        #self.Canvas.create_image(180, 100, image=self.drone)
        #self.Canvas.create_image(260, 100, image=self.wind)
        #self.Canvas.create_image(340, 100, image=self.sand)
         
         
        self.switch_btn = tk.Button(text="Switch",command=self.vehicle_switch)
        self.Canvas.create_window(900, 900,window = self.switch_btn)
        
        
        
        
        self.Canvas.pack()
    
        self.rov_ctrl = controleRoverGUI.ControleRoverGUI(self.window ,self.Canvas, self.bg_id)         #Sous classes
        self.rov_ctrl.spawn()
        self.vehicle = 0        #0: rover, 1: helico
        self.heli_ctrl = controleHelicoGUI.ControleHelicoGUI(self.window, self.Canvas, self.bg_id)
        self.alertes = alerteGUI.AlerteGUI()
        self.minimap = miniCarteGUI.MiniCarteGUI()
        self.carte = carteGUI.CarteGUI()

        self.ana_btn = tk.Button(text="Analyser",command=self.rov_ctrl.analyse)
        self.Canvas.create_window(970, 900,window = self.ana_btn)

    def data_update(self):
        answer = libclient.create_request(dataUser.data.userid, "data_update", 0)
        res = answer['result']
        dataUser.data.roverPos = res['roverPos']
        dataUser.data.helicoPos = res['helicoPos']
        dataUser.data.lootDict = res['lootDict']
        dataUser.data.currentMeteos = res['currentMeteos']
        
    
    
    def vehicle_switch(self):
        '''Change le vehicule courant'''
        print("self.vehicle = ", self.vehicle)
        if not self.vehicle:
            self.rov_ctrl.kubind()
            self.Canvas.itemconfigure(self.rov_ctrl.wHP, state = "hidden")
            self.Canvas.itemconfigure(self.rov_ctrl.wenergy, state = "hidden")
            self.Canvas.itemconfigure(self.rov_ctrl.rover_id, state = "hidden")
            self.ana_btn.configure(state = "disabled")
            self.heli_ctrl.deploy()
            self.vehicle = 1 
        
        elif self.vehicle:
            answer = libclient.create_request(dataUser.data.userid, "remove_helico", 0)
            if answer["result"] == "Heli removed":
                dataUser.data.helico = None
                self.heli_ctrl.kubind()
                self.Canvas.itemconfigure(self.heli_ctrl.wHP, state = "hidden")
                self.Canvas.itemconfigure(self.heli_ctrl.wenergy, state = "hidden")
                self.Canvas.itemconfigure(self.heli_ctrl.helico_id, state = "hidden")
                self.ana_btn.configure(state = "normal")
                self.rov_ctrl.spawn()
                self.vehicle = 0
                
            else:
                self.heli_ctrl.error()
        else:
            print("error")

    def placer_objet(self, type_obj, pos_serv):
        """Place un objet de type type_obj (1:rover, 2:helico, 3: rocher, 4: vent, 5: poussiere)"""
        if not self.vehicle:
            x_rov = dataUser.data.rover['pos'][0]
            y_rov = dataUser.data.rover['pos'][1]
        else:
            x_rov = dataUser.data.helico['pos'][0]
            y_rov = dataUser.data.helico['pos'][1]
        delta_x = pos_serv[0] - x_rov
        delta_y = pos_serv[1] - y_rov
        if (abs(delta_x) <= 30) and (abs(delta_y) <= 20) :  #On affiche que les objets qui devraient etre sur l'ecran, on ne s'embete pas a les afficher si ils n'y sont pas
            if type_obj == 1:
                img = self.rover
            elif type_obj == 2:
                img = self.drone
            elif type_obj == 3:
                img = self.rock
            elif type_obj == 4:
                img = self.wind
            elif type_obj == 5:
                img = self.sand
            else:
                raise Exception ("Wrong obj type")
            self.Canvas.create_image(960 + (80 * delta_x), 540 + (80 * delta_y), image=img, tags= "obj")

    def maj_objet(self):
        """Met a jour les objets a l'ecran"""
        self.data_update()
        self.Canvas.delete("obj")
        for o in dataUser.data.roverPos:
            if o != dataUser.data.rover['pos'] or ((o == dataUser.data.rover['pos']) and (self.vehicle)):
                self.placer_objet(1, o)
        
        for o in dataUser.data.helicoPos:

            if (dataUser.data.helico != "None"):
                if (o != dataUser.data.helico['pos']):
                    self.placer_objet(2, o)

        for o in dataUser.data.lootDict:
            self.placer_objet(3, o)

        #self.window.after(1000, self.maj_objet)         #1000 pour des tests, mettre 50 en utilisation normale
        self.window.after(50, self.maj_objet)

        #TODO: Meteo

    

if __name__ == "__main__":
    w = tk.Tk()
    w.resizable(width='false', height='false')
    w.geometry("1920x1080")
    A = MainGUI(w)
    w.mainloop()
