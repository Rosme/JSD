from tkinter import *

class RenduCarte():

    def __init__(self):
        return None                 ###
    
    def afficherFormes(self):
        return None                 ###
    
    def dessinerPanel(self):
        frame = Frame(width=400, height=400, colormap="new")
        frame.pack() 
    
    def afficherCarte(self):
        fenetre = Tk()
        rc.dessinerPanel()
        fenetre.mainloop()
        
class RenduInterface():
    
    def __init__(self):
        return None                 ###
    
    def afficherBouton(self):
        return None
    
    def afficherInfo(self):
        return None


if __name__ == '__main__':          #pour tester main
    rc = RenduCarte()
    rc.afficherCarte()
