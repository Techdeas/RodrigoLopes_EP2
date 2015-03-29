# Rodrigo Lopes Catto --- Design de Software
'''
    Projeto #2   Jogo da Forca
    
O programa constitui em um jogo da forca utilizando 
o turtle, uma ferramenta grafica. Assim o programa 
ira localizar uma lista com palavras, decodifica-las, 
e sortear uma palavra para ser decifrada pelo usuario.
Por meio de inputs o programa verifica se a letra inserida 
esta ou nao na palavra.      '''

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
