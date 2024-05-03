import alerteGUI
import carteGUI
import miniCarteGUI
import controleHelicoGUI
import controleRoverGUI
import authentificationGUI
import dataUser
import main_GUI
import tkinter as tk
import libclient



#TODO: TOUT
class AppliUser:
    def __init__(self, window):
        self.auth = None
        self.data = dataUser.data
        self.window = window
        self.gui = None

    def data_update(self):
        answer = libclient.create_request(dataUser.data.userid, "data_update", 0)
        #TODO: toute la methode

    def main(self):
        self.auth = authentificationGUI.AuthentificationGUI(self.window)
        self.window.wait_variable(self.auth.state)
        self.gui = main_GUI.MainGUI(self.window)
        self.gui.kbind()
        #self.gui.rov_ctrl.analyse(0)
        #self.gui.rov_ctrl.analyse(1)



    
