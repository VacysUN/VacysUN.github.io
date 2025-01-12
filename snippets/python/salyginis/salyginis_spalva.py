from p5 import *
from bendri import * 

EKRANO_PLOTIS = 200
EKRANO_AUKSTIS = 200


def setup():
    createCanvas(EKRANO_PLOTIS, EKRANO_AUKSTIS)
    rectMode(CENTER)

def draw():
  klavišas = key
  pelėsX = mouseX
  pelėsY = mouseY
  valandos = hour()
  minutės = minute()
  sekundės = second()
  background(spalvos.get('šviesiai pilkšva', 'black'))
  stroke(spalvos.get('tamsiai pilkšva', 'black'))
  # BEGIN_RODYTI
  nustatyk_teptuko_splavą('žydra')
  if sekundės % 2 == 0:
    nustatyk_teptuko_splavą('žalia')
  piešk_stačiakampį(100, 100 , 50, 50)
  # END_RODYTI

    
