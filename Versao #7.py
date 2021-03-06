# Rodrigo Lopes Catto --- Design de Software

import random
import turtle
from unicodedata import normalize       
def formatar(txt):
   return normalize('NFKD', txt).encode('ASCII','ignore').decode('ASCII')                                                
if __name__ == '__main__':
   from doctest import testmod
   testmod()
#------------------------------------------------------------------------------
   
   
p =open("entrada.txt",encoding="utf-8")
x = p.readlines()

limpa = []
for pa in x:
    y=pa.strip().lower()
    if y !="":
        limpa.append(y)
palavras = random.choice(limpa)
letras = []
formatado = formatar(palavras).lower()
    
def desenhar_forca():
        window = turtle.Screen()    
        window.bgcolor("lightblue")
        window.title("Jogo da Forca")
        lin   = turtle.Turtle() 
        lin.color("blue")
        lin.penup()
        lin.setpos(-150,-50)
        lin.pendown()
        lin.left(180)
        lin.forward(150)
        lin.right(90)
        lin.forward(300)
        lin.right(90)
        lin.forward(100)
        lin.right(90)
        lin.forward(40)
        lin.right(-90)
        
def erros(erro):
        lin   = turtle.Turtle() 
        if erro == 1:
            lin.penup()    
            lin.setpos(-200,160)
            lin.pendown()
            lin.circle(25)
        
        if erro == 2:
            lin.penup()
            lin.left(270)
            lin.setpos(-200,160)
            lin.pendown()    
            lin.forward(100)
            
        if erro == 3:
            lin.penup()
            lin.setpos(-200,130)
            lin.pendown()
            lin.right(45)
            lin.forward(50)
            
        if erro == 4:
            lin.penup()
            lin.setpos(-200,130)
            lin.pendown()
            lin.left(90)
            lin.forward(50)
            
        if erro == 5:
            lin.penup()
            lin.setpos(-200,60)
            lin.pendown()
            lin.left(270)
            lin.forward(50)
        if erro == 6:
            lin.penup()
            lin.setpos(-200,60)
            lin.pendown()
            lin.right(270)
            lin.forward(50) 
            lin.pu()
            lin.setpos(0,-300)
            lin.pd()
            lin.color('red')
            lin.write('VOCE PERDEU', font=('Arial',15))
            again = window.textinput("***Forca***","Para comtinuar digite 'sim' e para sair digite 'nao':")
            global start            
            if again == 'sim':
                start = True
            else:
                start = False
numLetras = len(formatado)
m = 0
n = 0             
#Desenho dos tracos:
def desenhar_tracos(): 

    while m < numLetras:
        lin.penup()    
        lin.setpos(-300+n,-200)
        lin.pendown()  
        lin.forward(25)
        global m
        global n
        m+=1
        n+=40
        lin.hideturtle()
        
        
        #Verifica a palavra! 
desenhar_forca()
start = True
while start == True:
    window = turtle.Screen()  
    lin   = turtle.Turtle() 
    p =open("entrada.txt",encoding="utf-8")
    x = p.readlines()

    limpa = []
    for pa in x:
        y=pa.strip().lower()
        if y !="":
            limpa.append(y)
    palavras = random.choice(limpa)
    palavras = palavras.replace(" ", "")
    formatado = formatar(palavras).lower()    
    numLetras = len(formatado)
    
    desenhar_tracos() 
    while ganhou < numLetras and erro != 6:
        letra = window.textinput("***Forca***", "Digite uma letra: OBS: Sem acento")
        while letra in letras:
          letra = window.textinput("***Forca***", "Letra ja digitada! Faça outra escolha:")  
        letras.append(letra)
        if i == numLetras and ganhou != numLetras:
            i=0
        while i < numLetras:
           b = formatado[i]
           if letra in formatado and b == letra:
                   lin.penup()
                   lin.setpos(-336+(40*(i+1)),-195)
                   lin.pendown()
                   lin.write(palavras[i],font=("Arial",15))
                   i+=1
                   ganhou+=1 
