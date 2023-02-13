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

def jeu():
  #debut()
  import Laby
  global LABY
  LABY = Laby.Labyrinthe()
  global player
  player = character(50, [120, 120], "", 1, LABY)
  LABY.blit(player.haut(), 'P')
  print(LABY)
  

def deplacements():
  while True:
    if is_pressed("up"):
      LABY.blit(player.haut(), 'P')
      #os.system("cls")
      print(LABY)
    if is_pressed("down"):
      LABY.blit(player.bas(), 'P')
      #os.system("cls")
      print(LABY)
    if is_pressed("left"):
      LABY.blit(player.gauche(), 'P')
      #os.system("cls")
      print(LABY)
    if is_pressed("right"):
      LABY.blit(player.droite(), 'P')
      #os.system("cls")
      print(LABY)

def fctemps():
  import temps
  temps.calctemps()

def quitter():
  while True:
    if is_pressed("q"):
      os._exit(0)

th1 = threading.Thread(target=jeu)
th2 = threading.Thread(target=fctemps)
th3 = threading.Thread(target=deplacements)
th4 = threading.Thread(target=quitter)

if __name__ == "__main__":
    th1.start()
    th2.start()
    th3.start()
    th4.start()
    #accueil()
