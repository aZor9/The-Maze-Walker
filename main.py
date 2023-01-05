from pystyle import*
from textes import debut
import param
import threading

def accueil():
  Write.Print("Bienvenue dans The Maze Walker \n", Colors.white, interval=0.05)
  action = Write.Input("Que souhaitez-vous faire ? \n\
Parametres - Jouer - Quitter \n", Colors.white, interval=0.05)

  if action.lower() == "parametres":
    param.parametres()

  if action.lower() == "jouer":
    debut()
    import Laby
    Laby.Labyrinthe()

  if action.lower() == "quitter":
    quit()

if __name__ == "__main__":
  accueil()