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
  line(100, 0, 100, 200) # nubrėžiame vertikalią liniją drobės viduryje
  if pelėsX < 100:
    nustatyk_teptuko_splavą('žalia')
    piešk_stačiakampį(100, 100 , 50, 50)
  else:
    nustatyk_teptuko_splavą('žydra')
    piešk_apskritimą(100, 100, 50)
  # END_RODYTI