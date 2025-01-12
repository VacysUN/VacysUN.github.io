from p5 import *
from bendri import * 

EKRANO_PLOTIS = 200
EKRANO_AUKSTIS = 200


def setup():
    createCanvas(EKRANO_PLOTIS, EKRANO_AUKSTIS)
    rectMode(CENTER)

def draw():
  pelėsX = mouseX
  background(spalvos.get('šviesiai pilkšva', 'black'))
  stroke(spalvos.get('tamsiai pilkšva', 'black'))
  highlight(mouseX)

  nustatyk_teptuko_splavą('žalia')
  # BEGIN_RODYTI
  if pelėsX > 150:
    piešk_apskritimą(150, 100, 50)
  elif pelėsX > 100:
    piešk_apskritimą(100, 100, 50)
  else:
    piešk_apskritimą(50, 100, 50)
  # END_RODYTI