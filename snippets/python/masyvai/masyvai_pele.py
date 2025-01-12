from p5 import *
from bendri import *


EKRANO_PLOTIS = 200
EKRANO_AUKSTIS = 200

# BEGIN_RODYTI
x = []
y = []
# END_RODYTI
pelėsX = 0
pelėsY = 0

def setup():
    createCanvas(EKRANO_PLOTIS, EKRANO_AUKSTIS)
    rectMode(CORNER)


# BEGIN_RODYTI
def pelėNuspausta():
    # ši funkcija iškviečiama kiekvieną kartą, kai paspaudžiame pelės mygtuką
    x.append(pelėsX)
    y.append(pelėsY)
# END_RODYTI

def mousePressed():
    pelėNuspausta()

def draw():
    global pelėsX
    global pelėsY
    pelėsX = mouseX
    pelėsY = mouseY
    background(spalvos.get('šviesiai pilkšva', 'black'))  
    nustatyk_teptuko_splavą('žalia')

    # BEGIN_RODYTI
    koordinačių_skaičius = len(x) # sužinome, kiek koordinačių turime
    for i in range(koordinačių_skaičius):
        # kintamasis diena, kiekvieną kartą vykdant ciklą bus lygus skaičiui nuo 0 iki 6
      piešk_apskritimą(x[i], y[i], 10)
    # END_RODYTI