from p5 import *
from bendri import * 

EKRANO_PLOTIS = 200
EKRANO_AUKSTIS = 200

def setup():
    createCanvas(EKRANO_PLOTIS, EKRANO_AUKSTIS)

def draw():
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
  pradžia = 40
  piešk_stačiakampį(pradžia, 10, 10, 10)
  piešk_stačiakampį(pradžia + 20, 10, 10, 10)
  piešk_stačiakampį(pradžia + 40, 10, 10, 10)
  # END_RODYTI

    
