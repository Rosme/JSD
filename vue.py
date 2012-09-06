'''
vue.py
Fichier contenant les classes vue du Redsquare
Projet par Jean-Sebastien Fauteux, Samuel Ryc et David Lebrun
'''
##-*- coding: ISO-8859-1 -*-
from tkinter import *
from tkinter import messagebox

class RenduCarte():

    def __init__(self, parent):
        self.parent = parent
        self.aireJeux=Canvas(width=450,height=370, bd=2, bg="white")            #contient le jeux

    ###Dessine les rectangles (ennemies) dans le canvas
    def dessinerFormes(self):
        self.rectangleHautGauche = self.aireJeux.create_rectangle(10,10,60,125, fill="blue")
        self.rectangleBasGauche = self.aireJeux.create_rectangle(10,300,150,350, fill="blue")
        self.rectangleBasDroite = self.aireJeux.create_rectangle(390,350,440,200, fill="blue")
        self.rectangleHautDroite = self.aireJeux.create_rectangle(250,20,440,70, fill="blue")
    
    ###Dessinge le redsquare dans le canvas
    def dessinerRedsquare(self):
        self.redsquare = self.aireJeux.create_rectangle(200,150,250,200, fill="red") 
    
    ###Permet d'afficher les widgets du jeux et de packer les widgets   
    def afficherFenetre(self):                   
        self.aireJeux.place(in_=self.parent.fenPrincipale, anchor="c", relx=.4, rely=.4)
        self.dessinerFormes()
        self.dessinerRedsquare()
        
class RenduOption():
    
    def __init__(self, parent):
        self.bouttonInfo=Button(parent.fenBoutton, text="Informations", padx=60, command=self.afficherInfo)
        self.bouttonQuit=Button(parent.fenBoutton, text="Quitter", padx=60, command=parent.root.quit)
    
    
    ###Affiche les informations si l'utilisateur clique sur le bouton informations. fonction de la command du boutton    
    def afficherInfo(self):
        messagebox.showinfo("Informations", "Developpe par :\nJean-Sebatien Fauteux\nSamuel Ryc\nDavid Lebrun")
        
    ###Affiche les bouton a partir de afficherFenetre dans RenduCarte()
    def afficherBouton(self):
        self.bouttonInfo.pack(side=LEFT)
        self.bouttonQuit.pack(side=LEFT)
        
class RenduInterface():
    
    def __init__(self, parent):
        self.root = Tk()
        self.root.title("RedSquare - Projet B41")
        self.fenPrincipale=Frame(width=600, height=500, bd = 2, colormap="new", relief = 'groove', bg = "black")    #contient frame du jeux, bouton et eventuellement frame pour highscore
        self.fenBoutton=Frame(bd=2, colormap="new")
        self.carte = RenduCarte(self)
        self.option = RenduOption(self)
        
    def dessiner(self):
        self.centrerFenetre()
        self.fenPrincipale.pack()
        self.fenBoutton.place(in_=self.fenPrincipale,relx=.1, rely=.8)
        self.carte.afficherFenetre()
        self.option.afficherBouton()    
        self.root.mainloop()
        
    ###Permet de centrer l'application au centre de l'ecran
    def centrerFenetre(self,w=600, h=500):              
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
if __name__ == '__main__':       
    renduCarte = RenduCarte()     
    renduOption = RenduOption()
    renduCarte.afficherFenetre()
    renduCarte.root.mainloop()          
