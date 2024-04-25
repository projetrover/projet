import tkinter as tk
from PIL import Image, ImageTk

MAP = "map.jpg"
rover = "drone.png"
im = Image.open(rover)
print (im.mode)

posx = 960
posy = 540
# Position of the image (global)

class mainGUI():

    def __init__(self, window, Imgmap, Imgrover):
        self.window = window
        self.Canvas = tk.Canvas(self.window, width=1920, height=1080, bg="black")
        self.rover = tk.PhotoImage(file = Imgrover)
        self.bg = ImageTk.PhotoImage(Image.open(Imgmap))
        self.bg_id = self.Canvas.create_image(posx, posy, image=self.bg)
        self.Canvas.create_image(960,540, image = self.rover)
        self.Canvas.pack()

    def move_left(self, event=None):
        global posx
        #if posx < 960:
        posx += 6
        self.Canvas.move(self.bg_id, 12, 0)

    def move_right(self, event=None):
        global posx
        #if posx > 960 - self.bg.width() + 1920:
        posx -= 6
        self.Canvas.move(self.bg_id, -12, 0)

    def move_up(self, event=None):
        global posy
        #if posy < 540:
        posy += 6
        self.Canvas.move(self.bg_id, 0, 12)

    def move_down(self, event=None):
        global posy
        #if posy > 540 - self.bg.height() + 1080:
        posy -= 6
        self.Canvas.move(self.bg_id, 0, -12)

    def kbind(self):
        self.window.bind("<Left>", self.move_left)
        self.window.bind("<Right>", self.move_right)
        self.window.bind("<Up>", self.move_up)
        self.window.bind("<Down>", self.move_down)

        # After bindings, the main loop needs to be started to capture the key events
        self.window.mainloop()


if __name__ == "__main__":
    w = tk.Tk()
    w.wm_attributes('-alpha', 0)
    w.resizable(width='false', height='false')
    w.geometry("1920x1080")
    A = mainGUI(w, MAP,rover)
    A.kbind()
