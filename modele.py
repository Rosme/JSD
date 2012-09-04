class Bornes():
    def __init__(self, x, y, longueur, hauteur):
        self.x = x
        self.y = y
        self.longueur = longueur
        self.hauteur = hauteur
        
class Formes():
    def __init__(self):
        
    def getBornes(self):
        
    def getCouleur(self):
        
    def update(self):
        
    def mouvement(self):
        
        
class RedSquare():
    def __init__(self):
        '''
        self.x = 50 #position x du RedSquare au depart (A  modifier eventuellement)
        self.y = 50 #position y du RedSquare au depart (A  modifier eventuellement)
        self.longueur = 20 #longueur du RedSquare
        self.hauteur = 20 #largeur du RedSquare
        '''
        self.bornesRS = Bornes(50, 50, 20, 20)        
        
    def getBornes(self):
        #self.bornesRS = Bornes(x, y, longueur, hauteur) #RS pour RedSquare (abreviation)
        return self.bornesRS
        
        
    def deplacer(self, x, y):
        bornesRS.x = x
        bornesRS.y = y