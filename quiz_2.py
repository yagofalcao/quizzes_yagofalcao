def valor(n):
    notas = [100.00, 50.00, 20.00, 10.00, 5.00, 1.00, 0.50, 0.25, 0.10, 0.5, 0.01]
    notas.sort()
    notas.reverse()
    numNotas = []
    for i in notas:
        if n/i == 0:
            numNotas.append(n/i)
        if n/i < 0:
            pass
        if n/i > 0:
            numNotas.append(n/i)
            n %= i
    for i in range(len(notas)):
        print (notas[i], numNotas[i])
        
valor(150)

"""
A classe bola representa uma esfera cheia de agua (com peso 1000g por metro cubico) com um raio r 
e superfice coberta com tinta ou azul (peso 1g por metro quadrado) ou amarelo (2g por metro quadrado) 
ou vermelho (3g por cm quadrado), o paramatro da classe é uma tupla (r, cor),
a funcao da classe "peso" de deve retorna o peso total em kg da bola,
Obs: volume da espera = (4/3)*pi*(r**3), area da superfice = 4*pi*(r**2)
Ex: bola((2, "vermelho")).peso -> 33.66012533333334
    bola((3, "azul")).peso     -> 113.20709400000001
"""
class bola:
    def __init__(self, tamanho,cor):
        self.tamanho = tamanho
        self.cor = "azul" or "amarelo" or "vermelho"
pi = 3.14159
