from p5 import *
from gyvate import *
import scoring

# BEGIN_RODYTI
x=9
y=12
stulpelių_kryptis = 1 
eilučių_kryptis = 0
# END_RODYTI

frame_count = 0
coords = []

def check():
    global frame_count
    global x, y
    if key == "p":
      coords.append((x, y))
      frame_count = frame_count + 1
      if frame_count == 3:
          correct = True
          for (x1, y1), (x2, y2) in zip(coords[:-1], coords[1:]):
              if (x1, y1 ) != (x2, y2):
                  correct = False
                  break
          if correct:
              scoring.score("beJundėjimoAtgalPauze", 1, 1)
              fill(143, 206, 44)
              textSize(NARELIO_AUKŠTIS * 2)                
              text("Teisingai", NARELIO_PLOTIS * 6, NARELIO_AUKŠTIS * 6)
          else:
              scoring.score("beJundėjimoAtgalPauze", 0, 1)
              fill(249, 65, 61)
              textSize(NARELIO_AUKŠTIS * 2)                
              text("Neteisingai", NARELIO_PLOTIS * 6, NARELIO_AUKŠTIS * 6)
          noLoop()

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
    if klavišas == "a" and stulpelių_kryptis !=1:
      stulpelių_kryptis = -1
      eilučių_kryptis = 0
    elif klavišas == "d":
      stulpelių_kryptis = 1
      eilučių_kryptis = 0
    elif klavišas == "w":
      stulpelių_kryptis = 0
      eilučių_kryptis = -1
    elif klavišas == "s" and eilučių_kryptis !=-1:
      stulpelių_kryptis = 0
      eilučių_kryptis = 1
    x=x+stulpelių_kryptis
    y=y+eilučių_kryptis
    # END_RODYTI
    check()


    