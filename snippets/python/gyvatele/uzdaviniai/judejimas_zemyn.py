from p5 import *
from gyvate import *
import scoring

# BEGIN_RODYTI
x = 9
y = 12
# END_RODYTI


frame_count = 0
coords = []


def check():
    global frame_count
    global y
    coords.append(y)
    frame_count = frame_count + 1
    if frame_count == 5:
        correct = True
        for y1, y2 in zip(coords[:-1], coords[1:]):
            if (y1 + 1) != y2:
                correct = False
                break
        if correct:
            scoring.score("judejimasZemyn", 1, 1)
            fill(143, 206, 44)
            textSize(NARELIO_AUKŠTIS * 2)                
            text("Teisingai", NARELIO_PLOTIS * 6, NARELIO_AUKŠTIS * 6)
        else:
            scoring.score("judejimasZemyn", 0, 1)
            fill(249, 65, 61)
            textSize(NARELIO_AUKŠTIS * 2)                
            text("Neteisingai", NARELIO_PLOTIS * 6, NARELIO_AUKŠTIS * 6)
        noLoop()


def setup():
    createCanvas(EKRANO_PLOTIS, EKRANO_AUKŠTIS)


def draw():
    background(255)
    frameRate(5)
    nupiešti_tinklelį(
        TINKLELIO_STULPELIŲ_SKAIČIUS,
        TINKLELIO_EILUČIŲ_SKAIČIUS,
        NARELIO_PLOTIS,
        NARELIO_AUKŠTIS,
    )
    global x, y
    # BEGIN_RODYTI
    nupiešti_narelį(x, y)
    x = x + 1
    # END_RODYTI
    check()
