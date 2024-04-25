import tkinter as tk
from PIL import Image, ImageTk

MAP = "map.jpg"
rover = "rover.png"

left = 90
right = -90
up = 0
down = 180

class MainGUI:

    def __init__(self, window, imgmap, imgrover):
        self.vehicle_dir = 0
        self.window = window
        self.Canvas = tk.Canvas(self.window, width=1920, height=1080, bg="black")
        self.imgrover = Image.open(imgrover).resize((80, 80), Image.ANTIALIAS)
        self.rover = ImageTk.PhotoImage(self.imgrover)
        self.bg = ImageTk.PhotoImage(Image.open(imgmap))
        self.bg_id = self.Canvas.create_image(540, 960, image=self.bg)
        self.rover_object = self.Canvas.create_image(960, 540, image=self.rover)
        self.Canvas.pack()
    
    def rotate(self, direction):
        print("rotate", direction)
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

       

if __name__ == "__main__":
    w = tk.Tk()
    w.wm_attributes('-alpha', 0)
    w.resizable(width='false', height='false')
    w.geometry("1920x1080")
    A = MainGUI(w, MAP, rover)
    A.kbind()
    w.mainloop()
