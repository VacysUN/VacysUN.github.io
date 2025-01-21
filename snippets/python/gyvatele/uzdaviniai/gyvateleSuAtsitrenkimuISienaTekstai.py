from p5 import *
from gyvate import * 
from bendri import * 
import scoring

x=3
y=3
stulpelių_kryptis = -1
eilučių_kryptis = 0
x_spalva_tikimasi='žalia'
x_pabaigos_tekstas_tikimasi='Stulpelių užribis'
y_spalva_tikimasi='raudona'
y_pabaigos_tekstas_tikimasi='Eilučių užribis'
spalva_is_parametro=''
pabaigos_tekstas_is_parametro=''

def stabdyti_žaidimą(spalva, pabaigos_tekstas):
    global spalva_is_parametro, pabaigos_tekstas_is_parametro
    spalva_is_parametro=spalva
    pabaigos_tekstas_is_parametro=pabaigos_tekstas
    fill(spalvos.get(spalva, "black"))
    textSize(40)
    textAlign(CENTER, CENTER)
    text(
        pabaigos_tekstas,
        EKRANO_PLOTIS / 2 + NARELIO_PLOTIS,
        EKRANO_AUKŠTIS / 2 - NARELIO_AUKŠTIS
    )


def check():   
    global x,y,stulpelių_kryptis,eilučių_kryptis
    #tinkinam ar gerai kai iseina is lentos stulpelyje 0
    if x < -1:
      if spalva_is_parametro==x_spalva_tikimasi and pabaigos_tekstas_is_parametro==x_pabaigos_tekstas_tikimasi:
        scoring.score("atsitrenkimuISienaTekstai", 1, 4)
        fill(143, 206, 44)
        textSize(NARELIO_AUKŠTIS * 2)                
        text("Teisingai 1/4", NARELIO_PLOTIS * 8, NARELIO_AUKŠTIS * 6)
      else:
        scoring.score("atsitrenkimuISienaTekstai", 1, 4)
        fill(249, 65, 61)
        textSize(NARELIO_AUKŠTIS * 2)                
        text("Neteisingai", NARELIO_PLOTIS * 8, NARELIO_AUKŠTIS * 6)
        noLoop()
      x=16
      y=3
      stulpelių_kryptis = 1
      eilučių_kryptis = 0
    #tinkinam ar gerai kai iseina is lentos eiluteje 0
    if x > 21 :
      if spalva_is_parametro==x_spalva_tikimasi and pabaigos_tekstas_is_parametro==x_pabaigos_tekstas_tikimasi:
        scoring.score("atsitrenkimuISienaTekstai", 2, 4)
        fill(143, 206, 44)
        textSize(NARELIO_AUKŠTIS * 2)                
        text("Teisingai 2/4", NARELIO_PLOTIS * 8, NARELIO_AUKŠTIS * 6)
      else:
        scoring.score("atsitrenkimuISienaTekstai", 1, 4)
        fill(249, 65, 61)
        textSize(NARELIO_AUKŠTIS * 2)                
        text("Neteisingai", NARELIO_PLOTIS * 8, NARELIO_AUKŠTIS * 6)
        noLoop()
      x=16
      y=3
      stulpelių_kryptis = 0
      eilučių_kryptis = -1
    #tinkinam ar gerai kai iseina is lentos eiluteje 20
    if y < -1 :
      if spalva_is_parametro==y_spalva_tikimasi and pabaigos_tekstas_is_parametro==y_pabaigos_tekstas_tikimasi:
        scoring.score("atsitrenkimuISienaTekstai", 3, 4)
        fill(143, 206, 44)
        textSize(NARELIO_AUKŠTIS * 2)                
        text("Teisingai 3/4", NARELIO_PLOTIS * 8, NARELIO_AUKŠTIS * 6)
      else:
        scoring.score("atsitrenkimuISienaTekstai", 2, 4)
        fill(249, 65, 61)
        textSize(NARELIO_AUKŠTIS * 2)                
        text("Neteisingai", NARELIO_PLOTIS * 8, NARELIO_AUKŠTIS * 6)
        noLoop()
      x=16
      y=18
      stulpelių_kryptis = 0
      eilučių_kryptis = 1
    if y > 21 :
      if spalva_is_parametro==y_spalva_tikimasi and pabaigos_tekstas_is_parametro==y_pabaigos_tekstas_tikimasi:
        scoring.score("atsitrenkimuISienaTekstai", 4, 4)
        fill(143, 206, 44)
        textSize(NARELIO_AUKŠTIS * 2)                
        text("Teisingai 4/4", NARELIO_PLOTIS * 8, NARELIO_AUKŠTIS * 6)
      else:
        scoring.score("atsitrenkimuISienaTekstai", 3, 4)
        fill(249, 65, 61)
        textSize(NARELIO_AUKŠTIS * 2)                
        text("Neteisingai", NARELIO_PLOTIS * 8, NARELIO_AUKŠTIS * 6)
      noLoop()
  

def setup():
    createCanvas(EKRANO_PLOTIS, EKRANO_AUKŠTIS)

def draw():
    klavišas = key
    background(255)
    frameRate(5)
    nupiešti_tinklelį(TINKLELIO_STULPELIŲ_SKAIČIUS,TINKLELIO_EILUČIŲ_SKAIČIUS,NARELIO_PLOTIS,NARELIO_AUKŠTIS)
    global x,y,stulpelių_kryptis,eilučių_kryptis,frame_count 
    # BEGIN_RODYTI
    nupiešti_narelį(x,y)

    if (x < 1 or x > 20 ) or (y < 1 or  y > 20):
        stabdyti_žaidimą('mėlyna','Pabandyk dar kartą!')
      
    # END_RODYTI



    #   stulpelių_kryptis = 1
    #   eilučių_kryptis = 0
    # if klavišas == 'a' and stulpelių_kryptis !=1:
    #   stulpelių_kryptis = -1
    #   eilučių_kryptis = 0
    # elif klavišas == 'd' and stulpelių_kryptis !=-1:
    #   stulpelių_kryptis = 1
    #   eilučių_kryptis = 0
    # elif klavišas == 'w'and eilučių_kryptis !=1 :
    #   stulpelių_kryptis = 0
    #   eilučių_kryptis = -1
    # elif klavišas == 's' and eilučių_kryptis !=-1:
    #   stulpelių_kryptis = 0
    #   eilučių_kryptis = 1

    
    x=x+stulpelių_kryptis
    y=y+eilučių_kryptis
    check()





    