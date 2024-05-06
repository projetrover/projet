import controleRover
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from os.path import exists
import dataUser
import libclient


left = 90
right = -90
up = 0
down = 180

def checkimg(image):
    '''Cherche l'image image et retourne son chemin, None si introuvable'''

    if exists("../../Images/"+image):
        return "../../Images/"+image
    elif exists("Images/"+image):
        return "Images/"+image
    return None


class ControleRoverGUI(controleRover.ControleRover):
    """Classe contenant tous les elements graphiques concernant le rover ainsi que les methodes qui vont avec"""
    def __init__(self, window,  Canvas, bg_id):
    
   
        controleRover.ControleRover.__init__(self)
        
        self.name = "rover"
        self.Canvas = Canvas
        self.window = window
        self.bg_id = bg_id

        imgrover = checkimg("rover.png")
        self.imgrover = Image.open(imgrover).resize((80, 80), Image.LANCZOS)
        self.rover = ImageTk.PhotoImage(self.imgrover)
        self.rover_id = self.Canvas.create_image(960, 540, image=self.rover)

        self.vehicle_dir = up

        styleHP = ttk.Style()
        styleHP.theme_use("alt")
        styleHP.configure("green.Horizontal.TProgressbar",background = "green2",troughcolor = "red",thickness = 40)
        styleEnergy = ttk.Style()
        styleEnergy.theme_use("alt")
        styleEnergy.configure("orange.Horizontal.TProgressbar",background = "gold", troughcolor = "black",thickness = 40)

        self.HP = ttk.Progressbar(self.window, orient = "horizontal", length = 300, mode = "determinate", value = 100,style = "green.Horizontal.TProgressbar")
        self.wHP = self.Canvas.create_window(1750,100,window = self.HP)
        self.Canvas.create_text(1750, 60, text="État du véhicule", font="bold 20", fill="black")
        self.energy = ttk.Progressbar(self.window, orient = "horizontal", length = 300, mode = "determinate", value = 100,style = "orange.Horizontal.TProgressbar")
        self.wenergy = self.Canvas.create_window(1750,200,window = self.energy)
        self.Canvas.create_text(1750, 160, text="Énergie", font="bold 20", fill="black")
        
        self.err_msg = None
        self.progressbar = None
        self.wprogressbar = None
        self.ana_msg = None
        self.anacheck = tk.BooleanVar()
    
    
    def rm_progressbar(self):
        """Enleve la barre de progression"""
        self.Canvas.delete(self.wprogressbar)
        self.progressbar.destroy()
        self.anacheck.set(not self.anacheck.get())


    def progress_bar(self):
        '''Créé une barre de progression au-dessus du rover et la supprime une fois remplie'''
        
        self.progressbar = ttk.Progressbar(self.window,orient = "horizontal",length = 70,mode = "determinate")
        self.wprogressbar = self.Canvas.create_window(960,480,window = self.progressbar)
        self.progressbar.start(50)
        self.progressbar.after(5000, self.rm_progressbar)
        

        
    

    def spawn(self):
        '''Fait reapparaitre le rover'''
        
        self.Canvas.itemconfigure(self.rover_id, state = "normal")
        self.kbind()
        self.Canvas.itemconfigure(self.wHP, state = "normal")
        self.Canvas.itemconfigure(self.wenergy, state = "normal")
        
        
    def teleport_rover(self, pos):
        '''Teleporte le rover a ses coordonnees serveur (utile quand on fait le tour de la map vu qu'elle est ronde)'''
        x = 920 - (pos[0] * 80)
        y = 500 - (pos[1] * 80)
        self.Canvas.moveto(self.bg_id, x, y)

    def decrease_HP(self,amount):
        '''Diminue la jauge de points de vie du rover'''
        
        if self.HP["value"]-amount>=0:
            self.HP.step(-amount)
        else:
            self.HP.step(-self.HP["value"])
    
    def refill_HP(self):
        '''Réinitialise la "barre de vie" du rover'''
        
        self.HP.destroy()
        self.HP = ttk.Progressbar(self.window, orient = "horizontal", length = 300, mode = "determinate", value = 100,style = "green.Horizontal.TProgressbar")
        self.wHP = self.Canvas.create_window(1750,100,window = self.HP)
            
    def decrease_energy(self,amount):
        '''Diminue la jauge d'énergie du rover'''
        
        if self.energy["value"]-amount>=0:
            self.energy.step(-amount)
        else: 
            self.energy.step(-self.energy["value"])
        
    def increase_energy(self,amount):
        '''Augmente la jauge d'énergie du rover'''
        
        self.energy.step(amount)

    def rotate(self, direction):
        '''Fait pivoter le rover de direction - self.vehicle_dir degrés'''
        
        self.imgrover = self.imgrover.rotate(direction - self.vehicle_dir)
        self.rover = ImageTk.PhotoImage(self.imgrover)
        self.Canvas.itemconfig(self.rover_id, image=self.rover)
        self.vehicle_dir = direction
    
    def move(self, dir, event=None):
        '''Fait pivoter le rover si nécessaire et déplace la carte de 12 pixels vers la droite, donnant l'impression que le rover avance vers la gauche'''

        answer = self.movereq(dir)  
        if answer['result']['state'] == 'moved':
            npos = answer['result']['pos']
            opos_x = dataUser.data.rover['pos'][0]
            opos_y = dataUser.data.rover['pos'][1]

            if (npos == (opos_x - 1, opos_y)):          #LEFT
                for i in range(4):
                    self.Canvas.move(self.bg_id, 20, 0)
                    self.window.after(250)
            elif (npos == (opos_x + 1, opos_y)):        #RIGHT
                for i in range(4):
                    self.Canvas.move(self.bg_id, -20, 0)
                    self.window.after(250)
            elif (npos == (opos_x, opos_y - 1)):        #UP
                for i in range(4):
                    self.Canvas.move(self.bg_id, 0, 20)
                    self.window.after(250)
            elif (npos == (opos_x, opos_y + 1)):        #DOWN
                for i in range(4):
                    self.Canvas.move(self.bg_id, 0, -20)
                    self.window.after(250)
            else :
                self.teleport_rover(npos)

            dataUser.data.rover['pos'] = npos
        elif answer['result']['state'] == 'not moved':
            dataUser.data.rover['durability'] -= answer['result']['damage']
            self.decrease_HP(answer['result']['damage'])
        dataUser.data.rover['battery'] -= answer['result']['battery_lost']
        self.decrease_energy(answer['result']['battery_lost'])

    def move_up(self, event=None):
        """Methode appelee avec le bind pour se deplacer vers le haut"""
        if self.vehicle_dir != up:
            self.rotate(up)
        self.move(0)

    def move_right(self, event=None):
        """Methode appelee avec le bind pour se deplacer vers le bas"""
        print("rover right")
        if self.vehicle_dir != right:
            self.rotate(right)
        self.move(1)

    def move_down(self, event=None):
        """Methode appelee avec le bind pour se deplacer vers la gauche"""
        if self.vehicle_dir != down:
            self.rotate(down)
        self.move(2)

    def move_left(self, event=None):
        """Methode appelee avec le bind pour se deplacer vers la droite"""
        if self.vehicle_dir != left:
            self.rotate(left)
        self.move(3)
    
    def rm_error(self):
        """Retire le message d'erreur"""
        self.Canvas.delete(self.msg_err)
        
    def rm_ana(self):
        """Enleve le message d'analyse"""
        self.Canvas.delete(self.ana_msg)
    
    def analyse(self):
        """Methode appelee avec le bouton pour analyser un rocher"""
        answer = self.analysereq()["result"]
        if answer["state"] == "failed":
            self.msg_err = self.Canvas.create_text(960, 800,text = "Le rover doit etre devant un rocher et bien oriente pour detruire le rocher\n et analyser les composants", font = "10", fill = "red")
            self.window.after(3000, self.rm_error)
        else:
            self.progress_bar()
            self.window.wait_variable(self.anacheck)
            self.ana_msg = self.Canvas.create_text(960, 800, text = ("Vous venez d'analyser : " + answer['material']), font = "25", fill = "black")
            self.window.after(2000, self.rm_ana)

            

    def kbind(self):
        '''Associe chaque fleche directionnelle du clavier à la méthode "move" correspondante'''
    
        self.window.bind("<Left>", self.move_left)
        self.window.bind("<Right>", self.move_right)
        self.window.bind("<Up>", self.move_up)
        self.window.bind("<Down>", self.move_down)
        
    def kubind(self):
        '''Dissocie chaque fleche directionnelle du clavier de la méthode "move" correspondante'''
    
        self.window.unbind("<Left>")
        self.window.unbind("<Right>")
        self.window.unbind("<Up>")
        self.window.unbind("<Down>")
        

    
