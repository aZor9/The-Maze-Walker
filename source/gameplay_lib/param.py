from pystyle import*
from keyboard import*
import os

nv = "undefined"

def parametres():
  global nv
  Write.Print("Paramètres : \n", Colors.white, interval=0.05)
  niveau = Write.Input("Il y a 3 niveaux possibles : Facile (11x11), Moyen (21x21), Dur (31,31) \n\
Tapez F, M ou D pour choisir votre niveau, le niveau par défaut est Moyen. Bon courage !\n\
Tapez ensuite B pour retourner en arrière.\n",Colors.white, interval=0.05)
  if niveau.lower() == "f":
    nv = (11,11)
    print("Vous avez choisi le niveau facile. Tapez B pour retourner en arrière\n")
  elif niveau.lower() == "d":
    nv = (31,31)
    print("Vous avez choisi le niveau difficile. Tapez B pour retourner en arrière\n")
  elif niveau.lower() == "m":
    nv = (21,21)
    print("Vous avez choisi le niveau moyen. Tapez B pour retourner en arrière\n")
  while True:
    if is_pressed("b") or is_pressed("B"):
      os.system("cls")
      import gameplay
      gameplay.accueil()

def returnnv():
  global nv
  return nv

def commandes():
  Write.Print("Dans The Maze Walker, vous pouvez utiliser q pour quitter le jeu et les flèches directionnelles pour vous déplacer. \n\
Pour afficher le temps de jeu, appuyez sur h. \n\
Appuyez sur b pour retourner à l'accueil \n", Colors.white, interval=0.05)
  while True:
    if is_pressed("b"):
      os.system("cls")
      import gameplay
      gameplay.accueil()

""" le morceau de code suivant est inutilisé car il n'y a pas encore d'ennemis
  texteennemi = False
  textedegat = False
  global texteennemi
  global textedegat
  paramennemi = Write.Input(f"Les repliques face aux ennemis sont actuellement en état {texteennemi} \n\
pour les modifier, tapez '{not texteennemi}' ou 'Passer' pour passer à la suite \n", Colors.white, interval=0.05)
  paramdegat = Write.Input(f"Les repliques en cas de dégâts sont actuellement en état {textedegat} \n\
pour les modifier, tapez '{not textedegat}' ou 'Passer' pour passer à la suite \n", Colors.white, interval=0.05)

  if (paramennemi.capitalize() != "Passer") and (paramennemi.capitalize() != "True") and (paramennemi.capitalize() != "False"):
    Write.Print("Ce n'est pas l'entrée attendue ! Veuillez réessayer\n", Colors.white, interval=0.05)
    parametres()
  elif paramennemi.capitalize() != "Passer":
    texteennemi = paramennemi.capitalize()
  
  if (paramdegat.capitalize() != "Passer") and (paramdegat.capitalize() != "True") and (paramdegat.capitalize() != "False"):
    Write.Print("Ce n'est pas l'entrée attendue ! Veuillez réessayer\n", Colors.white, interval=0.05)
    parametres()
  elif paramdegat.capitalize() != "Passer":
    textedegat = paramdegat.capitalize()

  a = Write.Input("Les changements effectués ont été appliqués, tapez 'Retour' pour commencer à jouer\n", Colors.white, interval=0.05)
  
  if a.lower() == "retour":
    import gameplay
    gameplay.accueil()
    #print(f"Vous avez choisi {texteennemi} pour les dialogues face aux ennemis et {textedegat} pour les textes de dégât")
"""
