import alerteGUI
import carteGUI
import miniCarteGUI
import controleHelicoGUI
import controleRoverGUI
import authentificationGUI
import dataUser
import tkinter as tk



#TODO: TOUT
class AppliUser:
    def __init__(self, window):
        self.auth = None
        self.data = None
        self.window = window

    def main(self):
        self.auth = authentificationGUI.AuthentificationGUI(self.window)
        self.window.wait_variable(self.auth.state)
        print("oui")

    
