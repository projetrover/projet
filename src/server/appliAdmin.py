import usersGUI
import mapGUI
import recieved_data
import tkinter as tk
from PIL import Image, ImageTk

CARTE_MARS = "../../Images/mercat.jpg"

class AppliAdmin:
	def __init__(self, Window):
		self.window = Window
		self.mapImg = ImageTk.PhotoImage( Image.open(CARTE_MARS) )
		self.canva = tk.Canvas(self.window, width= 1920, height = 1080)
		self.canva.create_image(-800,-800,image = self.mapImg, anchor="nw")
		self.canva.pack()
		

if __name__ == "__main__":
	root = tk.Tk()
	root.geometry("1920x1080")
	A = AppliAdmin(root)
	root.mainloop()

