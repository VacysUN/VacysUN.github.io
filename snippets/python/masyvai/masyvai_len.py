from p5 import *
from bendri import *


EKRANO_PLOTIS = 200
EKRANO_AUKSTIS = 200

# BEGIN_RODYTI
x = []
y = []
# END_RODYTI


def setup():
    createCanvas(EKRANO_PLOTIS, EKRANO_AUKSTIS)
    rectMode(CORNER)
    textAlign(CENTER, CENTER)

def draw():
    nuspaustas_klavišas = keyIsPressed
    background(spalvos.get('šviesiai pilkšva', 'black'))  
    nustatyk_teptuko_splavą('žalia')

    stroke(spalvos.get('juoda', 'black'))    
    fill(spalvos.get('juoda', 'black'))

    # BEGIN_RODYTI
    if nuspaustas_klavišas:
      x.append(random(0, 200))
      y.append(random(0, 200))
    # END_RODYTI

    # BEGIN_RODYTI
    rašyk_tekstą(len(x), 100, 100)

    
