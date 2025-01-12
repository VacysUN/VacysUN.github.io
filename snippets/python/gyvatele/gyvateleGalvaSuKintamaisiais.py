from p5 import *
from gyvate import * 

# BEGIN_RODYTI
x=9
y=12
# END_RODYTI



def setup():
    createCanvas(EKRANO_PLOTIS, EKRANO_AUKŠTIS)

def draw():
    background(255)
    frameRate(5)
    nupiešti_tinklelį(TINKLELIO_STULPELIŲ_SKAIČIUS,TINKLELIO_EILUČIŲ_SKAIČIUS,NARELIO_PLOTIS,NARELIO_AUKŠTIS)
    global x,y
    # BEGIN_RODYTI
    nupiešti_narelį(x,y)
    x=x+1
    # END_RODYTI

    