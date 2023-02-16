from pystyle import *
from textes import debut
import param
import threading
from personnage import character
from keyboard import is_pressed
from time import sleep
import os

def accueil():
  Write.Print("Bienvenue dans The Maze Walker \n", Colors.white, interval=0.05)
  action = Write.Input("Que souhaitez-vous faire ? \n\
Paramètres - Commandes - Jouer - Quitter \n", Colors.white, interval=0.05)

  if action.lower() == "parametres":
    param.parametres()

  if action.lower() == "jouer":
    th1.start()
    th2.start()

  if action.lower() == "quitter":
    quit()

  if action.lower() == "commandes":
    param.commandes()

def jeu(Y,X):
  #debut()
  import Laby
  global LABY
  LABY = Laby.Labyrinthe(Y,X)
  global player
  milieu = [Y//2 + Y , X//2 + X]
  player = character(50, milieu, "", 1, LABY)
  LABY.set_player(player)
  player.haut()
  player.bas()
  print(LABY)
  th3.start()
  
def touches():
  while True:
    if is_pressed("up"):
      if not player.haut():
        sleep(0.3)
        os.system("cls")
        LABY.blind()

    if is_pressed("down"):
      if not player.bas():
        sleep(0.3)
        os.system("cls")
        LABY.blind()

    if is_pressed("left"):
      if not player.gauche():
        sleep(0.3)
        os.system("cls")
        LABY.blind()

    if is_pressed("right"):
      if not player.droite():
        sleep(0.3)
        os.system("cls")
        LABY.blind()

    if is_pressed("q"):
        os._exit(0)

def fctemps():
  import temps
  temps.calctemps()

th1 = threading.Thread(target=lambda : jeu(21,21))
th2 = threading.Thread(target=fctemps)
th3 = threading.Thread(target=touches)

if __name__ == "__main__":
    #accueil()
    jeu(21,21)
