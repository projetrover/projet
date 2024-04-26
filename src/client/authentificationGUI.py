import authentification as aut
import tkinter as tk
from os.path import exists


#IMAGE_MARS = "Mars-blog-header.png"

class AuthentificationGUI(aut.Authentification):
	
	
	def __init__(self,window):
		file_exists = exists("../../Images/Mars-blog-header.png")
		if file_exists:
			Img = "../../Images/Mars-blog-header.png"
		else:
			Img = "Images/Mars-blog-header.png"

		aut.Authentification.__init__(self)

		self.window = window
		self.Canvas = tk.Canvas(self.window,width=1920,height=1080,bg="white")
		self.bg = tk.PhotoImage(file = Img)
		self.Canvas.create_image(960,540,image = self.bg)
		self.Canvas.create_text(960, 100, text="EXPLOVER", font="impact 80 italic", fill="black")
		self.Canvas.create_text(960, 460, text="Nom d'utilisateur: ", font="calibri 10", fill="black")
		
		self.entry1 = tk.Entry(self.window)
		self.Canvas.create_window(960,500,window=self.entry1)
		self.Canvas.create_text(960, 540, text="Mot de passe: ", font="calibri 10", fill="black")

		self.entry2 = tk.Entry(self.window,show = "•")
		self.Canvas.create_window(960,580,window=self.entry2)
		self.button = tk.Button(self.window,text = "Connexion",command = self.login_btn ,relief="groove")
		self.Canvas.create_window(960,620,window = self.button)
		self.Canvas.pack()	
			
	
		
	def error_wrong_password(self):
		"""Affiche message d'erreur quand mauvais login"""
		self.Canvas.create_text(960, 660, text = "Nom d'utilisateur ou mot de passe incorrect", font = "calibri 10 bold", fill = "red")
		self.Canvas.pack()
		
	def setcommand(self):
		"""Test"""
		print("action provisoire")
	
	def login_btn(self):
		"""Methode appelee quand on clique sur le bouton connexion, affiche le message d'erreur si erreur, sinon clear le canvas
			pour passer au prochain ecran"""
		username = self.entry1.get()
		password = self.entry2.get()
		self.login(username, password)
		if not self.state.get() :
			self.error_wrong_password()
		else:

			self.Canvas.pack_forget()
		
		
if __name__ == "__main__":
	
	w=tk.Tk()
	#w.wm_attributes('-alpha', 0)	
	w.resizable(width='false',height='false')
	w.geometry("1920x1080")
	A = AuthentificationGUI(w)
	tk.mainloop()	
