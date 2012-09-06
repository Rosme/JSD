'''
vue.py
Fichier contenant les classes vue du Redsquare
Projet par Jean-Sebastien Fauteux, Samuel Ryc et David Lebrun
'''
##-*- coding: ISO-8859-1 -*-
from tkinter import *
from tkinter import messagebox

import controlleur

class RenduCarte():

    def __init__(self, parent, redsquare, formes):
        self.parent = parent
        self.redsquare = redsquare
        self.formes = formes
        self.bleu = list()
        self.canvas=Canvas(width=375,height=375, bd=2, bg="white")            #contient le jeux
        borneRedSquare = redsquare.getBornes()
        self.rouge = self.canvas.create_rectangle(borneRedSquare.x,borneRedSquare.y,borneRedSquare.x+borneRedSquare.longueur,borneRedSquare.y+borneRedSquare.hauteur, fill=redsquare.getCouleur())
        #self.canvas.delete(self.rouge)
        #self.canvas.update() 

    ###Dessine les rectangles (ennemies) dans le canvas
    def dessinerFormes(self):
        for f in self.bleu:
            self.canvas.delete(f)
        
        for f in self.formes:
            borne = f.getBornes()
            self.bleu.append(self.canvas.create_rectangle(borne.x, borne.y, borne.x+borne.longueur, borne.y+borne.hauteur, fill=f.getCouleur()))
        
        self.canvas.update()
    
    ###Dessinge le redsquare dans le canvas
    def dessinerRedsquare(self):
        self.canvas.bind("<B1-Motion>", self.deplacerRedsquare)
    
        ###Permet de deplacer le redsquare
    def deplacerRedsquare(self, event):
        self.canvas.delete(self.rouge)
        x = event.x
        y = event.y
        self.redsquare.deplacer(x,y)
        borneRedSquare = self.redsquare.getBornes()
        self.rouge = self.canvas.create_rectangle(x-25,y-25,x+25,y+25, fill=self.redsquare.getCouleur())
        self.canvas.update()
    
    ###Permet d'afficher les widgets du jeux et de packer les widgets   
    def afficherFenetre(self):                   
        self.canvas.place(in_=self.parent.fenPrincipale, anchor="c", relx=.4, rely=.4)
        
    ###Permet d'afficher les widgets du jeux et de packer les widgets   
    def afficherFenetre(self):                   
        self.canvas.place(in_=self.parent.fenPrincipale, anchor="c", relx=.4, rely=.4)
        self.dessinerRedsquare()
        self.dessinerFormes()
        
class RenduOption():
    
    def __init__(self, parent):
        self.bouttonInfo=Button(parent.fenBoutton, text="Informations", padx=60, command=self.afficherInfo)
        self.bouttonQuit=Button(parent.fenBoutton, text="Quitter", padx=60, command=parent.root.quit)
    
    
    ###Affiche les informations si l'utilisateur clique sur le bouton informations. fonction de la command du boutton    
    def afficherInfo(self):
        messagebox.showinfo("Informations", "Developpe par :\n\nJean-Sebatien Fauteux\n\nSamuel Ryc\n\nDavid Lebrun")
        
    ###Affiche les bouton a partir de afficherFenetre dans RenduCarte()
    def afficherBouton(self):
        self.bouttonInfo.pack(side=LEFT)
        self.bouttonQuit.pack(side=LEFT)
        
class RenduInterface():
    
    def __init__(self, parent, redsquare, formes):
        self.root = Tk()
        self.root.title("RedSquare - Projet B41")
        self.formes = formes
        self.parent = parent
        self.redsquare = redsquare
        self.fenPrincipale=Frame(width=600, height=600, bd = 2, colormap="new", relief = 'groove', bg = "black")    #contient frame du jeux, bouton et eventuellement frame pour highscore
        self.fenBoutton=Frame(bd=2, colormap="new")
        self.rcCarte = RenduCarte(self, redsquare, formes)
        self.option = RenduOption(self)
        self.alive = True
        
    def dessiner(self):
        self.centrerFenetre()
        self.fenPrincipale.pack()
        self.fenBoutton.place(in_=self.fenPrincipale,relx=.1, rely=.8)
        self.rcCarte.afficherFenetre()
        self.option.afficherBouton()
        self.parent.update()
        self.root.mainloop()
        
    ###Permet de centrer l'application au centre de l'ecran
    def centrerFenetre(self,w=600, h=500):              
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
              
    
    def gameOver(self):
        if self.alive:
            messagebox.showinfo("Vous etes mort!", "Oups! Vous etes mort!")
            self.alive = False
            self.reset()
    
    def reset(self):
        self.parent.reset()
        self.formes = self.parent.niveau.getFormes()
        self.redsquare = self.parent.niveau.getRouge()
        self.rcCarte = RenduCarte(self, self.redsquare, self.formes)
        
if __name__ == '__main__':       
    j = controlleur.Jeu()
    j.run()         
