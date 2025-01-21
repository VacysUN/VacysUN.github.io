from p5 import *
from gyvate import * 
from bendri import * 
import random
import scoring


x=3
y=3
stulpelių_kryptis = 1
eilučių_kryptis = 0
a_expected=10
b_expected=15
correct = False

def check():
    if correct:
      scoring.score("suMaistuDesinysKampas", 1, 1)
      fill(143, 206, 44)
      textSize(NARELIO_AUKŠTIS * 2)                
      text("Teisingai", NARELIO_PLOTIS * 6, NARELIO_AUKŠTIS * 6)      
    else:
      scoring.score("suMaistuDesinysKampas", 0, 1)
      fill(249, 65, 61)
      textSize(NARELIO_AUKŠTIS * 2)                
      text("Neteisingai", NARELIO_PLOTIS * 6, NARELIO_AUKŠTIS * 6)
    noLoop()  


original_randint = random.randint
def randint(a, b):
    global correct
    if a==a_expected and b==b_expected:
      correct = True
    else:
      correct = False
    return original_randint(a , b )

random.randint = randint
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

    noFill()
    stroke('green')
    strokeWeight(4)
    rect(
        NARELIO_PLOTIS * 10,
        NARELIO_AUKŠTIS * 10 ,
        NARELIO_PLOTIS * 6,
        NARELIO_AUKŠTIS * 6,
    )
    stroke(72, 72, 72)
    strokeWeight(1)


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

    check()


    