from time import time, sleep
from keyboard import is_pressed
from math import floor

def calctemps():
  global tempsepoch
  tempsepoch = time()
  while True:
    if is_pressed("h"):
      call()

def call():
  temps2 = time()
  global tp
  tp = int(temps2 - tempsepoch)
  __convertisseur__()
  sleep(0.7)

def __convertisseur__():
  secondes = tp%60
  minutes = tp/60
  if minutes < 1:
    if secondes == 1:
      affichagetp = f"Vous avez joué pendant {secondes} seconde."
    else:
      affichagetp = f"Vous avez joué pendant {secondes} secondes."
  else:
    if minutes == 1:
      affichagetp = f"Vous avez joué pendant {floor(minutes)} minute et {secondes} secondes."
    else:
      affichagetp = f"Vous avez joué pendant {floor(minutes)} minutes et {secondes} secondes."
  if minutes > 60:
    heures = tp/3600
    minutes = tp%60
    affichagetp = f"Vous avez joué pendant {floor(heures)} heures, {floor(minutes)} minutes et {secondes} secondes."
  print(affichagetp)

if __name__ == "__main__":
  calctemps()