# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 19:29:06 2015
@author: Rodrigo
"""
#import time
import random
import turtle
from unicodedata import normalize
def formatar(txt):
   return normalize('NFKD', txt).encode('ASCII','ignore').decode('ASCII')
if __name__ == '__main__':
   from doctest import testmod
   testmod()
#------------------------------------------------------------------------------


ganhou = 0
letras = []
m = 0
n = 0  
erro = 0
i = 0



#------------------------------------------------------------------------------
#Desenho da forca:
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
# Erros da forca:
def erros(erro):
    lin   = turtle.Turtle() 
    lin.hideturtle()
    if erro == 1:
        lin.penup()    
        lin.setpos(-200,160)
        lin.pendown()
        lin.circle(25)
        lin.hideturtle()
    if erro == 2:
        lin.penup()
        lin.left(270)
        lin.setpos(-200,160)
        lin.pendown()    
        lin.forward(100)
        lin.hideturtle()
    if erro == 3:
        
        lin.penup()
        lin.setpos(-200,130)
        lin.pendown()
        lin.right(45)
        lin.forward(50)
        lin.hideturtle()
    if erro == 4:
        lin.left(135)
        lin.penup()
        lin.setpos(-200,130)
        lin.pendown()
        lin.left(90)
        lin.forward(50)
        lin.hideturtle()
    if erro == 5:
        lin.right(35)
        lin.penup()
        lin.setpos(-200,60)
        lin.pendown()
        lin.left(270)
        lin.forward(50)
        lin.hideturtle()
    if erro == 6:
        lin.left(-135)
        lin.penup()
        lin.setpos(-200,60)
        lin.pendown()
        lin.right(270)
        lin.forward(50) 
        lin.hideturtle()
        lin.pu()
        lin.setpos(0,50)
        lin.pd()
        lin.color('red')
        lin.write('VOCE PERDEU', font=('Arial',15))
        media = len(letra)//len(formatado)
        lin.pu()
        lin.setpos(-100,-300)
        lin.pd()
        lin.write('Media:',font=('Arial',25))
        lin.pu()
        lin.setpos(0,-300)
        lin.pd()
        lin.write(media,font=('Arial',25))
        again = window.textinput("***Forca***","Para comtinuar digite 'sim' e para sair digite 'não':")
        global start            
        if again == 'sim':
            start = True
        else:
            start = False
#Desenho dos tracos:
def desenhar_tracos(): 

    while m < numLetras:
        z = palavras[m]
        if z != " ":
            lin.penup()    
            lin.setpos(-300+n,-200)
            lin.pendown()  
            lin.forward(25)
            global m
            global n
            m+=1
            n+=40
            lin.hideturtle()
        else:
            lin.penup()    
            lin.setpos(-300+n,-200)
            m+=1
            n+=40
            lin.hideturtle()
            global ganhou
            ganhou+=1
def placar():
    lin = turtle.Turtle() 
    lin.color('green')
    lin.pu()
    lin.setpos(25,150)
    lin.pd()
    lin.write('Placar:', font=('Arial',20))
    lin.pu()
    lin.setpos(100,100)
    lin.pd()
    lin.write('Acertos:', font=('Arial',15))
    lin.pu()
    lin.setpos(100,50)
    lin.pd()
    lin.write('Erros:', font=('Arial',15))
    lin.hideturtle()

#------------------------------------------------------------------------------
#Verifica a palavra! 
desenhar_forca()
start = True
placar()
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
    formatado = formatar(palavras).lower()    
    numLetras = len(formatado)
    limpa.remove(palavras)
    y = 0

         
    desenhar_tracos() 
    while ganhou < numLetras and erro != 6:
        letra = window.textinput("***Forca***", "Digite uma letra: OBS: Sem acento")
        letra = letra.lower()
        while letra in letras:
          letra = window.textinput("***Forca***", "Letra ja digitada! Faça outra escolha:")
          letra = letra.lower()
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
                   lin.pu()
                   lin.setpos(200+y,100)
                   lin.pd()
                   lin.write(ganhou, font=('Arial',15))
                   y+=10
           elif letra in formatado:
               i+=1
           else:
               erro +=1
               erros(erro)
               lin.pu()
               lin.setpos(200+y,50)
               lin.pd()
               lin.write(erro, font=('Arial',15))
               i=numLetras
               y+=10
               
    if ganhou == numLetras:          
        media = len(letra)//len(formatado)        
        lin.pu()
        lin.setpos(0,0)
        lin.pd()
        lin.write('PARABÉNS! VOCÊ GANHOU',align = 'center',font=('Arial',25))
        lin.pu()
        lin.setpos(-100,-300)
        lin.pd()
        lin.write('Media:',font=('Arial',25))
        lin.pu()
        lin.setpos(0,-300)
        lin.pd()
        lin.write(media,font=('Arial',25))
        again = window.textinput("***Forca***","Para comtinuar digite 'sim' e para sair digite 'nao':")
        if again == 'sim':
            start = True
            y=0
            i = 0
            m = 0
            n = 0
            ganhou = 0
            erro = 0
            letras = []
            lin.clear()
            
        else:
            start = False
            lin.clear()
            
            
window.exitonclick()

#------------------------------------------------------------------------------




    
   
       



    
    
    
    
    