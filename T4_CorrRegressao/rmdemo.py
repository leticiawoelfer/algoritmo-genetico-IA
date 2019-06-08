# -*- coding: utf-8 -*-
"""
@authors: Douglas, Joana e Leticia
"""
import matplotlib.pyplot as plt
import math
import csv
import numpy as np

def lerArquivo():
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:            
            vetorPreco.append(float(row[2]))
            del row[2]
            row = [int(x) for x in row]
            row.insert(0, 1)
            matrizX.append(row)

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

def preparaLista(posicao, lista):
    for i in range(0, (len(matrizX)-1)):
        lista.append(int(matrizX[i][posicao]))

def geraMatrizTransposta():
    for i in range(0, 3):
        linha = []
        for j in range(0, len(matrizX)):
            linha.append(matrizX[j][i])
        matrizXTrans.append(linha)
    print(matrizXTrans)
    
def calcularB():
    a = np.dot(matrizX, matrizXTrans)
    b = np.linalg.inv(a)
    c = np.dot(vetorPreco,matrizXTrans)

    print(b*c)
    
def calcularLinhaRegr():
    pass
#def regressao(x, y, r):

matrizX = []
vetorPreco = []
lerArquivo()

#prepara a lista para fazer a correlacao e regressao linear
tamCasa = []
preparaLista(1, tamCasa)    
corr1 = correlacao(tamCasa, vetorPreco)
print("Correlação Tamanho da casa e Preço: "+str(corr1))
#regr = regressao


#prepara a lista para fazer a correlacao e regressao linear
numQuarts = []
preparaLista(2, numQuarts)
corr2 = correlacao(numQuarts, vetorPreco)
print("Correlação Número de quartos e Preço: "+str(corr2))


matrizXTrans = []
geraMatrizTransposta()

calcularB()

calcularLinhaRegr()





