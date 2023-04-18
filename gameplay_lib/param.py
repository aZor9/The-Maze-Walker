from pystyle import*
from keyboard import*
import os
texteennemi = False
textedegat = False

def parametres():
  global texteennemi
  global textedegat

  Write.Print("Paramètres : \n", Colors.white, interval=0.05)
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
  

  if a.capitalize() == "Retour":
    import gameplay
    gameplay.accueil()
    #print(f"Vous avez choisi {texteennemi} pour les dialogues face aux ennemis et {textedegat} pour les textes de dégât")

def commandes():
  Write.Print("Dans The Maze Walker, vous pouvez utiliser q pour quitter le jeu et les flèches directionnelles pour vous déplacer. \n\
Pour afficher le temps de jeu, appuyez sur h. \n\
Appuyez sur b pour retourner à l'accueil \n", Colors.white, interval=0.05)
  while True:
    if is_pressed("b"):
      os.system("cls")
      import gameplay
      gameplay.accueil()