# -*- coding: utf-8 -*-
"""
@authors: Douglas, Joana e Leticia
"""
import matplotlib.pyplot as plt
import math
import csv
import numpy as np

#le os dados do arquivo, faz uma matriz temporaria, converte para matriz 
#tipo numpy e retorna a mesma
def lerArquivo():
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        matrizXTemp = []
        for row in csv_reader:            
            vetorPreco.append(float(row[2]))
            del row[2]
            row = [int(x) for x in row]
            row.insert(0, 1)
            matrizXTemp.append(row)
        matrizX = np.array([l[:] for l in matrizXTemp])
    return(matrizX)

#aqui calculamos a correlacao
def correlacao(x, y):
    #variavel n contem o tamanho do array x
    n = len(x)
    
    #calculando a media de x
    somax = 0
    for numX in x:
        somax = somax + numX
    mediaX = somax / n
    
    #calculando a media de y
    somay = 0
    for numY in y:
        somay = somay + numY
    mediaY = somay / n
    
    #inicializa os valores que vão ser descobertos abaixo    
    somaR = 0
    somaMediaX = 0
    somaMediaY = 0
    #para todas as posições de x e y é feito o calculo de 
    #acordo com a fórmula do enunciado
    #somaR representa o dividendo da fórmula
    #somaMediaX, somaMediaY são valores para achar o divisor final
    for i in range(0,n):
        somaR = somaR + ((x[i] - mediaX) * (y[i] - mediaY))
        somaMediaX = somaMediaX + ((x[i] - mediaX)**2)
        somaMediaY = somaMediaY + ((y[i] - mediaY)**2)
        
    raizQuad = math.sqrt(somaMediaX * somaMediaY)
    
    #agora com todos os valores encontrados, conseguimos calcular o
    #valor da correcao, e ai retornamos ele pois precisa ser usado a diante.
    r = round((somaR/raizQuad),4)
    return r;

def geraGrafico3D():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(tamCasa, numQuarts, vetorPreco)
    ax.set_xlabel("Tamanho")
    ax.set_ylabel("Numero de quartos")
    ax.set_zlabel("Preço")
    ax.set_title("Correlação Tamanho da casa e Preço: "+str(corr1) + "\n" + "Correlação Número de quartos e Preço: "+str(corr2))
    ax.plot(matrizX[:, 1], matrizX[:, 2], regressao, 'r')
    plt.show()

def regmultipla(x, y):
    #a = matriz transposta vezes a matriz, elevado a -1
    a = np.linalg.inv(x.transpose().dot(x))
    #a vezes a matriz transposta, vezes a lista de precos, resulta em beta
    beta = a.dot(x.transpose()).dot(y)
    return beta, matrizX.dot(beta)


''' INICIO '''
vetorPreco = []
matrizX = lerArquivo()

#correlacao entre tamanho da casa e o preço
tamCasa = matrizX[:,1]
corr1 = round(correlacao(tamCasa, vetorPreco),4)

#correlacao entre número de quartos e o preço
numQuarts = matrizX[:,2]
corr2 = round(correlacao(numQuarts, vetorPreco),4)

#faz a regressao e calcula beta
beta, regressao = regmultipla(matrizX, vetorPreco)

#apresenta graficamente os resultados
geraGrafico3D()

#g) Calcule o preço de uma casa que tem tamanho de 1650 e 3 quartos. O resultado deve ser igual a 293081.
questaoG = np.array([1, 1650, 3])
result = questaoG.dot(beta)
print("Casa com 3 quartos e 1650 de tamanho custa R$"+str(round(result,2)))






