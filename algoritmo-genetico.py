# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:57:25 2019

@author: Douglas, Joana e Leticia
"""
import random
import matplotlib.pyplot as plt
import math

def criaMatrizCromossomos():
    #gerar uma matriz 20x20 de numero inteiro de 1 a 20
    for i in range(0, 20):
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

    print(x)
    print("\n")
    print(y)


    #Gera matriz das distancias de cada cidade
    for linha in range(0, 20):
        line = []#limpa a var line sempre que for pra próxima linha
        for coluna in range(0, 20):
#            valor = math.sqrt((x[linha]-x[coluna])^2+(y[linha]-y[coluna])^2)
            valor = round(((x[linha]-x[coluna])**2+(y[linha]-y[coluna])**2)**(1/2), 4)
            line.append(valor)
        matrizValores.append(line)
    
    
    
def criarListaDistancias():
    for linha in matrizValores:
        listaDistancias.append(linha[1])
 
        







#Gera grafico com os valores da função aptidão
#plt.xlabel('Indivíduos')
#plt.ylabel('Aptidão')
#plt.title('Aptidão dos indivíduos')
#plt.plot(matrizValores)        
#plt.show()
   
    
    
matriz = [];
matrizValores = [];
listaDistancias = [];

'''gerar matriz 20x20 de numeros inteiros'''
criaMatrizCromossomos();
'''gerar matriz valorada de 20x21'''
criarMatrizValores();
'''gerar a matriz com o calculo sa distancias'''
criarListaDistancias();


