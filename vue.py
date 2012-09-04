'''
vue.py
Fichier contenant les classes vue du Redsquare
Projet par Jean-Sebastien Fauteux, Samuel Ryc et David Lebrun
'''
##-*- coding: ISO-8859-1 -*-
from tkinter import *
from tkinter import messagebox

class RenduCarte():

    def __init__(self):
        self.root = Tk()  
        self.root.title("RedSquare - Projet B41")  
        self.fenPrincipale=Frame(width=600, height=500, bd = 2, colormap="new", relief = 'groove', bg = "black")
        self.fenSecondaire=Frame(width=450,height=380, bd=2,colormap="new", relief='groove', bg="white")
        self.fenBoutton=Frame(bd=2, colormap="new")
        self.bouttonInfo=Button(self.fenBoutton, text="Informations", padx=20, command=self.callback)
        self.bouttonQuit=Button(self.fenBoutton, text="Quitter", padx=35, command=self.root.quit)
        
    def callback(self):
        messagebox.showinfo("Informations", "Developpe par :\nJean-Sebatien Fauteux\nSamuel Ryc\nDavid Lebrun")
        
    def afficherFenetre(self):                         #Permet d'afficher les widgets du jeux et de packer les widgets
        renduOption = RenduOption()
        self.centrerFenetre()
        self.fenPrincipale.pack()
        self.fenSecondaire.place(in_=self.fenPrincipale, anchor="c", relx=.4, rely=.4)
        self.fenBoutton.place(in_=self.fenPrincipale,relx=.1, rely=.8)
        self.bouttonInfo.pack()
        self.bouttonQuit.pack()
    
    def centrerFenetre(self,w=600, h=500):              #Permet de centrer l'application au centre de l'ecran
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))                
        
class RenduOption():                #A revenir plus tard.... gestion des boutons
    
    def __init__(self):
        return None

if __name__ == '__main__':       
    renduCarte = RenduCarte()
    renduCarte.afficherFenetre()
    renduCarte.root.mainloop()       #Demarre le gestionnaire d'evenements
