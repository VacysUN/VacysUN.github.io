from p5 import *
from bendri import *


EKRANO_PLOTIS = 200
EKRANO_AUKSTIS = 200

pelėsX = 0
pelėsY = 0


def setup():
    createCanvas(EKRANO_PLOTIS, EKRANO_AUKSTIS)
    rectMode(CORNER)


def horizontali_linija(y):
    piešk_liniją(0, y, EKRANO_PLOTIS, y)


def vertikali_linija(x):
    piešk_liniją(x, 0, x, EKRANO_AUKSTIS)


def draw():
    background(spalvos.get("šviesiai pilkšva", "black"))
    stroke(spalvos["tamsiai pilkšva"])
    # BEGIN_RODYTI
    # linijas piešime su 40 pikselių tarpais
    for i in range(5):
        horizontali_linija(20 + 40 * i)

    for i in range(5):
        vertikali_linija(20 + 40 * i)
    # END_RODYTI
