from p5 import *


EKRANO_PLOTIS = 400
EKRANO_AUKSTIS = 400
TINKLELIO_STULPELIU_SKAICIUS = 20
TINKLELIO_EILUCIU_SKAICIUS = 20
NARELIO_PLOTIS = EKRANO_PLOTIS /TINKLELIO_STULPELIU_SKAICIUS
NARELIO_AUKSTIS = EKRANO_AUKSTIS /TINKLELIO_EILUCIU_SKAICIUS
# BEGIN_RODYTI
xs = [11, 10, 9]
ys = [12, 12, 12]
# END_RODYTI

def nupiesti_nareli(x, y):
    fill(161,114,4)
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

def setup():
    createCanvas(EKRANO_PLOTIS+NARELIO_PLOTIS, EKRANO_AUKSTIS+NARELIO_AUKSTIS)

def draw():
    frameRate(5)
    nupiesti_tinkleli(TINKLELIO_STULPELIU_SKAICIUS,TINKLELIO_EILUCIU_SKAICIUS,NARELIO_PLOTIS,NARELIO_AUKSTIS)
    global xs,ys
    # BEGIN_RODYTI
    # Pabandykite padaryti, kad gyvatėlės padėti būtų vertikali ir ji judėtų žemyn
    nupiesti_nareli(xs[0],ys[0])
    nupiesti_nareli(xs[1],ys[1])
    nupiesti_nareli(xs[2],ys[2])
    xs[2] = xs[1]
    xs[1] = xs[0]
    xs[0] = xs[0] + 1
    # END_RODYTI

    
