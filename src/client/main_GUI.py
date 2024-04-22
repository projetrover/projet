import tkinter as tk
import authentificationGUI

MAP = "mercat.png"

posx = 960
posy = 540
#position de l'image (globale)

def move_left(canvas,bg):
	global posx
	global posy
	posx += 100
	canvas.create_image(posx,posy,image = bg)
	
def move_right(canvas,bg):
	global posx
	global posy
	posx -= 100
	canvas.create_image(posx,posy,image = bg)

def move_up(canvas,bg):
	global posx
	global posy
	posy += 100
	canvas.create_image(posx,posy,image = bg)

def move_down(canvas,bg):
	global posx
	global posy
	posy -= 100
	canvas.create_image(posx,posy,image = bg)

w=tk.Tk()

w.wm_attributes('-alpha', 0)	
w.resizable(width='false',height='false')
w.geometry("1920x1080")
Canv = tk.Canvas(w,width=1920,height=1080,bg="white")
bg = tk.PhotoImage(file = MAP)
Canv.create_image(960,540,image = bg)


	
b = tk.Button(w,text = "left",command=lambda:move_left(Canv,bg),relief="groove")
Canv.create_window(920,540,window = b)
b = tk.Button(w,text = "right",command=lambda:move_right(Canv,bg),relief="groove")
Canv.create_window(1000,540,window = b)
b = tk.Button(w,text = "up",command=lambda:move_up(Canv,bg),relief="groove")
Canv.create_window(960,500,window = b)
b = tk.Button(w,text = "down",command=lambda:move_down(Canv,bg),relief="groove")
Canv.create_window(960,580,window = b)

Canv.pack()

tk.mainloop()	
