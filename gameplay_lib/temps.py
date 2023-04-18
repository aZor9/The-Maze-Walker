from time import time, sleep
from keyboard import is_pressed
from math import floor

def calctemps():
  tempsepoch = time()
  global tp
  tp = 0
  while True:
    if is_pressed("h"):
      temps2 = time()
      tp = int(temps2 - tempsepoch)
      __convertisseur__()
      sleep(0.7)

def __convertisseur__():
  secondes = tp%60
  minutes = tp/60
  if minutes < 1:
    if secondes == 1:
      affichagetp = f"Vous avez joué {secondes} seconde."
    else:
      affichagetp = f"Vous avez joué {secondes} secondes."
  else:
    if minutes == 1:
      affichagetp = f"Vous avez joué {floor(minutes)} minute et {secondes} secondes."
    else:
      affichagetp = f"Vous avez joué {floor(minutes)} minutes et {secondes} secondes."
  if minutes > 60:
    heures = tp/3600
    minutes = tp%60
    affichagetp = f"Vous avez joué {floor(heures)} heures, {floor(minutes)} minutes et {secondes} secondes."
  return affichagetp

if __name__ == "__main__":
  calctemps()