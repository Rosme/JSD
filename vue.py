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
        self.fenetre.title("RedSquare - Projet B41")
        self.panelPrincipal()
        self.panelSecondaire()
        self.FenetrePrincipal.pack()
        self.FenetreSecondaire.place(in_=self.FenetrePrincipal, anchor="c", relx=.4, rely=.4)
        self.centrerFenetre()
        
class RenduInterface():
    
    def __init__(self):
        return None
    
    def bouttonQuitter(self):
        self.BouttonQuitter = Button(rc.FenetrePrincipal, text = "Quitter", bg = "white", command = rc.FenetrePrincipal.quit)
        #self.BouttonQuitter.pack()                    #A revoir, quand pack() change l'interface et bouton ne s'affiche pas
    
    def bouttonInfo(self):
        return None
    
    def afficherBoutton(self):
        self.bouttonQuitter()

if __name__ == '__main__':         
    rc = RenduCarte()
    ri = RenduInterface()
    rc.afficherCarte()
    ri.afficherBoutton()
    rc.fenetre.mainloop()       #Demarre le gestionnaire d'evenements
