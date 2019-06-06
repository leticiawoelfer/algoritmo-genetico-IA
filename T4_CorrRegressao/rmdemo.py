# -*- coding: utf-8 -*-
"""
@authors: Douglas, Joana e Leticia
"""
import matplotlib.pyplot as plt
import csv

def lerArquivo():
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            row.insert(0, 1)
            vetorPreco.append(row[3])
            del row[3]
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



matrizX = []
vetorPreco = []

lerArquivo()
#prepara a lista para fazer a correlacao e regressao linear
tamCasa = []
for i in range(0, (len(matrizX)-1)):
    tamCasa.append(matrizX[i][1])

correlacao(tamCasa, vetorPreco)










