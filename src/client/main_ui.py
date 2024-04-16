import tkinter as tk
import login_screen

MAP = "mercat.png"

def move_image(canvas,img,x,y):
	Canv.create_image(960+i,540+y,image = bg)

w=tk.Tk()

w.wm_attributes('-alpha', 0)	
w.resizable(width='false',height='false')
w.geometry("1920x1080")
Canv = tk.Canvas(w,width=1920,height=1080,bg="white")
bg = tk.PhotoImage(file = MAP)
Canv.create_image(960,540,image = bg)

for i in range(500):
	Canv.create_image(960-i,540,image = bg)

	
b = tk.Button(w,text = "move",command=lambda:move_image(Canv,bg,1,0),relief="groove")
Canv.create_window(960,620,window = b)

Canv.pack()

tk.mainloop()	
