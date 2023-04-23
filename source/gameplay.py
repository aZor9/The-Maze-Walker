from pystyle import *
from gameplay_lib.textes import debut
import gameplay_lib.param as param
import threading
from gameplay_lib.personnage import character
import gameplay_lib.temps as temps
from keyboard import is_pressed
from time import sleep
from os import system, _exit

def accueil():
  Write.Print("Bienvenue dans The Maze Walker \n", Colors.white, interval=0.05)
  Write.Print("Que souhaitez-vous faire ? \n\
Paramètres (P) - Commandes (C) - Jouer (J) - Quitter (Q)\n", Colors.white, interval=0.05)

  cmd = False
  while not cmd:

    action = input("")

    if (action.casefold() == "parametres") or (action.casefold() == 'p'):
      system("cls")
      param.parametres()
      cmd = True

    elif (action.casefold()) == "jouer" or (action.casefold() == 'j'):
      system("cls")
      niveau = param.returnnv()
      if niveau == "undefined":
        jeu()
      else:
        jeu(niveau[0], niveau[1])
      th1.start()
      cmd = True

    elif (action.casefold()) == "quitter" or (action.casefold() == 'q'):
      quit()
      cmd = True

    elif (action.casefold()) == "commandes" or (action.casefold() == 'c'):
      system("cls")
      param.commandes()
      cmd = True

    elif (action.casefold() == 'a'):
      system("start ./source/index.html")
      action = ""

def jeu(Y = 21,X = 21):
  #debut()
  sleep(1)
  system("cls")
  from Laby import Labyrinthe
  global LABY
  LABY = Labyrinthe(Y,X)
  LABY.gen()
  global player
  milieu = (Y, X)
  player = character(50, milieu, "", 1, LABY)
  LABY.set_player(player)
  LABY.first_print()
  th2.start()

def touches():
  while True:
    if is_pressed("up"):
      LABY.move(player.haut())
      sleep(0.3)
      system("cls")
      #LABY.blind()
      #print(LABY)
      LABY.renderv2()

    elif is_pressed("down"):
      LABY.move(player.bas())
      sleep(0.3)
      system("cls")
      #LABY.blind()
      #print(LABY)
      LABY.renderv2()

    elif is_pressed("left"):
      LABY.move(player.gauche())
      sleep(0.3)
      system("cls")
      #LABY.blind()
      #print(LABY)
      LABY.renderv2()

    elif is_pressed("right"):
      LABY.move(player.droite())
      sleep(0.3)
      system("cls")
      #LABY.blind()
      #print(LABY)
      LABY.renderv2()

    elif is_pressed("q"):
        _exit(0)

    elif is_pressed('a'):
      system("start ./source/index.html")
      sleep(0.5)

def fctemps():
  temps.calctemps()

def wincase():
  print("Vous avez gagné !!")
  print(temps.call())
  _exit(0)

th1 = threading.Thread(target=fctemps)
th2 = threading.Thread(target=touches)

if __name__ == "__main__":
  acceuil()
