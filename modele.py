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