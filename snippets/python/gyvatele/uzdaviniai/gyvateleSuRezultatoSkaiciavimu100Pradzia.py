from p5 import *
from gyvate import * 
from bendri import * 
import random
import scoring



x=9
y=12
stulpelių_kryptis = 1
eilučių_kryptis = 0
 # BEGIN_RODYTI
x_maistas = random.randint(1, 20)
y_maistas = random.randint(1, 20)
rezultatas=0
# END_RODYTI
rezultatas_tikimasi=100
patikra_baigta= False
teisingai= False


def check():
    global patikra_baigta,teisingai

    if patikra_baigta==False:
      if rezultatas==rezultatas_tikimasi:
        scoring.score("suRezultatoSkaiciavimu100Pradzia", 1, 1)
        teisingai= True
        fill(143, 206, 44)
        textSize(NARELIO_AUKŠTIS * 2)                
        text("Teisingai", NARELIO_PLOTIS * 6, NARELIO_AUKŠTIS * 6)
      else:
          scoring.score("suRezultatoSkaiciavimu100Pradzia", 0, 1)
          teisingai= False
          fill(249, 65, 61)
          textSize(NARELIO_AUKŠTIS * 2)                
          text("Neteisingai", NARELIO_PLOTIS * 6, NARELIO_AUKŠTIS * 6)
      patikra_baigta=True
    else:
      if teisingai==True:
        fill(143, 206, 44)
        textSize(NARELIO_AUKŠTIS * 2)                
        text("Teisingai", NARELIO_PLOTIS * 6, NARELIO_AUKŠTIS * 6)
      else:
        fill(249, 65, 61)
        textSize(NARELIO_AUKŠTIS * 2)                
        text("Neteisingai", NARELIO_PLOTIS * 6, NARELIO_AUKŠTIS * 6)

         


def setup():
    createCanvas(EKRANO_PLOTIS, EKRANO_AUKŠTIS)

def draw():
    klavišas = key
    background(255)
    frameRate(5)
    nupiešti_tinklelį(TINKLELIO_STULPELIŲ_SKAIČIUS,TINKLELIO_EILUČIŲ_SKAIČIUS,NARELIO_PLOTIS,NARELIO_AUKŠTIS)
    global x,y,stulpelių_kryptis,eilučių_kryptis,x_maistas,y_maistas,rezultatas
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


    # BEGIN_RODYTI
    if x==x_maistas and y==y_maistas:
      rezultatas+= 1
      x_maistas = random.randint(1, 20)
      y_maistas = random.randint(1, 20)
    # END_RODYTI
    rodyti_rezultatą(rezultatas)
    check()





    