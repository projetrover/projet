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

class MainGUI():
	'''Classe de l'interface principale'''

	def __init__(self, window):
		'''Initialise les attributs de l'interface: la fenêtre principale, le canvas, l'image de fond (carte), le rover et les autres sprites, la barre de progression et les jauges de "points de vie" et d'énergie.
		vehicle_dir est le sens vers lequel le rover est tourné, utilisé pour les rotations. Le rover est positionné au milieu de l'écran'''
		

		self.rov_ctrl = controleRoverGUI.ControleRoverGUI()
		self.heli_ctrl = controleHelicoGUI.ControleHelicoGUI()
		self.alertes = alerteGUI.AlerteGUI()
		self.minimap = miniCarteGUI.MiniCarteGUI()
		self.map = carteGUI.CarteGUI()

		imgmap = checkimg("map.jpg")
		imgrover = checkimg("rover.png")
		imgrocher = checkimg("rock.png")
		imgdrone = checkimg("drone.png")
		imgwind = checkimg("Wind_Storm.png")
		imgsand = checkimg("Sandstorm.png")
		
		styleHP = ttk.Style()
		styleHP.theme_use("alt")
		styleHP.configure("green.Horizontal.TProgressbar",background = "green2",troughcolor = "red",thickness = 40)
		styleEnergy = ttk.Style()
		styleEnergy.theme_use("alt")
		styleEnergy.configure("orange.Horizontal.TProgressbar",background = "gold", troughcolor = "black",thickness = 40)

		self.vehicle_dir = up
		self.window = window
		self.Canvas = tk.Canvas(self.window, width=1920, height=1080, bg="black")
		self.imgrover = Image.open(imgrover).resize((80, 80), Image.LANCZOS)
		
		self.rover = ImageTk.PhotoImage(self.imgrover)
		self.bg = ImageTk.PhotoImage(Image.open(imgmap))
		self.rock = ImageTk.PhotoImage(Image.open(imgrocher).resize((80, 80), Image.LANCZOS))
		self.drone = ImageTk.PhotoImage(Image.open(imgdrone).resize((80, 80), Image.LANCZOS))
		self.wind = ImageTk.PhotoImage(Image.open(imgwind).resize((80, 80), Image.LANCZOS))
		self.sand = ImageTk.PhotoImage(Image.open(imgsand).resize((80, 80), Image.LANCZOS))
		self.bg_id = self.Canvas.create_image(0, 0, image=self.bg, anchor = tk.NW)
		#self.Canvas.create_image(100, 100, image=self.rock)
		#self.Canvas.create_image(180, 100, image=self.drone)
		#self.Canvas.create_image(260, 100, image=self.wind)
		#self.Canvas.create_image(340, 100, image=self.sand)
		self.rover_id = self.Canvas.create_image(960, 540, image=self.rover)
		
		
		self.progressbar = None
		self.HP = ttk.Progressbar(self.window, orient = "horizontal", length = 300, mode = "determinate", value = 100,style = "green.Horizontal.TProgressbar")
		self.Canvas.create_window(1750,100,window = self.HP)
		self.Canvas.create_text(1750, 60, text="État du véhicule", font="bold 20", fill="black")
		self.energy = ttk.Progressbar(self.window, orient = "horizontal", length = 300, mode = "determinate", value = 100,style = "orange.Horizontal.TProgressbar")
		self.Canvas.create_window(1750,200,window = self.energy)
		self.Canvas.create_text(1750, 160, text="Énergie", font="bold 20", fill="black")
		self.Canvas.pack()
	
	def rotate(self, direction):
		'''Fait pivoter le rover de direction - self.vehicle_dir degrés'''
		
		self.imgrover = self.imgrover.rotate(direction - self.vehicle_dir)
		self.rover = ImageTk.PhotoImage(self.imgrover)
		self.Canvas.itemconfig(self.rover_id, image=self.rover)
		self.vehicle_dir = direction
	
	def move_left(self, event=None):
		'''Fait pivoter le rover si nécessaire et déplace la carte de 12 pixels vers la droite, donnant l'impression que le rover avance vers la gauche'''
		
		if self.vehicle_dir != left:
			self.rotate(left)
		#answer = libclient.create_request(dataUser.data.userid, 'move_rover', 3)  #A remplacer par controle_Rover.move()
		#if answer['result']['state'] == 'moved':
		#	self.Canvas.move(self.bg_id, 80, 0)
		#elif answer['result']['state'] == 'not moved':
		#	dataUser.data.rover['durability'] -= answer['result']['damage']
		#	self.decrease_HP(answer['result']['damage'])
		#dataUser.data.rover['battery'] -= answer['result']['battery_lost']
		#self.decrease_energy(answer['result']['battery_lost'])
		self.Canvas.move(self.bg_id, 80, 0)

	def move_right(self, event=None):
		'''Fait pivoter le rover si nécessaire et déplace la carte de 12 pixels vers la gauche, donnant l'impression que le rover avance vers la droite'''
		
		if self.vehicle_dir != right:
			self.rotate(right)
		# answer = libclient.create_request(dataUser.data.userid, 'move_rover', 3)  #A remplacer par controle_Rover.move()
		# if answer['result']['state'] == 'moved':
		# 	self.Canvas.move(self.bg_id, -80, 0)
		# elif answer['result']['state'] == 'not moved':
		# 	dataUser.data.rover['durability'] -= answer['result']['damage']
		# 	self.decrease_HP(answer['result']['damage'])
		# dataUser.data.rover['battery'] -= answer['result']['battery_lost']
		# self.decrease_energy(answer['result']['battery_lost'])
		self.Canvas.move(self.bg_id, -80, 0)

	def move_up(self, event=None):
		'''Fait pivoter le rover si nécessaire et déplace la carte de 12 pixels vers le bas, donnant l'impression que le rover avance vers le haut'''
		
		if self.vehicle_dir != up:
			self.rotate(up)
		# answer = libclient.create_request(dataUser.data.userid, 'move_rover', 3)  #A remplacer par controle_Rover.move()
		# if answer['result']['state'] == 'moved':
		# 	self.Canvas.move(self.bg_id, 0, 80)
		# elif answer['result']['state'] == 'not moved':
		# 	dataUser.data.rover['durability'] -= answer['result']['damage']
		# 	self.decrease_HP(answer['result']['damage'])
		# dataUser.data.rover['battery'] -= answer['result']['battery_lost']
		# self.decrease_energy(answer['result']['battery_lost'])
		self.Canvas.move(self.bg_id, 0, 80)
		

	def move_down(self, event=None):
		'''Fait pivoter le rover si nécessaire et déplace la carte de 12 pixels vers le haut, donnant l'impression que le rover avance vers le bas'''
	
		if self.vehicle_dir != down:
			self.rotate(down)
		# answer = libclient.create_request(dataUser.data.userid, 'move_rover', 3)  #A remplacer par controle_Rover.move()
		# if answer['result']['state'] == 'moved':
		# 	self.Canvas.move(self.bg_id, 0, -80)
		# elif answer['result']['state'] == 'not moved':
		# 	dataUser.data.rover['durability'] -= answer['result']['damage']
		# 	self.decrease_HP(answer['result']['damage'])
		# dataUser.data.rover['battery'] -= answer['result']['battery_lost']
		# self.decrease_energy(answer['result']['battery_lost'])
		self.Canvas.move(self.bg_id, 0, -80)
		

	def kbind(self):
		'''Associe chaque touche directionnelle du clavier à la méthode "move" correspondante'''
	
		self.window.bind("<Left>", self.move_left)
		self.window.bind("<Right>", self.move_right)
		self.window.bind("<Up>", self.move_up)
		self.window.bind("<Down>", self.move_down)
		
		
	def progress_bar(self):
		'''Créé une barre de progression au-dessus du rover et la supprime une fois remplie'''
		
		self.progressbar = ttk.Progressbar(self.window,orient = "horizontal",length = 70,mode = "determinate")
		self.Canvas.create_window(960,480,window = self.progressbar)
		self.progressbar.start(50)
		self.progressbar.after(5000,self.progressbar.destroy)
	
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
		self.Canvas.create_window(1750,100,window = self.HP)
			
	def decrease_energy(self,amount):
		'''Diminue la jauge d'énergie du rover'''
		
		if self.energy["value"]-amount>=0:
			self.energy.step(-amount)
		else: 
			self.energy.step(-self.energy["value"])
		
	def increase_energy(self,amount):
		'''Augmente la jauge d'énergie du rover'''
		
		self.energy.step(amount)
	
	

if __name__ == "__main__":
	w = tk.Tk()
	w.resizable(width='false', height='false')
	w.geometry("1920x1080")
	A = MainGUI(w)
	A.kbind()
	w.mainloop()
