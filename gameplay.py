from pystyle import *
from gameplay_lib.textes import debut
import gameplay_lib.param as param
import threading
from gameplay_lib.personnage import character
import gameplay_lib.temps as temps
from keyboard import is_pressed
from time import sleep
import os

def accueil():
  Write.Print("Bienvenue dans The Maze Walker \n", Colors.white, interval=0.05)
  action = Write.Input("Que souhaitez-vous faire ? \n\
Paramètres (P) - Commandes (C) - Jouer (J) - Quitter (Q)\n", Colors.white, interval=0.05)

  if (action.lower() == "parametres") or (action.lower() == "p"):
    os.system("cls")
    param.parametres()

  if (action.lower()) == "jouer" or (action.lower() == "j"):
    os.system("cls")
    niveau = param.returnnv()
    jeu(niveau[0], niveau[1])
    th1.start()

  if (action.lower()) == "quitter" or (action.lower() == "q"):
    quit()

  if (action.lower()) == "commandes" or (action.lower() == "c"):
    os.system("cls")
    param.commandes()

def jeu(Y = 21,X = 21):
  #debut()
  sleep(1)
  os.system("cls")
  from src.Laby import Labyrinthe
  global LABY
  LABY = Labyrinthe(Y,X)
  LABY.gen()
  global player
  milieu = (Y, X)
  player = character(50, milieu, "", 1, LABY)
  LABY.set_player(player)
  print(LABY)
  th2.start()
  
def touches():
  while True:
    if is_pressed("up"):
      LABY.move(player.haut())
      sleep(0.3)
      os.system("cls")
      LABY.blind()
      #print(LABY)

    if is_pressed("down"):
      LABY.move(player.bas())
      sleep(0.3)
      os.system("cls")
      LABY.blind()
      #print(LABY)

    if is_pressed("left"):
      LABY.move(player.gauche())
      sleep(0.3)
      os.system("cls")
      LABY.blind()
      #print(LABY)

    if is_pressed("right"):
      LABY.move(player.droite())
      sleep(0.3)
      os.system("cls")
      LABY.blind()
      #print(LABY)

    if is_pressed("q"):
        os._exit(0)

def fctemps():
  temps.calctemps()

def wincase():
  print("Vous avez gagné !!")
  print(temps.call())
  os._exit(0)

th1 = threading.Thread(target=fctemps)
th2 = threading.Thread(target=touches)

if __name__ == "__main__":
    accueil()
