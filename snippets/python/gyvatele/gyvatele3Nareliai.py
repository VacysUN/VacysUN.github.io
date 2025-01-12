from p5 import *
from gyvate import * 
from bendri import * 
import random

# BEGIN_RODYTI
x=11; y=12
x2=10; y2=12
x3=9; y3=12
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
    global x,y,stulpelių_kryptis,eilučių_kryptis,x_maistas,y_maistas,rezultatas,x2,y2,x3,y3,x4,y4

    nupiešti_maistą(x_maistas,y_maistas)
    # BEGIN_RODYTI
    nupiešti_narelį(x,y)
    nupiešti_narelį(x2,y2)
    nupiešti_narelį(x3,y3)
    # END_RODYTI
    if (x < 1 or x > 20 ) or (y < 1 or  y > 20):
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
    x3 = x2
    y3 = y2

    x2 = x
    y2 = y
    
    x=x+stulpelių_kryptis
    y=y+eilučių_kryptis
    # END_RODYTI      

    if x==x_maistas and y==y_maistas:
      rezultatas+= 1
      x_maistas = random.randint(1, 20)
      y_maistas = random.randint(1, 20)

    rodyti_rezultatą(rezultatas)






    