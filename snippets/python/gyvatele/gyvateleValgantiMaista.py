from p5 import *
import random

EKRANO_PLOTIS = 400
EKRANO_AUKSTIS = 400
# BEGIN_RODYTI
TINKLELIO_STULPELIU_SKAICIUS = 20
TINKLELIO_EILUCIU_SKAICIUS = 20
# END_RODYTI
NARELIO_PLOTIS = EKRANO_PLOTIS /TINKLELIO_STULPELIU_SKAICIUS
NARELIO_AUKSTIS = EKRANO_AUKSTIS /TINKLELIO_EILUCIU_SKAICIUS
# BEGIN_RODYTI
xs = [11, 10, 9]
ys = [12, 12, 12]
stulpeliu_kryptis = 1 
eiluciu_kryptis = 0
x_maistas = random.randint(1, TINKLELIO_STULPELIU_SKAICIUS)
y_maistas = random.randint(1, TINKLELIO_EILUCIU_SKAICIUS)
# END_RODYTI

def nupiesti_nareli(x, y):
    fill(161,114,4)
    if (1 <= x <= TINKLELIO_STULPELIU_SKAICIUS ) and (1 <= y <= TINKLELIO_EILUCIU_SKAICIUS):
      rect(NARELIO_AUKSTIS * x
           ,NARELIO_PLOTIS * y
           ,NARELIO_AUKSTIS,
           NARELIO_PLOTIS)
def nupiesti_maista(x, y):
    fill(24,82,4)   
    if (1 <= x <= TINKLELIO_STULPELIU_SKAICIUS ) and (1 <= y <= TINKLELIO_EILUCIU_SKAICIUS):
      rect(NARELIO_AUKSTIS * x
           ,NARELIO_PLOTIS * y
           ,NARELIO_AUKSTIS,
           NARELIO_PLOTIS)
def nupiesti_tinkleli(cols,rows,rowWidth,rowHeight):

    textFont('Fibon Sans')
    
    for i in range(cols):
        fill(102, 102, 102)
        textAlign(CENTER, CENTER)
        textSize(NARELIO_AUKSTIS *0.6)
        text(i+1, (i+1)*NARELIO_PLOTIS+NARELIO_PLOTIS/2, NARELIO_AUKSTIS/2)

        # text(i+1, (i+1)*NARELIO_PLOTIS+NARELIO_PLOTIS/5, NARELIO_AUKSTIS/2)
        for j in range(rows):
          fill(62,62,62)
          stroke(72, 72, 72)
          rect(NARELIO_PLOTIS *i+NARELIO_PLOTIS
               ,NARELIO_AUKSTIS *j+NARELIO_AUKSTIS
               ,rowWidth
               ,rowHeight)
    for j in range(rows):
      fill(102, 102, 102)
      textAlign(CENTER, CENTER)
      textSize(NARELIO_AUKSTIS *0.6)
      text(j+1,NARELIO_PLOTIS/2, (j+1)*NARELIO_AUKSTIS+NARELIO_AUKSTIS/2)
# BEGIN_RODYTI
def keyPressed():
  global stulpeliu_kryptis,eiluciu_kryptis
  if key == "a":
    stulpeliu_kryptis = -1
    eiluciu_kryptis = 0
  elif key == "d":
    stulpeliu_kryptis = 1
    eiluciu_kryptis = 0
  elif key == "w":
    stulpeliu_kryptis = 0
    eiluciu_kryptis = -1
  elif key == "s":
    stulpeliu_kryptis = 0
    eiluciu_kryptis = 1
# END_RODYTI
def setup():
    createCanvas(EKRANO_PLOTIS+NARELIO_PLOTIS, EKRANO_AUKSTIS+NARELIO_AUKSTIS)

def draw():
    frameRate(5)
    nupiesti_tinkleli(TINKLELIO_STULPELIU_SKAICIUS,TINKLELIO_EILUCIU_SKAICIUS,NARELIO_PLOTIS,NARELIO_AUKSTIS)
    global xs,ys,x_maistas,y_maistas

    # Panadyk pakeisti, kad maistas negeruotųsi tik art 1 ir 10 stulpelio
    nupiesti_maista(x_maistas,y_maistas)
  
    # BEGIN_RODYTI
    for i in range(len(xs)):
        nupiesti_nareli(xs[i],ys[i])
  

    for j in range(len(xs)-1,0,-1):
        xs[j] = xs[j-1]
        ys[j] = ys[j-1]
        
    xs[0] = xs[0]+stulpeliu_kryptis
    ys[0] = ys[0]+eiluciu_kryptis

    if xs[0]==x_maistas and ys[0]==y_maistas:
      xs.append(xs[len(xs)-1])
      ys.append(ys[len(ys)-1])
      x_maistas = random.randint(1, TINKLELIO_STULPELIU_SKAICIUS)
      y_maistas = random.randint(1, TINKLELIO_EILUCIU_SKAICIUS)

    # END_RODYTI

    