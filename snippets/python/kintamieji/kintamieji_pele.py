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
  # BEGIN_RODYTI
  nustatyk_teptuko_splavą('raudona')
  piešk_stačiakampį(100, 100, 20, 20)
  nustatyk_teptuko_splavą('žydra')
  piešk_stačiakampį(10, 10, 20, 20)
  # END_RODYTI

    