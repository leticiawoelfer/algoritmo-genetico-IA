# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:57:25 2019

@author: _-Douglas-_
"""
import random

#gerar uma matriz 20x20


def criaMatrizCromossomos():
    for x in range(1, 21):
        linha = random.sample(range(1,21),20);
        matriz.append(linha);
    #print(matriz);
    
def criarMatrizValores():
    x = [];
    y = [];
    line = [];
    #monta as duas listas 
    for i in range(1, 21):
        x.append(round(random.uniform(0.0, 1.0),4));
        y.append(round(random.uniform(0.0, 1.0),4));
    #montar a linha de valores para adicionar na matriz de valores
    for linha in range(0, 22):
        for coluna in range(0, 22):
            line.append(x[linha] - y[coluna]);
        matrizValores.append(line);
    
    print(x);
    print(y);
    print(matrizValores);
        #for j in range()
    


"""for i in range(1, 20):
    linha2 = i
    i+=1
    x = round(random.uniform(0.0, 1.0),2)
    y = round(random.uniform(0.0, 1.0),2)
    print(x)
    #print(y)
    
print ("")
   
for i in range(1, 20):
    linha2 = i
    i+=1
    x = round(random.uniform(0.0, 1.0),2)
    y = round(random.uniform(0.0, 1.0),2)
    #print(x)
    print(y)
""" 
matriz = [];
matrizValores = [];

criaMatrizCromossomos();
criarMatrizValores();