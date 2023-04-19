from pystyle import*
from copy import deepcopy
from random import randrange

"""
from gameplay_lib.param import textedegat, texteennemi

repliques = ["Tiens (BAM) prends ça ! \n", "Ça n'en finit plus ! \n", "Je finirai par tous les avoir \n", 
            "Excusez-moi je pense qu'on essaye de vous tuer, ah oui c'est moi (PAW) \n", "Mange toi ça ! \n"]

global repliquesliste
repliquesliste = deepcopy(repliques)

repdegats = ["Aie, ça ça fait mal ! \n", "ouch, il m'a eu \n", "Je me vengerais \n", 
            "Tu ne paies rien pour attendre \n", "Ça c'était un coup de chance pour toi ! \n"]
global repdegatsliste
repdegatsliste = deepcopy(repdegats)
"""

def debut():
    texte = Center.XCenter(Box.DoubleCube("30 septembre 2206\n\
Cette lettre est la sixième, une par jour depuis le jour où tout a basculé. \n\
Avant j’avais une vie lambda, vide d’émotions, ni famille, ni amis.\n\
Je ne sais même pas si quelqu’un lira un jour cette lettre. \n\
Je ne sais ni où je suis, ni pourquoi j’y suis… l'atmosphère est particulière, je veux sortir.. \n\
J’essaierai ce soir…\n"))
    Write.Print(texte, Colors.white, interval=0.03)
    print("")

"""
def ennemi1():
    Write.Print("AH !! En plus il y a des ennemis ?! \n", Colors.white, interval=0.05)

def ennemi2():
    Write.Print("Encore un ??? \n", Colors.white, interval=0.05)

def ennemimort():
    global texteennemi
    if texteennemi:
        global repliquesliste
        if repliquesliste != None:
            indice = randrange(0, len(repliquesliste))
            Write.Print(repliquesliste[indice], Colors.white, interval=0.05)
            repliquesliste.pop(indice)
        else:
            repliquesliste = deepcopy(repliques)
            ennemimort()

def aiedegat():
    global textedegat
    if textedegat:
        global repdegatsliste
        if repdegatsliste != None:
            indice = randrange(0, len(repdegatsliste))
            Write.Print(repdegatsliste[indice], Colors.white, interval=0.05)
            repdegatsliste.pop(indice)
        else:
            repdegatsliste = deepcopy(repdegats)
            ennemimort()
"""