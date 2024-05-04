import controleHelico
from tkinter import ttk
from PIL import Image, ImageTk
from os.path import exists


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
    
   
class ControleHelicoGUI(controleHelico.ControleHelico):
    
     def __init__(self, window,  Canvas, bg_id):
     
        controleHelico.ControleHelico.__init__(self)
        
        self.name = "helico"
        self.Canvas = Canvas
        self.window = window
        self.bg_id = bg_id

        imgrdrone = checkimg("drone.png")
        self.imghelico = Image.open(imghelico).resize((80, 80), Image.LANCZOS)
        self.helico = ImageTk.PhotoImage(self.imghelico)
        self.helico_id = None

        self.vehicle_dir = up

        styleHP = ttk.Style()
        styleHP.theme_use("alt")
        styleHP.configure("green.Horizontal.TProgressbar",background = "green2",troughcolor = "red",thickness = 40)
        styleEnergy = ttk.Style()
        styleEnergy.theme_use("alt")
        styleEnergy.configure("orange.Horizontal.TProgressbar",background = "gold", troughcolor = "black",thickness = 40)

        self.HP = ttk.Progressbar(self.window, orient = "horizontal", length = 300, mode = "determinate", value = 100,style = "green.Horizontal.TProgressbar")
        self.Canvas.create_window(1750,100,window = self.HP)
        self.Canvas.create_text(1750, 60, text="État du véhicule", font="bold 20", fill="black")
        self.energy = ttk.Progressbar(self.window, orient = "horizontal", length = 300, mode = "determinate", value = 100,style = "orange.Horizontal.TProgressbar")
        self.Canvas.create_window(1750,200,window = self.energy)
        self.Canvas.create_text(1750, 160, text="Énergie", font="bold 20", fill="black")
    
    
    def deploy(self):
    	'''Fait apparaitre l'helicoptere'''
    
    	self.helico_id = self.Canvas.create_image(960, 540, image=self.helico)
    	self.kbind()
    
    
    def ranger(self):
    	'''
    	
    def teleport_helico(self, pos):
        '''Teleporte l'helicoptere a ses coordonnees serveur (utile quand on fait le tour de la map vu qu'elle est ronde)'''
        x = 920 - (pos[0] * 80)
        y = 500 - (pos[1] * 80)
        self.Canvas.moveto(self.bg_id, x, y)

    def decrease_HP(self,amount):
        '''Diminue les points de vie de l'helicoptere'''
        
        if self.HP["value"]-amount>=0:
            self.HP.step(-amount)
        else:
            self.HP.step(-self.HP["value"])
    
    def refill_HP(self):
        '''Réinitialise les points de vie de l'hélicoptere'''
        
        self.HP.destroy()
        self.HP = ttk.Progressbar(self.window, orient = "horizontal", length = 300, mode = "determinate", value = 100,style = "green.Horizontal.TProgressbar")
        self.Canvas.create_window(1750,100,window = self.HP)
            
    def decrease_energy(self,amount):
        '''Diminue la jauge d'energie de l'helicoptere'''
        
        if self.energy["value"]-amount>=0:
            self.energy.step(-amount)
        else: 
            self.energy.step(-self.energy["value"])
        
    def increase_energy(self,amount):
        '''Augmente la jauge d'énergie de l'helicoptere'''
        
        self.energy.step(amount)

    def rotate(self, direction):
        '''Fait pivoter l'helicoptere de direction - self.vehicle_dir degres'''
        
        self.imghelico = self.imghelico.rotate(direction - self.vehicle_dir)
        self.helico = ImageTk.PhotoImage(self.imghelico)
        self.Canvas.itemconfig(self.helico_id, image=self.helico)
        self.vehicle_dir = direction
    
    def move(self, dir, event=None):
        '''Fait pivoter l'helicoptere si necessaire et deplace la carte de 12 pixels vers la droite, donnant l'impression que l'helicoptere avance vers la gauche'''

        answer = libclient.create_request(dataUser.data.userid, 'move_helico', dir)  #A remplacer par controle_Helico.move()
        if answer['result']['state'] == 'moved':
            npos = answer['result']['pos']
            opos_x = dataUser.data.helico['pos'][0]
            opos_y = dataUser.data.helico['pos'][1]

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
                self.teleport_helico(npos)

            dataUser.data.helico['pos'] = npos
        elif answer['result']['state'] == 'not moved':
            dataUser.data.helico['durability'] -= answer['result']['damage']
            self.decrease_HP(answer['result']['damage'])
        dataUser.data.helico['battery'] -= answer['result']['battery_lost']
        self.decrease_energy(answer['result']['battery_lost'])

    def move_up(self, event=None):
        if self.vehicle_dir != up:
            self.rotate(up)
        self.move(0)

    def move_right(self, event=None):
        if self.vehicle_dir != right:
            self.rotate(right)
        self.move(3)

    def move_down(self, event=None):
        if self.vehicle_dir != down:
            self.rotate(down)
        self.move(2)

    def move_left(self, event=None):
        if self.vehicle_dir != left:
            self.rotate(left)
        self.move(1)
        

    def kbind(self):
        '''Associe chaque fleche directionnelle du clavier à la methode "move" correspondante'''
    
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
