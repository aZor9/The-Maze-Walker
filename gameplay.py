from pystyle import *
from textes import debut
import param
import threading
from personnage import character
from keyboard import is_pressed
import os

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

def jeu(Y,X):
  #debut()
  import Laby
  global LABY
  LABY = Laby.Labyrinthe(Y,X)
  global player
  milieu = [Y//2 + Y , X//2 + X]
  player = character(50, milieu, "", 1, LABY)
  player.haut()
  player.bas()
  print(LABY)
  
def touches():
  while True:
    if is_pressed("up"):
      if not player.haut():
        os.system("cls")
        print(LABY)
    if is_pressed("down"):
      if not player.bas():
        os.system("cls")
        print(LABY)
    if is_pressed("left"):
      if not player.gauche():
        os.system("cls")
        print(LABY)
    if is_pressed("right"):
      if not player.droite():
        os.system("cls")
        print(LABY)
    if is_pressed("q"):
        os._exit(0)

def fctemps():
  import temps
  temps.calctemps()

th1 = threading.Thread(target=lambda : jeu(21,21))
th2 = threading.Thread(target=fctemps)
th3 = threading.Thread(target=touches)

if __name__ == "__main__":
    th1.start()
    th2.start()
    th3.start()
    #accueil()
