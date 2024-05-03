import alerteGUI
import carteGUI
import miniCarteGUI
import controleHelicoGUI
import controleRoverGUI
import authentificationGUI
import dataUser
import main_GUI
import tkinter as tk



#TODO: TOUT
class AppliUser:
    def __init__(self, window):
        self.auth = None
        self.data = dataUser.data
        self.window = window
        self.gui = None

    def main(self):
        self.auth = authentificationGUI.AuthentificationGUI(self.window)
        self.window.wait_variable(self.auth.state)
        self.gui = main_GUI.MainGUI(self.window)
        self.gui.kbind()


    
