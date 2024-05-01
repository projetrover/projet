import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from os.path import exists

left = 90
right = -90
up = 0
down = 180

def checkimg(image):
	"""Cherche l'image image et retourne son chemin, None si introuvable"""

	if exists("../../Images/"+image):
		return "../../Images/"+image
	elif exists("Images/"+image):
		return "Images/"+image
	return None

class MainGUI:

	def __init__(self, window):
		
		imgmap = checkimg("map.jpg")
		imgrover = checkimg("rover.png")

		self.vehicle_dir = 0
		self.window = window
		self.Canvas = tk.Canvas(self.window, width=1920, height=1080, bg="black")
		self.imgrover = Image.open(imgrover).resize((80, 80), Image.LANCZOS)
		self.rover = ImageTk.PhotoImage(self.imgrover)
		self.bg = ImageTk.PhotoImage(Image.open(imgmap))
		self.bg_id = self.Canvas.create_image(540, 960, image=self.bg)
		self.rover_object = self.Canvas.create_image(960, 540, image=self.rover)
		self.progressbar = None
		self.Canvas.pack()
	
	def rotate(self, direction):
		
		self.imgrover = self.imgrover.rotate(direction - self.vehicle_dir)
		self.rover = ImageTk.PhotoImage(self.imgrover)
		self.Canvas.itemconfig(self.rover_object, image=self.rover)
		self.vehicle_dir = direction
	
	def move_left(self, event=None):
		if self.vehicle_dir != left:
			self.rotate(left)
		self.Canvas.move(self.bg_id, 12, 0)

	def move_right(self, event=None):
		if self.vehicle_dir != right:
			self.rotate(right)
		self.Canvas.move(self.bg_id, -12, 0)

	def move_up(self, event=None):
		if self.vehicle_dir != up:
			self.rotate(up)
		self.Canvas.move(self.bg_id, 0, 12)

	def move_down(self, event=None):
		if self.vehicle_dir != down:
			self.rotate(down)
		self.Canvas.move(self.bg_id, 0, -12)

	def kbind(self):
		self.window.bind("<Left>", self.move_left)
		self.window.bind("<Right>", self.move_right)
		self.window.bind("<Up>", self.move_up)
		self.window.bind("<Down>", self.move_down)
		
	def progress_bar(self):
		#progress = tk.IntVar()
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
	A.progress_bar()
	w.mainloop()
