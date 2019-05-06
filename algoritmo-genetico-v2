# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 16:02:21 2019

@author: Douglas, Joana e Leticia
"""
from math import sqrt
import random
from random import randint

def calculaDistancia(cidade1, cidade2):

    distancia = round(sqrt((cidade1[0]-cidade2[0])**2 + (cidade1[1]-cidade2[1])**2), 4)

    if distancia < 0:
        distancia = distancia * -1

    return distancia


def geraPontos():

    vCidades = []
    # monta as duas listas de numero aleatorios entre 0.0 e 1.0
    for i in range(0, 20):
        x = round(random.uniform(0.0, 1.0), 4)
        y = round(random.uniform(0.0, 1.0), 4)
        vCidades.append([x, y])

    return vCidades


def calculaCustoRota(rota, matrizDist):

    custo = 0
    i = 0
    while i < 19:

        custo = custo + matrizDist[rota[i]-1][rota[i+1]-1]
        i = i + 1

    return round(custo, 4)


def ordenaMatriz(matriz):

   #selection sort
    for index in range(0, len(matriz)):
        min_index = index

        for right in range(index + 1, len(matriz)):
            if matriz[right][20] < matriz[min_index][20]:
                min_index = right

        matriz[index], matriz[min_index] = matriz[min_index], matriz[index]

    return matriz


def geraDistancias(vCidades):

    mDistancias = []

    # gera a matriz numerica de 20x20
    for linha in range(0, 20):
        line = []  # limpa a var line sempre que for pra próxima linha

        for coluna in range(0, 20):
            #valor = 0
            distancia =0
            # print("linha ={0}".format(linha))
            # print("coluna ={0}".format(coluna))
            # print(type(linha));
            # print(type(coluna));

            if linha != coluna:
                # print("x[{0}] - y[{1}]".format(linha, coluna))

                #valor = round(x[linha] - y[coluna], 4)
                distancia = calculaDistancia(vCidades[linha], vCidades[coluna])
            else:
                distancia = 0

                # print("{0} - {1} = {2}".format(x[linha], y[coluna], valor))
            # print("adiciona valor na line ={0}".format(valor))

            line.append(distancia)
            # print("adiciona valor na matrizValores ={0}".format(line))

        mDistancias.append(line)
    # print(matrizValores)

    return mDistancias


def geraDistanciasRelativas(mCromossomos):

    distancia_total = 0
    i = 0
    while i < 10:
        distancia_total = distancia_total + mCromossomos[i][20]
        i = i+1

    distancias_relativas = []
    umporcento = distancia_total / 100
    # mCromossomos[i][21]
    i = 0
    while i < 10:
        distancias_relativas.append(mCromossomos[i][20] / umporcento)
        i = i + 1

    i = 0
    j = 9
    while i < 10:
        mCromossomos[i].append(round(distancias_relativas[j] / 100, 4))
        i = i + 1
        j = j - 1

    return mCromossomos


def geraCaminhos(mDistancias):


    mCromossomos = []

    # gerar uma matriz 20x20 de numero inteiro de 1 a 20
    for x in range(0, 20):

        linha = random.sample(range(1, 21), 20)

        custo = calculaCustoRota(linha, mDistancias)
        linha.append(custo)
        mCromossomos.append(linha)

    mCromossomos = ordenaMatriz(mCromossomos)
    #mCromossomos = geraDistanciasRelativas(mCromossomos)

    return mCromossomos


def printMatriz(matrizPr):

    tamanhoMt = len(matrizPr)
    i = 0
    while i < tamanhoMt:
        print(matrizPr[i])
        i = i+1


def cycle(mCromossomos, mDistancias):

    print('entrou no cycle')
    i = 0
    j = 10
    while i < 10:
#        print('entrou no cycle: '+str(i))
#        printMatriz(mCromossomos)
#        print('\n')
        # chamamos a função para gerar os novos cromossomos
        # devolve dois vetores dos filhos gerados a partir dos dois pais
        # escolha dos pais POR ENQUANTO de forma seguida: 0 e 1, 2 e 3, etc..

        #### AQUI COLOCA A FUNÇÃO ROLETA #######

        # RESULTADO DA FUNÇÃO ROLETA COLOCA NO ARGUMENTO DO copiaVetor() para ambos abaixo
        novo_vetor_um = copiaVetor(mCromossomos[i])
        novo_vetor_dois = copiaVetor(mCromossomos[i+1])

        #print(novo_vetor_um)
        #print(novo_vetor_dois)
        #print('chama gera novos crom \n')
        novo_vetor_um, novo_vetor_dois = geraNovosCromossomos(novo_vetor_um, novo_vetor_dois)
        #print('\n voltou do gera new crom \n')

#       print(novo_vetor_um)
#       print(novo_vetor_dois)
        # a partir da posicao 10 colocamos também em sequencia os vetores filhos
        mCromossomos.append(novo_vetor_um)
        mCromossomos.append(novo_vetor_dois)

#        print('\n')
#        printMatriz(mCromossomos)
        # recalculamos o custo das rotas dos novos filhos
        mCromossomos[j][20] = calculaCustoRota(mCromossomos[j], mDistancias)
        mCromossomos[j+1][20] = calculaCustoRota(mCromossomos[j+1], mDistancias)

        i = i+2
        j = j+2

    mCromossomos = ordenaMatriz(mCromossomos)

    return mCromossomos


def geraNovosCromossomos(novo_vetor_um, novo_vetor_dois):
    print('entrou no geraNCrom')
    # assumimos que o primeiro numero randomico nao pode ser posicao contendo valores iguais em ambos os vetores
    k = randint(0, 19)
    valid_rand = 0
    while valid_rand < 1:
        if novo_vetor_um[k] == novo_vetor_dois[k]:
            k = randint(0, 19)
        else:
            print('posicao escolhida rand '+ str(k))
            valid_rand = 1

    #print(novo_vetor_um)
    #print('\n')
    #print(novo_vetor_dois)
    #print('\n')
    # k será -1 quando acabarmos todas as inversoes possíveis para aqueles cromossomos
    while k >= 0:
        # realizamos a inversão
        aux = novo_vetor_um[k]
        novo_vetor_um[k] = novo_vetor_dois[k]
        novo_vetor_dois[k] = aux
        #novo_um[k], novo_dois[k] = novo_dois[k], novo_um[k]
    #    print('\n')
    #    print(novo_vetor_um)
        #print('\n')
    #    print(novo_vetor_dois)
        #print('\n')
        # procuramos um novo valor para k
        k = procuraPosicaoRepetido(novo_vetor_um, k)

    return novo_vetor_um, novo_vetor_dois


def procuraPosicaoRepetido(novo_vetor_um, k):

    posicao_repetido = -1
    i = 0
    while i < 20:
        # compara a posicao recebida por parametro com todas as outras (menos ela mesma)
        if novo_vetor_um[i] == novo_vetor_um[k] and i != k:

            # posicao que foi encontrada a repeticao é a que queremos para a próxima iteração
            posicao_repetido = i

        i = i+1

    return posicao_repetido

def desalocaMatriz(mCromossomos):


    i=0
    while i < 10:
        mCromossomos.pop()
        i = i+1

    return mCromossomos

def copiaVetor(vetor_recebido):

    vetor_novo = []

    i=0
    while i < len(vetor_recebido):
        vetor_novo.append(vetor_recebido[i])
        i = i+1

    return vetor_novo

vCidades = geraPontos()

printMatriz(vCidades)
print('\n')
mDistancias = geraDistancias(vCidades)

printMatriz(mDistancias)

print('\n')
mCromossomos = geraCaminhos(mDistancias)

printMatriz(mCromossomos)



i = 0
while i < 3: # numero de vezes a ser executado o AG
    mCromossomos = desalocaMatriz(mCromossomos)

    print('\n')
    printMatriz(mCromossomos)
    mCromossomos = cycle(mCromossomos, mDistancias)
    i = i + 1

print('\n')
printMatriz(mCromossomos)
