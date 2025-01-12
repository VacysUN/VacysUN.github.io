from p5 import *
from gyvate import * 


def setup():
    createCanvas(EKRANO_PLOTIS, EKRANO_AUKŠTIS)

def draw():
    background(255)
    nupiešti_tinklelį(TINKLELIO_STULPELIŲ_SKAIČIUS,TINKLELIO_EILUČIŲ_SKAIČIUS,NARELIO_PLOTIS,NARELIO_AUKŠTIS)
    # BEGIN_RODYTI
    # Nupiešime gyvatėlės galvą 10 stulpelyje, 5 eilutėje
    nupiešti_narelį(10,5)
    # END_RODYTI

    