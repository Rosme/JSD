'''
modele.py
Fichier contenant les classes modeles du RedSquare
Projet par Jean-Sebastien Fauteux, Samuel Ryc et David Lebrun
'''

import time
import datetime

class Bornes():
    def __init__(self, x, y, longueur, hauteur):
        self.x = x
        self.y = y
        self.longueur = longueur
        self.hauteur = hauteur
        
class Formes():
    def __init__(self):
        None
        
    def getBornes(self):
        None
        
    def getCouleur(self):
        None
        
    def update(self):
        None
        
    def mouvement(self):
        None
        
class RedSquare():
    def __init__(self):
        self.bornesRS = Bornes(50, 50, 20, 20)        
        
    def getBornes(self):
        #self.bornesRS = Bornes(x, y, longueur, hauteur) #RS pour RedSquare (abreviation)
        return self.bornesRS
        
        
    def deplacer(self, x, y):
        bornesRS.x = x
        bornesRS.y = y
        
class Temps():
    def __init__(self):
        self.running = False
        self.timeStart = None
        self.time = None
    
    #Demarre le temps
    def start(self):
        if self.running == False:
            self.timeStart = datetime.datetime.now()
            self.running = True
    
    #Arrete le temps
    def stop(self):
        if self.running:
            self.time = datetime.datetime.now() - self.timeStart
            self.running = False
            
    #Retourne un string du nombre de secondes ecoule
    def getTemps(self):
        if self.running:
            self.time = datetime.datetime.now() - self.timeStart
            return str(self.time.seconds)
        else:
            return str(self.time.seconds)
        
class GerantCollision():
    #Methode de verification pour les collisions entre formes
    def collisionForme(self, bornesA, bornesB):
        bornesGauche = [bornesA.x, bornesB.x]
        bornesTop = [bornesA.y, bornesB.y]
        bornesDroite = [bornesA.x+bornesA.longueur, bornesB.x+bornesB.longueur]
        bornesBas = [bornesA.y+bornesA.hauteur, bornesB.y+bornesB.hauteur]
        interGauche = max(bornesGauche)
        interTop = max(bornesTop)
        interDroite = min(bornesDroite)
        interBas = min(bornesBas)
        
        #Si on a une collision, on retourne vrai, sinon faux
        if interGauche < interDroite and interTop < interBas:
            return True
        else:
            return False
    
    #Methode de verification de collision pour les mur exterieur
    def collisionExterieur(self, bornesA, bornesB): #On assume que bornesA est le joueur
        if bornesA.x <= bornesB.x or bornesA.y <= bornesB.y: #On est sorti en haut ou a gauche
            return True
        if bornesA.x+bornesA.longueur >= bornesB.x+bornesB.longueur: #On est sorti a droite
            return True
        if bornesA.y+bornesA.hauteur >= bornesB.y+bornesB.hauteur: #On est sorti en bas
            return True
        return False # On est toujours a l'interieur
        