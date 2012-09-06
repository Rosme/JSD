#-*- coding: utf-8 -*-
'''
controlleur.py
Fichier contenant les classes controlleur du Redsquare
Projet par Jean-Sébastien Fauteux, Samuel Ryc et David Lebrun
'''

import modele
import vue

class Jeu():
    def __init__(self):
        self.carte = modele.Carte()
        self.niveau = self.carte.getNiveau()
        self.gc = modele.GerantCollision()
        self.started = False
        self.interface = vue.RenduInterface(self, self.niveau.getRouge(), self.niveau.getFormes())
    
    def run(self):
        self.interface.dessiner()
    
    def update(self):
        if self.started:
            if self.gc.collisionExterieur(self.niveau.getRouge().getBornes(), self.carte.getBornes()):
                self.interface.gameOver()
        
            for forme in self.niveau.getFormes():
                if self.gc.collisionForme(self.niveau.getRouge().getBornes(), forme.getBornes()):
                    self.interface.gameOver()
                forme.mouvement()
    
    def reset(self):
        self.carte = modele.Carte()
        self.niveau = self.carte.getNiveau()
        self.started = False
    
    def gameOn(self):
        self.started = True
    
if __name__ == '__main__':
    j = Jeu()
    j.run()
