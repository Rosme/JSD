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
        self.interface = vue.RenduInterface(self, self.niveau)
        self.temps = modele.Temps()
    
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
                
            if self.temps.getTemps() > 5.0:
                self.niveau.boost()
                self.temps.restart()
    
    def reset(self):
        self.carte = modele.Carte()
        self.niveau = self.carte.getNiveau()
        self.started = False
        self.temps.stop()
    
    def gameOn(self):
        self.started = True
        self.temps.start()
    
if __name__ == '__main__':
    j = Jeu()
    j.run()
