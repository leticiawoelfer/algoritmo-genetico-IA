# -*- coding: utf-8 -*-
"""
@authors: Douglas, Joana e Leticia
"""
import matplotlib.pyplot as plt
import scipy.io as scipy
import numpy as np
from random import uniform


def lerBaseDados():
    matrizData = []
    mat = scipy.loadmat('data_preg.mat')
    matrizData = mat['data']

    return matrizData


def geraGrafico(matrizData):
    plt.scatter(matrizData[:, 0], matrizData[:, 1])

    #    plt.plot(x,resultados)
    #    plt.title("Correlação:"+str(r)+"  B0:"+str(b0)+"  B1:"+str(b1))
    plt.figure()


# fazendo a função polyfit
def polyfit(matrizData):
    coefs1 = np.polyfit(matrizData[:, 0], matrizData[:, 1], 1)
    coefs2 = np.polyfit(matrizData[:, 0], matrizData[:, 1], 2)
    coefs3 = np.polyfit(matrizData[:, 0], matrizData[:, 1], 3)
    coefs8 = np.polyfit(matrizData[:, 0], matrizData[:, 1], 8)


    y1 = coefs1[1] + coefs1[0] * matrizData[:, 0]
    y2 = coefs2[2] + coefs2[1] * matrizData[:, 0] + coefs2[0] * matrizData[:, 0] ** 2
    y3 = coefs3[3] + coefs3[2] * matrizData[:, 0] + coefs3[1] * matrizData[:, 0] ** 2 + coefs3[0] * matrizData[:,0] ** 3
    y8 = coefs8[8] + coefs8[7] * matrizData[:, 0] + coefs8[6] * matrizData[:, 0] ** 2 + coefs8[5] * matrizData[:,0] ** 3 \
         + coefs8[4] * matrizData[:, 0] ** 4 + coefs8[3] * matrizData[:, 0] ** 5 + coefs8[2] * matrizData[:, 0] ** 6 + \
         coefs8[1] * matrizData[:, 0] ** 7 + coefs8[0] * matrizData[:, 0] ** 8

    erro_medio = calcErroQuadMedio(matrizData, y1, y2, y3, y8)
    #g) [0.26593234844362734, 0.13852582459887405, 0.07869718985110802, 0.05870965739108984] y8 é o mais preciso

    print(erro_medio)
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    ax1.scatter(matrizData[:, 0], matrizData[:, 1])
    ax1.plot(matrizData[:, 0], y1, 'r')
    ax1.plot(matrizData[:, 0], y2, 'g')
    ax1.plot(matrizData[:, 0], y3, 'b')
    ax1.plot(matrizData[:, 0], y8, 'y')

    plt.show()


def polyfitTeste(matrizData, matrizDataTeste):

    coefs1 = np.polyfit(matrizData[:, 0], matrizData[:, 1], 1)
    coefs2 = np.polyfit(matrizData[:, 0], matrizData[:, 1], 2)
    coefs3 = np.polyfit(matrizData[:, 0], matrizData[:, 1], 3)
    coefs8 = np.polyfit(matrizData[:, 0], matrizData[:, 1], 8)

    y1 = coefs1[1] + coefs1[0] * matrizData[:, 0]
    y2 = coefs2[2] + coefs2[1] * matrizData[:, 0] + coefs2[0] * matrizData[:, 0] ** 2
    y3 = coefs3[3] + coefs3[2] * matrizData[:, 0] + coefs3[1] * matrizData[:, 0] ** 2 + coefs3[0] * matrizData[:,
                                                                                                    0] ** 3
    y8 = coefs8[8] + coefs8[7] * matrizData[:, 0] + coefs8[6] * matrizData[:, 0] ** 2 + coefs8[5] * matrizData[:,
                                                                                                    0] ** 3 \
         + coefs8[4] * matrizData[:, 0] ** 4 + coefs8[3] * matrizData[:, 0] ** 5 + coefs8[2] * matrizDataTeste[:, 0] ** 6 + \
         coefs8[1] * matrizData[:, 0] ** 7 + coefs8[0] * matrizData[:, 0] ** 8

    # calcular erro medio baseado em uma matriz, desta vez somente com os dados de teste
    erro_medio = calcErroQuadMedio(matrizDataTeste, y1, y2, y3, y8)

    matrizDataOrig = lerBaseDados() # para plotar os 53 pontos
    print(erro_medio)
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    ax1.scatter(matrizDataOrig[:, 0], matrizDataOrig[:, 1]) #53 pontos plotados
    ax1.plot(matrizData[:, 0], y1, 'r')
    ax1.plot(matrizData[:, 0], y2, 'g')
    ax1.plot(matrizData[:, 0], y3, 'b')
    ax1.plot(matrizData[:, 0], y8, 'y')
      

    plt.show()


def tiraGrupoTeste(matrizData, aleatorios):
#    matrizData2 = []
#    matrizDataTeste = []
    matrizDataTeste=np.zeros((4,2), dtype=np.float64)
    matrizData2=np.zeros((int(len(matrizData)),int(len(matrizData[0]))), dtype=np.float64)
    
    print(len(matrizData[0]))
    
    count = 0 
    i = 0
    while i < len(matrizData):
        if matrizData[i][0] in aleatorios:
            linha = []
            linha.append(matrizData[i])
#            linha.insert(i,matrizData[i][1])
#            matrizTemp=np.zeros((1,2), dtype=np.float64)
#            matrizTemp[0][0]= linha[0]
#            matrizTemp[0][1]= linha[1]
            
#            matrizDataTeste.append(matrizData[i])
#            matrizDataTeste.append(matrizTemp[0])
            matrizDataTeste[count][0]= linha[0][0]
            matrizDataTeste[count][1]= linha[0][1]
            count=count+1
#            matrizDataTeste.insert(i,1, matrizData[i][1])

        else:
#            linha = []
#            linha.insert(i,matrizData[i][0])
#            linha.insert(i,matrizData[i][1])
#            matrizData2.append(linha)
            matrizData2[i][0] = matrizData[i][0]
            matrizData2[i][1] = matrizData[i][1]
            
        i += 1

    return matrizData2, matrizDataTeste

# calcular o erro quadratico medio
def calcErroQuadMedio(matriz_dados, y1, y2, y3, y8):
    erro_medio = []

    #linha1
    erro_medio.append(calcSomaResiduo(matriz_dados, y1) / len(y1))

    #linha2
    erro_medio.append(calcSomaResiduo(matriz_dados, y2) / len(y2))

    #linha3
    erro_medio.append(calcSomaResiduo(matriz_dados, y3) / len(y3))

    #linha4
    erro_medio.append(calcSomaResiduo(matriz_dados, y8) / len(y8))

    return erro_medio


def calcSomaResiduo(matriz_dados, y):

    total_residuo = 0
    i = 0
    while i < len(y):

        total_residuo += calcResiduo(matriz_dados[i][1], y[i])
        i += 1

    return total_residuo


def calcResiduo(observado, estimado):

    residuo = (observado - estimado) ** 2

    return residuo

def geraAleatorios():
    aleatorios = []
    aleatorios.append(round(uniform(0, 5.2), 1))
    aleatorios.append(round(uniform(0, 5.2), 1))
    aleatorios.append(round(uniform(0, 5.2), 1))
    aleatorios.append(round(uniform(0, 5.2), 1))
    aleatorios.append(round(uniform(0, 5.2), 1))

    print(aleatorios)

    return aleatorios


# geraGrafico(lerBaseDados())
polyfit((lerBaseDados()))

# dividindo os dados aleatoriamente gerando 2 matrizes
aleatorios = geraAleatorios()
matrizData2, matrizDataTeste = tiraGrupoTeste((lerBaseDados()), aleatorios)

# matrizData2 = 47 pontos para gerar curva
polyfitTeste(matrizData2, matrizDataTeste)
