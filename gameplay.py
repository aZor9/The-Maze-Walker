from pystyle import *
from gameplay_lib.textes import debut
import gameplay_lib.param
import threading
from gameplay_lib.personnage import character
from keyboard import is_pressed, send
from time import sleep
import os

def accueil():
  th1.start()
  th2.start()
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
    os.system("cls")
    param.commandes()
def jeu(Y,X):
  #debut()
  from src.Laby import Labyrinthe
  global LABY
  LABY = Labyrinthe(Y,X)
  LABY.gen()
  global player
  milieu = (Y, X)
  player = character(50, milieu, "", 1, LABY)
  LABY.set_player(player)
  th3.start()
  
def touches():
  while True:
    if is_pressed("up"):
      LABY.move(player.haut())
      sleep(0.18)
      os.system("cls")
      LABY.blind()
      #print(LABY)

    if is_pressed("down"):
      LABY.move(player.bas())
      sleep(0.18)
      os.system("cls")
      LABY.blind()
      #print(LABY)

    if is_pressed("left"):
      LABY.move(player.gauche())
      sleep(0.18)
      os.system("cls")
      LABY.blind()
      #print(LABY)

    if is_pressed("right"):
      LABY.move(player.droite())
      sleep(0.18)
      os.system("cls")
      LABY.blind()
      #print(LABY)

    if is_pressed("q"):
        os._exit(0)

def fctemps():
  import gameplay_lib.temps as temps
  temps.calctemps()

def wincase():
  print("Vous avez gagné !!")
  send('h')
  os._exit(0)

th1 = threading.Thread(target=lambda : jeu(23, 23))
th2 = threading.Thread(target=fctemps)
th3 = threading.Thread(target=touches)

if __name__ == "__main__":
    accueil()
