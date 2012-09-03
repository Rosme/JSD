from tkinter import *

class RenduCarte():

    def __init__(self):
        return None                 
    
    def centrerFenetre(self,w=600, h=500):              #Permet de centrer l'application au centre de l'ecran
        ws = self.fenetre.winfo_screenwidth()
        hs = self.fenetre.winfo_screenheight()
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        self.fenetre.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    def afficherFormes(self):                           #affichages des formes dans le panelSecondaire
        return None                 
    
    def panelPrincipal(self):                           #Contient tout ce qui a dans la fenetre de tkinter  
        self.FenetrePrincipal = Frame(width=600, height=500, bd = 2, colormap="new", relief = 'groove', bg = "black")
    
    def panelSecondaire(self):                          #Contient le jeux 
        self.FenetreSecondaire = Frame(width = 450, height = 380, bd = 2, colormap = "new", relief = 'groove', bg = "white")
    
    def afficherCarte(self):                            #Permet d'afficher les widgets du jeux et de packer les widgets
        self.fenetre = Tk()
        rc.panelPrincipal()
        rc.panelSecondaire()
        self.FenetrePrincipal.pack()
        self.FenetreSecondaire.place(in_=self.FenetrePrincipal, anchor="c", relx=.4, rely=.4)
        rc.centrerFenetre()
        self.fenetre.mainloop()
        
class RenduInterface():
    
    def __init__(self):
        return None                 
    
    def afficherBouton(self):
        return None
    
    def afficherInfo(self):
        return None


if __name__ == '__main__':          #pour tester main
    rc = RenduCarte()
    rc.afficherCarte()
