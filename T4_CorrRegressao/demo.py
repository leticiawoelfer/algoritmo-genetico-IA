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
    return r;

    
def regressao(x, y, r):
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
    linhaRegressao(b0, b1, x, y, r)
    
    
def linhaRegressao(b0, b1, x, y, r):
    resultados=[]
    for num in x:
        resultados.append(b0 + (b1 * num))
    geraGrafico(b0, b1, x, y, r, resultados)

def geraGrafico(b0, b1, x, y, r, resultados):
    plt.scatter(x, y)
    plt.plot(x,resultados)
    plt.title("Correlação:"+str(r)+"  B0:"+str(b0)+"  B1:"+str(b1))
    plt.figure()

def dataset1():
    x1 = [10,8,13,9,11,14,6,4,12,7,5]
    y1 = [8.04,6.95,7.58,8.81,8.33,9.96,7.24,4.26,10.84,4.82,5.68]
    print("Dataset 1")
    r = correlacao(x1, y1)
    regressao(x1, y1, r)

def dataset2():
    x2 = [10,8,13,9,11,14,6,4,12,7,5]
    y2 = [9.14,8.14,8.47,8.77,9.26,8.10,6.13,3.10,9.13,7.26,4.74]
    print("Dataset 2")
    r = correlacao(x2, y2)
    regressao(x2, y2, r)

def dataset3():
    x3 = [8,8,8,8,8,8,8,8,8,8,19]
    y3 = [6.58,5.76,7.71,8.84,8.47,7.04,5.25,5.56,7.91,6.89,12.50]
    print("Dataset 3")
    r = correlacao(x3, y3)
    regressao(x3, y3, r)

dataset1()
dataset2()
dataset3()

"""
3) Qual dos datasets não é apropriado para regressão linear?
    dataset 3, porque o valor da variável dependente não cresce
    em relação a variável independente.
"""


