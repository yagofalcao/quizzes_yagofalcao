#FINAL - CONTANDO CEDULAS

def numero(x):

    notas = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.25, 0.10, 0.5, 0.01]
    #Coloquei para ler cada nota
    for i in range(len(notas)):
        #salvei em a o valor do numero divido pela nota
        a = x/notas[i]    
        if int(a)>0:
            print (int(a), 'nota(s) de', notas[i])
        x -= notas[i]*int(a)  
        i += 1
        
numero(275.50)


"""
A classe bola representa uma esfera cheia de agua (com peso 1000g por metro cubico) com um raio r 
e superfice coberta com tinta ou azul (peso 1g por metro quadrado) ou amarelo (2g por metro quadrado) 
ou vermelho (3g por cm quadrado), o paramatro da classe é uma tupla (r, cor),
a funcao da classe "peso" de deve retorna o peso total em kg da bola,
Obs: volume da espera = (4/3)*pi*(r**3), area da superfice = 4*pi*(r**2)
Ex: bola((2, "vermelho")).peso -> 33.66012533333334
    bola((3, "azul")).peso     -> 113.20709400000001
"""

#BOLA

class bola:
   
    def __init__(self,r,cor):
        self.r = r
        self.cor = cor
        
    def peso(self):
        pi = 3.14159
        
        if self.cor == "azul" or "Azul":
            x = 1
        if self.cor == "amarelo" or "Amarelo":
            x = 2
        if self.cor == "vermelho" or "Vermelho":
            x = 3
        else:
            print("Você deve escolher as cores: azul, amarelo ou vermelho")
            
        #V = volume da esfera
        V = (4/3)*pi*(self.r**3)
        
        #kg por m³
        
        #AS = Área da Superfície
        AS = 4*pi*(self.r**2)
        
        peso = V + AS*x
        
        return peso

bola_x = bola(5,"vermelho")
bola_x.peso()
