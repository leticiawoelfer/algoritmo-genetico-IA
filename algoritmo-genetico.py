# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:57:25 2019

@author: Douglas, Joana e Leticia
"""
import random
import matplotlib.pyplot as plt

def criaMatrizCromossomos():
    #gerar uma matriz 20x20 de numero inteiro de 1 a 20
    for x in range(0, 20):
        linha = random.sample(range(1,21),20);
        matriz.append(linha);
    #print(matriz);
    
def criarMatrizValores():
    x = []
    y = []
    #monta as duas listas de numero aleatorios entre 0.0 e 1.0
    for i in range(0, 20):
        x.append(round(random.uniform(0.0, 1.0),4))
        y.append(round(random.uniform(0.0, 1.0),4))

    #gera a matriz numerica de 20x20 
    for linha in range(0, 20):
        line = []#limpa a var line sempre que for pra próxima linha
        for coluna in range(0, 20):
            valor = 0
            #print("linha ={0}".format(linha))
            #print("coluna ={0}".format(coluna))
            #print(type(linha));
            #print(type(coluna));
            if linha != coluna:
                #print("x[{0}] - y[{1}]".format(linha, coluna))
                valor = round(x[linha] - y[coluna], 4)
                #print("{0} - {1} = {2}".format(x[linha], y[coluna], valor))
            #print("adiciona valor na line ={0}".format(valor))
            line.append(valor)            
        #print("adiciona valor na matrizValores ={0}".format(line))
        matrizValores.append(line)
    #print(matrizValores)
    
def criarListaDistancias():
    for linha in matrizValores:
        listaDistancias.append(linha[1])
        #print(linha[1])

        


plt.xlabel('Indivíduos')
plt.ylabel('Aptidão')
plt.title('Aptidão dos indivíduos')
plt.plot(matrizValores)        
plt.show()
   
    
    
matriz = [];
matrizValores = [];
listaDistancias = [];

'''gerar matriz 20x20 de numeros inteiros'''
criaMatrizCromossomos();
'''gerar matriz valorada de 20x21'''
criarMatrizValores();
'''gerar a matriz com o calculo sa distancias'''
criarListaDistancias();


