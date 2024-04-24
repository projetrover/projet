import tkinter as tk
#import authentificationGUI

MAP = "mercat.png"

posx = 960
posy = 540
#position de l'image (globale)

class mainGUI():

	def __init__(self,window,Img):
	
		self.window = window
		self.Canvas = tk.Canvas(self.window,width=1920,height=1080,bg="white")
		self.bg = tk.PhotoImage(file = Img)
		self.Canvas.create_image(960,540,image = self.bg)
		self.Canvas.pack()	
		
	
	def move_left(canvas,bg):
		print("move_left")
		global posx
		global posy
		posx += 12
		canvas.create_image(posx,posy,image = bg)
	
	
	def move_right(self):
		print("move_right")
		global posx
		global posy
		posx -= 12
		canvas.create_image(posx,posy,image = bg)

	def move_up(self):
		print("move_up")
		global posx
		global posy
		posy += 12
		canvas.create_image(posx,posy,image = bg)

	def move_down(self):
		print("move_down")
		global posx
		global posy
		posy -= 12
		canvas.create_image(posx,posy,image = bg)

if __name__ == "__main.py__":


	w=tk.Tk()
	w.wm_attributes('-alpha', 0)	
	w.resizable(width='false',height='false')
	w.geometry("1920x1080")
	A = mainGUI(w,"mercat.png")
	tk.mainloop()	
