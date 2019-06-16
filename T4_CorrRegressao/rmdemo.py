# -*- coding: utf-8 -*-
"""
@authors: Douglas, Joana e Leticia
"""
import matplotlib.pyplot as plt
import math
import csv
import numpy as np
from mpl_toolkits.mplot3d import Axes3D



def lerArquivo():
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:            
            vetorPreco.append(float(row[2]))
            del row[2]
            row = [int(x) for x in row]
            row.insert(0, 1)
            matrizX.append(row)
        npMatrizX = np.array([l[:] for l in matrizX])
    return(npMatrizX)

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
    for i in range(0, (len(matrizX))):
        lista.append(int(matrizX[i][posicao]))

def geraMatrizTransposta():
    for i in range(0, 3):
        linha = []
        for j in range(0, len(matrizX)):
            linha.append(matrizX[j][i])
        matrizXTrans.append(linha)
    
def calcularB():
    a = np.dot(matrizXTrans, matrizX)
    b = np.linalg.inv(a)
    c = np.dot(matrizXTrans,vetorPreco)

    matrizB.append(b*c)

    
def calcularLinhaRegr():
    pass


def geraGrafico3D():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(tamCasa, numQuarts, vetorPreco)
    ax.set_xlabel("Tamanho")
    ax.set_ylabel("Numero de quartos")
    ax.set_zlabel("Preço")
    ax.set_title("Correlação Tamanho da casa e Preço: "+str(corr1) + "\n" + "Correlação Número de quartos e Preço: "+str(corr2))
    ax.plot(npMatrizX[:, 1], npMatrizX[:, 2], linhaRegrassao, 'r')
    plt.show()

def getLinhaRegressao():
    matriz = np.dot(matrizXTrans, npMatrizX)
    matriz = matriz.astype(float)
    matriz = matriz**-1
    matriz = np.dot(matriz, matrizXTrans)
    b = np.dot(matriz, vetorPreco)
    y = np.dot(npMatrizX, b)
    return(y)
    #Para testar o beta
#    return(b)

matrizX = []
vetorPreco = []
npMatrizX = lerArquivo()

#prepara a lista para fazer a correlacao e regressao linear
tamCasa = []
preparaLista(1, tamCasa)    
corr1 = correlacao(tamCasa, vetorPreco)
#print("Correlação Tamanho da casa e Preço: "+str(corr1))
#regr = regressao


#prepara a lista para fazer a correlacao e regressao linear
numQuarts = []
preparaLista(2, numQuarts)
corr2 = correlacao(numQuarts, vetorPreco)
#print("Correlação Número de quartos e Preço: "+str(corr2))



#matrizXTrans = []
#geraMatrizTransposta()
matrizXTrans = np.transpose(npMatrizX)


#matrizB = []
#calcularB()
#linhaRegrassao = np.dot(npMatrizX,matrizB)
#print(linhaRegrassao)

linhaRegrassao = getLinhaRegressao()

beta = getLinhaRegressao()

# Para testar se o s balores de beta estão ok, comentar a linha 91 e descomentar a linha 93
y1 = beta[0] + beta[1] * 1650 + beta[2] * 3** 2
print(y1)

calcularLinhaRegr()


geraGrafico3D()




