import tkinter as tk
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

class MainGUI:
	'''Classe de l'interface principale'''

	def __init__(self, window):
		'''Initialise les attributs de l'interface: la fenêtre principale, le canvas, l'image de fond (carte), le rover, la barre de progression.
		vehicle_dir est le sens vers lequel le rover est tourné, utilisé pour les rotations. Le rover est positionné au milieu de l'écran'''
		

		imgmap = checkimg("map.jpg")
		imgrover = checkimg("rover.png")

		self.vehicle_dir = up
		self.window = window
		self.Canvas = tk.Canvas(self.window, width=1920, height=1080, bg="black")
		self.imgrover = Image.open(imgrover).resize((80, 80), Image.LANCZOS)
		self.rover = ImageTk.PhotoImage(self.imgrover)
		self.bg = ImageTk.PhotoImage(Image.open(imgmap))
		self.bg_id = self.Canvas.create_image(540, 960, image=self.bg)
		self.rover_id = self.Canvas.create_image(960, 540, image=self.rover)
		self.progressbar = None
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
		self.Canvas.move(self.bg_id, 12, 0)

	def move_right(self, event=None):
		'''Fait pivoter le rover si nécessaire et déplace la carte de 12 pixels vers la gauche, donnant l'impression que le rover avance vers la droite'''
		
		if self.vehicle_dir != right:
			self.rotate(right)
		self.Canvas.move(self.bg_id, -12, 0)

	def move_up(self, event=None):
		'''Fait pivoter le rover si nécessaire et déplace la carte de 12 pixels vers le bas, donnant l'impression que le rover avance vers le haut'''
		
		if self.vehicle_dir != up:
			self.rotate(up)
		self.Canvas.move(self.bg_id, 0, 12)

	def move_down(self, event=None):
		'''Fait pivoter le rover si nécessaire et déplace la carte de 12 pixels vers le haut, donnant l'impression que le rover avance vers le bas'''
	
		if self.vehicle_dir != down:
			self.rotate(down)
		self.Canvas.move(self.bg_id, 0, -12)

	def kbind(self):
		'''associe chaque touche directionnelle du clavier à la méthode "move" correspondante'''
	
		self.window.bind("<Left>", self.move_left)
		self.window.bind("<Right>", self.move_right)
		self.window.bind("<Up>", self.move_up)
		self.window.bind("<Down>", self.move_down)
		
	def progress_bar(self):
		'''créé une barre de progression au-dessus du rover et la supprime une fois remplie'''
		
		self.progressbar = ttk.Progressbar(self.window,orient = "horizontal",length = 70,mode = "determinate")
		self.Canvas.create_window(960,480,window = self.progressbar)
		self.progressbar.start(50)
		self.progressbar.after(5000,self.progressbar.destroy)
	
	

if __name__ == "__main__":
	w = tk.Tk()
	#w.wm_attributes('-alpha', 0)
	w.resizable(width='false', height='false')
	w.geometry("1920x1080")
	A = MainGUI(w)
	A.kbind()
	w.mainloop()
