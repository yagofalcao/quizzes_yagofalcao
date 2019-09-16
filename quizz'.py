import math
import numpy as np

"""
Dado um valor (float com 2 casas decimais), retorne a quantidade de 
notas ou moedas ([100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.25, 0.10, 0.5, 0.01]) 
mínimo para pagar esse valo"

Ex: quantidade(576.73) -> 15 (5 de 100.00, 1 de 50.00, 1 de 20.00, 1 de 5.00, 1 de 1.00, 
                                1 de 0.50, 2 de 0.10 e 3 de 0.01)
    quantidade(4.00) -> 4 (4 de 1.00)
"""


def quantidade(n):
    l=[]
    c=[]
    for a in [100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.25, 0.10, 0.5, 0.01]:
        if n >= a:
            q = n/a
            m = q%1
            q = q-m
            n = n-q*a
            l.append(q)
            c.append([a]*int(q))

        else:
            pass
    m=sum(l)
    print(m)
    print(c)




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
    def __init__(self,t):
        self.raio = t[0]
        self.cor = t[1]
        self.pi = 3.14159
    def peso(self):
        if   self.cor == 'amarelo':
            return (4/3)*self.pi*(self.raio**3)*1+4*self.pi*(self.raio**2)*0.002
        elif self.cor == 'vermelho':
            return (4/3)*self.pi*(self.raio**3)*1+4*self.pi*(self.raio**2)*0.003
        elif self.cor == 'azul':
            return (4/3)*self.pi*(self.raio**3)*1+4*self.pi*(self.raio**2)*0.001
"""
Dado um array (numpy) n x m com n >= 3 e m >= 3, qualquer A[i,j] != 0,
a funcao borda deve tornar a soma de todos os valores
da borda do array divido pelo produto de todos os valores interiores

Ex: borda(np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],   -> borda = [1,2,3,4,5,8,9,2,3,4,5,6] -> retorno = 1.2380952380952381
                    [9, 1, 1, 2],      interior = [6,7,0,1]
                    [3, 4, 5, 6]]))

    borda(np.array([[2, 2, 2],
                    [2, 2, 2],   -> 8
                    [2, 2, 2]]))
"""


def borda(array):
    b=[]
    meio=[]
    s=array.shape
    for i in range(s[0]):
        for j in range(s[1]):
            if i==0 or i==(s[0]-1) or j==0 or j==(s[1]-1):
                b.append(array[i][j])
            else:
                meio.append(array[i][j])
    print(b)
    print()
    print(meio)
    print()
    print(sum(b)/np.prod(meio))
