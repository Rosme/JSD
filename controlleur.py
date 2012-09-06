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
        self.carte = modele.Carte()
        self.niveau = self.carte.getNiveau()
        self.gc = modele.GerantCollision()
        self.interface = vue.RenduInterface(self, self.niveau.getRouge(), self.niveau.getFormes())
    
    def run(self):
        self.interface.dessiner()
    
    def update(self):
        if self.gc.collisionExterieur(self.niveau.getRouge().getBornes(), self.carte.getBornes()):
            self.interface.gameOver()
        
        for forme in self.niveau.getFormes():
            if self.gc.collisionForme(self.niveau.getRouge().getBornes(), forme.getBornes()):
                self.interface.gameOver()
            forme.mouvement()
        
        
        self.interface.root.after(20, self.update)
    
    def reset(self):
        self.carte = modele.Carte()
        self.niveau = self.carte.getNiveau()
    
if __name__ == '__main__':
    j = Jeu()
    j.run()
