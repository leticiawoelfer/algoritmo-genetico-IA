# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:57:25 2019

@author: Douglas, Joana e Leticia
"""
import random
import matplotlib.pyplot as plt
import numpy as np

#Variageis locais
matrizPopulacao = []
matrizDistancias = []
listaDistancias = []
distanciasOrdenadas = []


def criaMatrizPopulacao():
    #gerar uma matriz 20x20 de numero inteiro de 1 a 20
    for i in range(0, 20):
        linha = random.sample(range(1,21),20);
        matrizPopulacao.append(linha);
    
def criarMatrizDistancias():
    x = []
    y = []
    #monta as duas listas de numero aleatorios entre 0.0 e 1.0
    for i in range(0, 20):
        x.append(round(random.uniform(0.0, 1.0),4))
        y.append(round(random.uniform(0.0, 1.0),4))

    #Gera matriz das distancias de cada cidade
    for linha in range(0, 20):
        line = []#limpa a var line sempre que for pra próxima linha
        for coluna in range(0, 20):
            valor = round(((x[linha]-x[coluna])**2+(y[linha]-y[coluna])**2)**(1/2), 4)
            line.append(valor)
        matrizDistancias.append(line)

def criarListaDistancias():
    #Cria a lista com a soma das distancias das cidades
    for linha in range(0, len(matrizPopulacao)):
        total=0#Limpa valor total a cada troca de individuo
        for coluna in range(0, len(matrizPopulacao[0])):
            if coluna == 19:#Condição para finalizar na cidade que iniciou
                total=total+(matrizDistancias[matrizPopulacao[linha][coluna]-1][matrizPopulacao[linha][0]-1])             
            else:
                total=total+(matrizDistancias[matrizPopulacao[linha][coluna]-1][matrizPopulacao[linha][coluna+1]-1])
        listaDistancias.append(total)


def exibeResultados():
#Gera grafico com os valores da função aptidão
    plt.xlabel('Indivíduos')
    plt.ylabel('Aptidão')
    plt.title('Aptidão dos indivíduos')
    plt.plot(listaDistancias)
    plt.axis([0, 100, 5, 15])
    plt.show()
    
    

    #Exibe o tamanho da população na legenda
    print ('Tamanho da população: '+ str(len(matrizPopulacao)))
    
    #Exibe taxa de mutação na legenda
    print ('Taxa de mutação: '+ str(listaDistancias[distanciasOrdenadas[0][0]]))

    #Exibe numero de cidades na legenda
    print ('Numero de cidades: '+ str(len(matrizPopulacao[0])))
    
    #Exibe o melhor custo na legenda
    print ('Melhor custo: '+ str(listaDistancias[distanciasOrdenadas[0][0]]))
    
    #Exibe a melhor solução na legenda
    print ('Melhor solução: '+ str(matrizPopulacao[distanciasOrdenadas[0][0]]))



def ordenaMatrizDistancias():
    matrizPopulacaoSort = []
    matrizDistanciasSort = []
    distanciasOrdenadas.append(np.argsort(listaDistancias))

    for individuo in range(0,  20):
        matrizPopulacaoSort.append(matrizPopulacao[distanciasOrdenadas[0][individuo]])
        matrizDistanciasSort.append(matrizDistancias[distanciasOrdenadas[0][individuo]])

#Não sei como colocar os valores de uma matriz na outra, não assim:        
#    matrizDistancias = matrizDistanciasSort
#    matrizPopulacao = matrizPopulacaoSort

    
    
#Laço principal até 10.000 interações
#    for interacoes in range(0, 10000):
#        teste=interacoes
    
    
    
    
    
    
    



'''gerar matriz 20x20 de numeros inteiros'''
criaMatrizPopulacao();
'''gerar matriz valorada de 20x21'''
criarMatrizDistancias();
'''gerar a matriz com o calculo sa distancias'''
criarListaDistancias();
'''Ordenar um array retornando apenas o index'''
ordenaMatrizDistancias()
'''Exibe resultado em modo grafio'''
exibeResultados();

