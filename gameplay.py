from pystyle import *
from textes import debut
import param
import threading

def proc():
  debut()
  import Laby
  Laby.Labyrinthe()

def proc2():
  import temps
  temps.calctemps()

def accueil():
  Write.Print("Bienvenue dans The Maze Walker \n", Colors.white, interval=0.05)
  action = Write.Input("Que souhaitez-vous faire ? \n\
Paramètres - Jouer - Quitter \n", Colors.white, interval=0.05)

  if action.lower() == "parametres" or "paramètres":
    param.parametres()

  if action.lower() == "jouer":
    th1.start()
    th2.start()

  if action.lower() == "quitter":
    quit()

th1 = threading.Thread(target=proc)
th2 = threading.Thread(target=proc2)

if __name__ == "__main__":
  accueil()
