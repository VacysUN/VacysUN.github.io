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
  line(0, 100, 200, 100) # nubrėžiame vertikalią liniją drobės viduryje
  nustatyk_teptuko_splavą('žalia')
  if klavišas == '1':
    piešk_apskritimą(50, 50, 50)
  elif klavišas == '2':
    piešk_apskritimą(150, 50, 50)
  elif klavišas == '3':
    piešk_apskritimą(50, 150, 50)
  elif klavišas == '4':
    piešk_apskritimą(150, 150, 50)
  # END_RODYTI