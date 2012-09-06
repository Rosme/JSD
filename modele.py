'''
modele.py
Fichier contenant les classes modeles du RedSquare
Projet par Jean-Sebastien Fauteux, Samuel Ryc et David Lebrun
'''
##-*- coding: ISO-8859-1 -*-
import random
import time
import random as rd
import controlleur

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
        self.movementSpeedX = 7
        self.movementSpeedY = 7
        if self.directionX == 0:
            self.movementSpeedX *= -1
        if self.directionY == 0:
            self.movementSpeedY *= -1
        
    def getBornes(self):
        return self.bornesFig
        
    def getCouleur(self):
        return self.couleur
        
    def mouvement(self):
        self.interfaceDimension = 375 #j'assume que notre interface de jeu est de 375x375
        '''
        #directionX == 0 donc -x deplacement a gauche
        if(self.directionX == 0):
            if(self.bornesFig.x <= 1):                      #verification si la figure n'est pas sur le cote gauche du cadre (0,y)
                directionX = 1                    #si oui, changement de direction de -x a +x 
            else:                                 #sinon pas a gauche du cadre
                self.bornesFig.x -= self.movementSpeedX     #continue de deplacer a gauche
        
        #directionX == 1 donc +x deplacement vers la droite
        elif(self.directionX == 1):
            if((self.bornesFig.x+self.longueur) >= self.interfaceDimension-1): 
                directionX = 0
            else:
                self.bornesFig.x += self.movementSpeedX
        
        #directionY == 0 donc  -y deplacement vers le bas
        if(self.directionY == 0):
            if(self.bornesFig.y <= 1):
                directionY = 1
            else:
                self.bornesFig.y -= self.movementSpeedY
                
        #directionY == 1 donc +y deplacement vers le haut
        elif(self.directionY == 1):
            if((self.bornesFig.y+self.hauteur) >= self.interfaceDimension-1):
                directionY = 0
            else:
                self.bornesFig.y += self.movementSpeedY'''
        
        if self.bornesFig.x <= 0 or self.bornesFig.x >= self.interfaceDimension:
            self.movementSpeedX *= -1
        if self.bornesFig.y <= 0 or self.bornesFig.y >= self.interfaceDimension:
            self.movementSpeedY *= -1
        
        self.bornesFig.x += self.movementSpeedX
        self.bornesFig.y += self.movementSpeedY
        
class RedSquare():
    def __init__(self):
        self.bornesRS = Bornes(200, 150, 50, 50)
        self.couleur = "red"      
        
    def getBornes(self):
        return self.bornesRS
    
    def getCouleur(self):
        return self.couleur
        
    def deplacer(self, x, y):
        self.bornesRS.x = x
        self.bornesRS.y = y
        
class Temps():
    def __init__(self):
        self.running = False
        self.timeStart = None
        self.time = None
    
    #Demarre le temps
    def start(self):
        if self.running == False:
            self.timeStart = time.time()
            self.running = True
    
    #Arrete le temps
    def stop(self):
        if self.running:
            self.time = time.time() - self.timeStart
            self.running = False
            
    #Retourne un string du nombre de secondes ecoule
    def getTemps(self):
        if self.running:
            self.time = time.time() - self.timeStart
            return str(round(self.time, 2))
        else:
            return str(round(self.time, 2))
        
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

class Niveau():
    def __init__(self):
        self.lvl = 1
        self.rouge = RedSquare()
        self.formes = list()
        self.nouveau()
    
    def getFormes(self):
        return self.formes
    
    def getRouge(self):
        return self.rouge
    
    def nouveau(self):
        self.lvl += 1
        self.formes = list()
        self.formes.append(Formes(10, 10, 50, 50, "blue"))
        self.formes.append(Formes(10, 300, 50, 50, "blue"))
        self.formes.append(Formes(300, 200, 50, 50, "blue"))
        self.formes.append(Formes(250, 20, 50, 50, "blue"))
            
class Carte():
    def __init__(self):
        self.niveau = Niveau()
        self.bornes = Bornes(0, 0, 375, 375)
    
    def getBornes(self):
        return self.bornes
    
    def getNiveau(self):
        return self.niveau
    
if __name__ == '__main__':       
    j = controlleur.Jeu()
    j.run()         
