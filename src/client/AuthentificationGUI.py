import tkinter as tk



IMAGE_MARS = "Mars-header-blog.png"


class AuthentificationGUI:
	
	
	def __init__(self,window,Img):
		
		self.window = window
		self.Canvas = tk.Canvas(self.window,width=1920,height=1080,bg="white")
		self.bg = tk.PhotoImage(file = Img)
		self.Canvas.create_image(500,500,image = self.bg)
		#self.Frame = tk.Frame(self.Canvas,width = 700, height = 500)
		self.label1 = tk.Label(self.Canvas,text = "Nom d'utilisateur: ",width = 20, height = 5)
		self.entry1 = tk.Entry(self.window)
		self.Canvas.create_window(960,500,window=self.entry1)
		self.label2 = tk.Label(self.Canvas,text = "Mot de passe: ",width = 20, height = 5)
		self.entry2 = tk.Entry(self.window)
		self.Canvas.create_window(960,580,window=self.entry2)
		#self.Frame.pack(side = "top")
		
		#self.label1.pack()
		#self.label2.pack()
		self.Canvas.pack()		
		
if __name__ == "__main__":
	w=tk.Tk()
	w.wm_attributes('-alpha', 0)	
	w.resizable(width='false',height='false')
	w.geometry("1920x1080")
	A = Authentification(w,IMAGE_MARS)
	tk.mainloop()	
