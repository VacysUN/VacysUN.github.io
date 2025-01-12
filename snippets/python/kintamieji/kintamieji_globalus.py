from p5 import *
from bendri import *

EKRANO_PLOTIS = 200
EKRANO_AUKSTIS = 200

# BEGIN_RODYTI
x = 10 # nustatome pradinę x koordinatę
# END_RODYTI

def setup():
    createCanvas(EKRANO_PLOTIS, EKRANO_AUKSTIS)
    rectMode(CENTER)

def draw():
  global x
  klavišas = key
  pelėsX = mouseX
  pelėsY = mouseY
  valandos = hour()
  minutės = minute()
  sekundės = second()
  background(spalvos.get('šviesiai pilkšva', 'black'))
  stroke(spalvos.get('tamsiai pilkšva', 'black'))
  nustatyk_teptuko_splavą('žydra')
  # BEGIN_RODYTI
  # pabandykite kintamąjam 'pradžia' priskirti kitamųjų pelėsX ar pelėsY reikšmes
  # tuomet užveskitės pelės žymeklį ant ekrano ir pažiūrėkite kas atsitiks
  piešk_stačiakampį(x, 100 , 20, 20)
  x = x + 1
  # END_RODYTI

    
