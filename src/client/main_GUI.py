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
        '''Initialise les attributs de l'interface: la fenêtre principale, le canvas, l'image de fond (carte), le rover et les autres sprites, la barre de progression et les jauges de "points de vie" et d'énergie.
        vehicle_dir est le sens vers lequel le rover est tourné, utilisé pour les rotations. Le rover est positionné au milieu de l'écran'''
    
        imgmap = checkimg("map.jpg")
        imgrocher = checkimg("rock.png")
        imgdrone = checkimg("drone.png")
        imgwind = checkimg("Wind_Storm.png")
        imgsand = checkimg("Sandstorm.png")
        
        

        
        self.window = window
        self.Canvas = tk.Canvas(self.window, width=1920, height=1080, bg="black")
        
        
        
        self.bg = ImageTk.PhotoImage(Image.open(imgmap))
        self.rock = ImageTk.PhotoImage(Image.open(imgrocher).resize((80, 80), Image.LANCZOS))
        self.drone = ImageTk.PhotoImage(Image.open(imgdrone).resize((80, 80), Image.LANCZOS))
        self.wind = ImageTk.PhotoImage(Image.open(imgwind).resize((80, 80), Image.LANCZOS))
        self.sand = ImageTk.PhotoImage(Image.open(imgsand).resize((80, 80), Image.LANCZOS))
        print(920 - (dataUser.data.rover['pos'][0] * 80), 500 - (dataUser.data.rover['pos'][1] * 80))
        self.bg_id = self.Canvas.create_image(920 - (dataUser.data.rover['pos'][0] * 80), 500 - (dataUser.data.rover['pos'][1] * 80), image=self.bg, anchor = tk.NW)
        #self.Canvas.create_image(100, 100, image=self.rock)
        #self.Canvas.create_image(180, 100, image=self.drone)
        #self.Canvas.create_image(260, 100, image=self.wind)
        #self.Canvas.create_image(340, 100, image=self.sand)
         
        self.progressbar = None
        self.Canvas.pack()

        self.rov_ctrl = controleRoverGUI.ControleRoverGUI(self.window ,self.Canvas, self.bg_id)         #Sous classes
        self.rov_ctrl.kbind()
        self.heli_ctrl = controleHelicoGUI.ControleHelicoGUI()
        self.alertes = alerteGUI.AlerteGUI()
        self.minimap = miniCarteGUI.MiniCarteGUI()
        self.carte = carteGUI.CarteGUI()

        
    def progress_bar(self):
        '''Créé une barre de progression au-dessus du rover et la supprime une fois remplie'''
        
        self.progressbar = ttk.Progressbar(self.window,orient = "horizontal",length = 70,mode = "determinate")
        self.Canvas.create_window(960,480,window = self.progressbar)
        self.progressbar.start(50)
        self.progressbar.after(5000,self.progressbar.destroy)
    
    
    
    

if __name__ == "__main__":
    w = tk.Tk()
    w.resizable(width='false', height='false')
    w.geometry("1920x1080")
    A = MainGUI(w)
    w.mainloop()
