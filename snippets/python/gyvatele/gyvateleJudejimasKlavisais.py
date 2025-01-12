from p5 import *
from gyvate import * 

# BEGIN_RODYTI
x=9
y=12
stulpelių_kryptis = 0 
eilučių_kryptis = 0
# END_RODYTI


def setup():
    createCanvas(EKRANO_PLOTIS, EKRANO_AUKŠTIS)

def draw():
    klavišas = key
    background(255)
    frameRate(5)
    nupiešti_tinklelį(TINKLELIO_STULPELIŲ_SKAIČIUS,TINKLELIO_EILUČIŲ_SKAIČIUS,NARELIO_PLOTIS,NARELIO_AUKŠTIS)
    global x,y,stulpelių_kryptis,eilučių_kryptis
    # BEGIN_RODYTI
    nupiešti_narelį(x,y)
    if klavišas == "a":
      stulpelių_kryptis = -1
      eilučių_kryptis = 0
    elif klavišas == "d":
      stulpelių_kryptis = 1
      eilučių_kryptis = 0
    elif klavišas == "w":
      stulpelių_kryptis = 0
      eilučių_kryptis = -1
    elif klavišas == "s":
      stulpelių_kryptis = 0
      eilučių_kryptis = 1
    x=x+stulpelių_kryptis
    y=y+eilučių_kryptis
    # END_RODYTI

    