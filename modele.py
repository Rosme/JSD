'''
modele.py
Fichier contenant les classes modeles du RedSquare
Projet par Jean-Sebastien Fauteux, Samuel Ryc et David Lebrun
'''
##-*- coding: ISO-8859-1 -*-
import random
import time
import datetime

class Bornes():
    def __init__(self, x, y, longueur, hauteur):
        self.x = x
        self.y = y
        self.longueur = longueur
        self.hauteur = hauteur
        
class Formes():
    def __init__(self, x, y, longueur, hauteur, couleur):
        self.x = x
        self.y = y
        self.longueur = longueur
        self.hauteur = hauteur
        self.couleur = couleur
        self.bornesFig = Bornes(self.x, self.y, self.longueur, self.hauteur)
        
        #inisialisation de la direction de depart
        '''si x = 0 deplacement a gauche (-x)
           si x = 1 deplacement a droite (+x)
           idem pour y                            '''
        self.directionX = random.randrange(2) #methodes random: retourne soit 0 ou 1
        self.directionY = random.randrange(2)
        
    def getBornes(self):
        return self.bornesFig
        
    def getCouleur(self):
        return self.couleur
        
    def update(self):
        None
        
    def mouvement(self):
        # !!! les vitesses de deplacement sont a modifier !!! 
        self.movementSpeedX = 1
        self.movementSpeedY = 1
        
        self.interfaceDimension = 400 #j'assume que notre interface de jeu est de 400x400
        
        #directionX == 0 donc -x deplacement a gauche
        if(self.directionX == 0):
            if(self.x == 0):                      #verification si la figure n'est pas sur le cote gauche du cadre (0,y)
                directionX = 1                    #si oui, changement de direction de -x a +x 
            else:                                 #sinon pas a gauche du cadre
                self.x -= self.movementSpeedX     #continue de deplacer a gauche
        
        #directionX == 1 donc +x deplacement vers la droite
        elif(self.directionX == 1):
            if((self.x+self.longueur) == self.interfaceDimension): 
                directionX = 0
            else:
                self.x += self.movementSpeedX
        
        #directionY == 0 donc  -y deplacement vers le bas
        if(self.directionY == 0):
            if(self.y == 0):
                directionY = 1
            else:
                self.y -= self.movementSpeedY
                
        #directionY == 1 donc +y deplacement vers le haut
        elif(self.directionY == 1):
            if((self.y+self.hauteur) == self.interfaceDimension):
                directionY = 0
            else:
                self.y += self.movementSpeedY
                
class RedSquare():
    def __init__(self):
        self.bornesRS = Bornes(100, 100, 20, 20)
        self.couleur = "RED"      
        
    def getBornes(self):
        return self.bornesRS
    
    def getCouleur(self):
        return self.couleur
        
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
        