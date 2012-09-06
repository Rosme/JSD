'''
controlleur.py
Fichier contenant les classes controlleur du Redsquare
Projet par Jean-Sebastien Fauteux, Samuel Ryc et David Lebrun
'''
##-*- coding: ISO-8859-1 -*-

import modele
import vue

class Jeu():
    def __init__(self):
        self.interface = vue.RenduInterface(self)
        self.interface.setData(self.rouge, self.forme)
    
    def run(self):
        self.interface.dessiner()
        
    
if __name__ == '__main__':
    j = Jeu()
    j.run()
