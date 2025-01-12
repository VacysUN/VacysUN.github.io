from p5 import *
from bendri import *


EKRANO_PLOTIS = 200
EKRANO_AUKSTIS = 200

def nupiešk_stulpelį(x, aukštis):
    rect( (x + 1) * 20 + 1, EKRANO_AUKSTIS - aukštis * 10, 18, aukštis*10)

def nupiešk_tinklelį():
    push()
    stroke(spalvos.get('vidutiniškai pilkšva', 'black'))
    for y in range(10, EKRANO_AUKSTIS, 20):
        line(0, y, EKRANO_PLOTIS, y)
    pop()


def setup():
    createCanvas(EKRANO_PLOTIS, EKRANO_AUKSTIS)
    rectMode(CORNER)

def draw():
    #12, 14, 15, 15, 12, 11, 12 
    background(spalvos.get('šviesiai pilkšva', 'black'))  
    nupiešk_tinklelį()
    nustatyk_teptuko_splavą('žalia')
    # BEGIN_RODYTI
    temperatūros = [12, 14, 15, 15, 12, 11, 12]
    for diena in range(7):
        # kintamasis diena, kiekvieną kartą vykdant ciklą bus lygus skaičiui nuo 0 iki 6
        nupiešk_stulpelį(diena, temperatūros[diena])
    # END_RODYTI