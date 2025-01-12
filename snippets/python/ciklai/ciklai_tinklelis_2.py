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
    horizontali_linija(20)
    horizontali_linija(20 + 20)
    horizontali_linija(20 + 20 * 2)
    horizontali_linija(20 + 20 * 3)
    horizontali_linija(20 + 20 * 4)
    horizontali_linija(20 + 20 * 5)
    horizontali_linija(20 + 20 * 6)
    horizontali_linija(20 + 20 * 7)
    horizontali_linija(20 + 20 * 8)

    vertikali_linija(20)
    vertikali_linija(20 + 20)
    vertikali_linija(20 + 20 * 2)
    vertikali_linija(20 + 20 * 3)
    vertikali_linija(20 + 20 * 4)
    vertikali_linija(20 + 20 * 5)
    vertikali_linija(20 + 20 * 6)
    vertikali_linija(20 + 20 * 7)
    vertikali_linija(20 + 20 * 8)
    # END_RODYTI
