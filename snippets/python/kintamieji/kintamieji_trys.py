from p5 import *
from bendri import * 

EKRANO_PLOTIS = 100
EKRANO_AUKSTIS = 100


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
  piešk_stačiakampį(10, 10, 10, 10)
  piešk_stačiakampį(10 + 20, 10, 10, 10)
  piešk_stačiakampį(10 + 40, 10, 10, 10)
  # END_RODYTI

    