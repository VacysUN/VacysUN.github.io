from p5 import *
from gyvate import * 
from bendri import * 
import random


x=9
y=12
stulpelių_kryptis = 1
eilučių_kryptis = 0
 # BEGIN_RODYTI
x_maistas = random.randint(1, 20)
y_maistas = random.randint(1, 20)
# END_RODYTI

def setup():
    createCanvas(EKRANO_PLOTIS, EKRANO_AUKŠTIS)

def draw():
    klavišas = key
    background(255)
    frameRate(5)
    nupiešti_tinklelį(TINKLELIO_STULPELIŲ_SKAIČIUS,TINKLELIO_EILUČIŲ_SKAIČIUS,NARELIO_PLOTIS,NARELIO_AUKŠTIS)
    global x,y,stulpelių_kryptis,eilučių_kryptis,x_maistas,y_maistas
    # BEGIN_RODYTI
    nupiešti_maistą(x_maistas,y_maistas)
    nupiešti_narelį(x,y)
    

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
    x=x+stulpelių_kryptis
    y=y+eilučių_kryptis






    