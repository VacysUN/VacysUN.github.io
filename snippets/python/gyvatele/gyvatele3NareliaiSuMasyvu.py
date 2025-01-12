from p5 import *
from gyvate import * 
from bendri import * 
import random

# BEGIN_RODYTI
xs = [11, 10, 9]
ys = [12, 12, 12]
# END_RODYTI

stulpelių_kryptis = 1
eilučių_kryptis = 0
x_maistas = random.randint(1, 20)
y_maistas = random.randint(1, 20)
rezultatas=0

def setup():
    createCanvas(EKRANO_PLOTIS, EKRANO_AUKŠTIS)

def draw():
    klavišas = key
    background(255)
    frameRate(5)
    nupiešti_tinklelį(TINKLELIO_STULPELIŲ_SKAIČIUS,TINKLELIO_EILUČIŲ_SKAIČIUS,NARELIO_PLOTIS,NARELIO_AUKŠTIS)
    global xs,ys,stulpelių_kryptis,eilučių_kryptis,x_maistas,y_maistas,rezultatas

    nupiešti_maistą(x_maistas,y_maistas)
    # BEGIN_RODYTI
    nupiešti_narelį(xs[0],ys[0])
    nupiešti_narelį(xs[1],ys[1])
    nupiešti_narelį(xs[2],ys[2])
    # END_RODYTI
    if (xs[0] < 1 or xs[0] > 20 ) or (ys[0] < 1 or  ys[0] > 20):
        stabdyti_žaidimą('mėlyna','Pabandyk dar kartą!')
    

    if klavišas == 'a' and stulpelių_kryptis !=1:
      stulpelių_kryptis = -1
      eilučių_kryptis = 0
    elif klavišas == 'd' and stulpelių_kryptis !=-1:
      stulpelių_kryptis = 1
      eilučių_kryptis = 0
    elif klavišas == 'w'and eilučių_kryptis !=1 :
      stulpelių_kryptis = 0
      eilučių_kryptis = -1
    elif klavišas == 's' and eilučių_kryptis !=-1:
      stulpelių_kryptis = 0
      eilučių_kryptis = 1

    # BEGIN_RODYTI
    xs[2] = xs[1]
    ys[2] = ys[1]

    xs[1] = xs[0]
    ys[1] = ys[0]
    
    xs[0]=xs[0]+stulpelių_kryptis
    ys[0]=ys[0]+eilučių_kryptis
    # END_RODYTI      

    if xs[0]==x_maistas and ys[0]==y_maistas:
      rezultatas+= 1
      x_maistas = random.randint(1, 20)
      y_maistas = random.randint(1, 20)

    rodyti_rezultatą(rezultatas)






    