########################################
#AUTEUR: David, Samuel, Jean-Sebastien
#TITRE: REDSQUARE
#DATE DE REMISE: 30 AOUT 2012
########################################

from tkinter import *

class RenduCarte():

    def __init__(self, parent = None):
        return None
        
    def affichePanel(self):
        frame = Frame(width=400, height=400, colormap="new")
        frame.pack() 
    
    def afficheJeux(self):
        fenetre = Tk()
        rc.affichePanel()
        fenetre.mainloop()
         

if __name__ == '__main__':
    rc = RenduCarte()
    rc.afficheJeux()
    