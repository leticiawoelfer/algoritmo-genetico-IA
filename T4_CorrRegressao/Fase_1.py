# -*- coding: utf-8 -*-
"""
Created on Wed May 29 21:28:29 2019

@authors: Douglas, Joana e Leticia
"""
import matplotlib.pyplot as plt
import math

def correlacao(x, y):
    n = len(x)
    somax = 0
    for numX in x:
        somax = somax + numX
    mediaX = somax / n
    
    somay = 0
    for numY in y:
        somay = somay + numY
    mediaY = somay / n
    
    somaR1 = 0
    somaMediaX = 0
    somaMediaY = 0
    for i in range(0,n):
        somaR1 = somaR1 + ((x[i] - mediaX) * (y[i] - mediaY))
        somaMediaX = somaMediaX + ((x[i] - mediaX)**2)
        somaMediaY = somaMediaY + ((y[i] - mediaY)**2)
        
    raizQuad = math.sqrt(somaMediaX * somaMediaY)
    
    r = round((somaR1/raizQuad),4)
    print("r="+str(r))
    return r;

    
def regressao(x, y):
    n = len(x)
    somax = 0
    for numX in x:
        somax = somax + numX
    mediaX = somax / n
    
    somay = 0
    for numY in y:
        somay = somay + numY
    mediaY = somay / n
    
    soma1 = 0
    soma2 = 0
    for i in range(0,n):
        soma1 = soma1 + ((x[i] - mediaX) * (y[i] - mediaY))
        soma2 = soma2 + ((x[i] - mediaX)**2)
    
    b1 = round((soma1 / soma2),4)
    b0 = round((mediaY - (b1 * mediaX)),4)
    print("B0="+str(b0))
    print("B1="+str(b1))
    linhaRegressao(b0, b1, x)
    
def graficoDispersao(x, y):
    plt.scatter(x, y)
    
def linhaRegressao(b0, b1, x):
    resultados=[]
    #resultados.append(0)
    for num in x:
        resultados.append(b0 + (b1 * num))
    print(resultados)
    resultados = sorted(resultados)
    print(resultados)
    fim = round(((resultados[len(resultados)-1])+1),0)
    print(fim)
    resultados.append(fim)
    print(resultados)
    plt.plot(resultados)
    


def dataset1():
    x1 = [10,8,13,9,11,14,6,4,12,7,5]
    y1 = [8.04,6.95,7.58,8.81,8.33,9.96,7.24,4.26,10.84,4.82,5.68]
    graficoDispersao(x1,y1)
    print("Dados 1")
    r = correlacao(x1,y1)
    regressao(x1, y1)
    


dataset1()

"""
x2 = [10,8,13,9,11,14,6,4,12,7,5]
y2 = [9.14,8.14,8.47,8.77,9.26,8.10,6.13,3.10,9.13,7.26,4.74]
print("Dados 2")
correlacao(x2,y2)
regressao(x2,y2)

x3 = [8,8,8,8,8,8,8,8,8,8,19]
y3 = [6.58,5.76,7.71,8.84,8.47,7.04,5.25,5.56,7.91,6.89,12.50]
print("Dados 3")
correlacao(x3,y3)
regressao(x3,y3)
"""




