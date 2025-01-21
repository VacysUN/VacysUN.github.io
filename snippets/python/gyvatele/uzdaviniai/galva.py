from p5 import *
from gyvate import * 
from gyvate import nupiešti_narelį  as nupiešti_narelį_orginalas
import scoring

x_expected=15
y_expected=5
frame_count = 0

def nupiešti_narelį(x, y):
    global frame_count
    nupiešti_narelį_orginalas(x, y)
    frame_count = frame_count + 1
    if frame_count == 3:
        if x>=x_expected and x<=20 and y<=y_expected and y>=1:
            scoring.score("galva", 1, 1)
            fill(143, 206, 44)
            textSize(NARELIO_AUKŠTIS * 2)                
            text("Teisingai", NARELIO_PLOTIS * 6, NARELIO_AUKŠTIS * 6)
        else:
            scoring.score("galva", 0, 1)
            fill(249, 65, 61)
            textSize(NARELIO_AUKŠTIS * 2)                
            text("Neteisingai", NARELIO_PLOTIS * 6, NARELIO_AUKŠTIS * 6)
        noLoop()       




def setup():
    createCanvas(EKRANO_PLOTIS, EKRANO_AUKŠTIS)

def draw():
    background(255)
    frameRate(5)
    nupiešti_tinklelį(TINKLELIO_STULPELIŲ_SKAIČIUS,TINKLELIO_EILUČIŲ_SKAIČIUS,NARELIO_PLOTIS,NARELIO_AUKŠTIS)

    noFill()
    stroke('green')
    strokeWeight(4)
    rect(
        NARELIO_PLOTIS * 15,
        NARELIO_AUKŠTIS ,
        NARELIO_PLOTIS*6,
        NARELIO_AUKŠTIS*5,
    )

    stroke(72, 72, 72)
    strokeWeight(1)
    # BEGIN_RODYTI
    nupiešti_narelį(10,12)
    # END_RODYTI

    