from pystyle import *
from textes import debut
import param
import threading
from personnage import character

def jeu():
  #debut()
  import Laby
  LABY = Laby.Labyrinthe()
  player = character(50, [75, 75], "", 1, LABY)
  print(LABY)
  print(player.position)
  LABY.blit(player.position, player.haut())
  print(LABY)

def fctemps():
  import temps
  temps.calctemps()

def accueil():
  Write.Print("Bienvenue dans The Maze Walker \n", Colors.white, interval=0.05)
  action = Write.Input("Que souhaitez-vous faire ? \n\
Paramètres - Jouer - Quitter \n", Colors.white, interval=0.05)

  if action.lower() == "parametres":
    param.parametres()

  if action.lower() == "jouer":
    th1.start()
    th2.start()

  if action.lower() == "quitter":
    quit()

th1 = threading.Thread(target=jeu)
th2 = threading.Thread(target=fctemps)

if __name__ == "__main__":
    th1.start()
    #accueil()
