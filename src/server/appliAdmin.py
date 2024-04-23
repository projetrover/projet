import server as serv
import tkinter as tk
from PIL import Image, ImageTk

CARTE_MARS = "../../Images/map.jpg"

class AppliAdmin:
	def __init__(self, Window, userF, vehicleF):
		self.window = Window

		self.userF = userF
		self.vehicleF = vehicleF

		self.main_frame = tk.Frame(self.window)

		self.mapImg = ImageTk.PhotoImage( Image.open(CARTE_MARS) )
		self.canva = tk.Canvas(self.window, width= 1920, height = 1080)
		self.canva.create_image(-800,-800,image = self.mapImg, anchor="nw")
		self.main_frame.pack(side=tk.BOTTOM,expand=1)
		self.canva.pack()

		self.sb = tk.Scrollbar(root,orient='vertical',command=self.canva.yview)
		self.sb.pack(side='right',fill=tk.Y)

		self.canva.config(yscrollcommand = self.sb.set)

	def UsersGUI(self):
		self.userF = userF
		self.vehicleF = vehicleF
		self.sb = tk.Scrollbar(root,orient='vertical',command=self.canva.yview)
		self.sb.pack(side='right',fill=tk.Y)

'''
s = serv.Server()
root = tk.Tk()
root.geometry("1920x1080")
A = AppliAdmin(root, s.userF, s.vehicleF)
root.mainloop()
'''
