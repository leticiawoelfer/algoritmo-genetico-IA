# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:57:25 2019

@author: Douglas, Joana e Leticia
"""
import random
import matplotlib.pyplot as plt
import numpy as np
from random import randint

#Variageis locais
matrizPopulacao = []
matrizDistancias = []
listaDistancias = []
indicesOrdenados = []
resultados=[]


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
                total=round(total+(matrizDistancias[matrizPopulacao[linha][coluna]-1][matrizPopulacao[linha][0]-1]),4)             
            else:
                total=round(total+(matrizDistancias[matrizPopulacao[linha][coluna]-1][matrizPopulacao[linha][coluna+1]-1]),4)
        listaDistancias.append(total)
        resultados.append(total)

def exibeResultados():
#Gera grafico com os valores da função aptidão
    plt.xlabel('Indivíduos')
    plt.ylabel('Aptidão')
    plt.title('Aptidão dos indivíduos')
    plt.plot(resultados)
    plt.axis([0, 100, 5, 15])
    plt.show()
    
    

    #Exibe o tamanho da população na legenda
    print ('Tamanho da população: '+ str(len(matrizPopulacao)))
    
    #Exibe taxa de mutação na legenda
    print ('Taxa de mutação: '+ str(listaDistancias[0]))

    #Exibe numero de cidades na legenda
    print ('Numero de cidades: '+ str(len(matrizPopulacao[0])))
    
    #Exibe o melhor custo na legenda
    print ('Melhor custo: '+ str(listaDistancias[0]))
    
    #Exibe a melhor solução na legenda
    print ('Melhor solução: '+ str(matrizPopulacao[0]))



def ordenaMatrizes():
    matrizPopulacaoSort = []
    matrizDistanciasSort = []
    temp=[]
    
    #Ordenando distancias na lista
    indicesOrdenados.append(np.argsort(listaDistancias))
    
    
    #Gerando matriz temporaria de distancias
    for distancias in range(0,  20):
        temp.append(listaDistancias[indicesOrdenados[0][distancias]])
    
    #Atualizando variavel original com a ordenação
    for d in range(0, 20):
        listaDistancias[d]=temp[d]    
    
    #Organiza as matrizes de população e distancias com base na ordenação das distancias        
    for individuo in range(0,  20):
        matrizPopulacaoSort.append(matrizPopulacao[indicesOrdenados[0][individuo]])
        
        #talvez a da distancia possa ser ignorada - Validar
        matrizDistanciasSort.append(matrizDistancias[indicesOrdenados[0][individuo]])
        
    #atualiza matriz antiga com os valores ordenados
    for i in range(0, 20):
        matrizPopulacao[i]=matrizPopulacaoSort[i]
        matrizDistancias[i]=matrizDistanciasSort[i]
        

def removerMetade():
    #Remoção dos 10 piores individuos 
    del matrizPopulacao[9:19]
    del matrizDistancias[9:19]
    del listaDistancias[9:19]        
        

'''def roleta2():
    roletaRand = randint(0, 100)
    i=0
    soma = 0.0
#    print(str(roletaRand))
    for i in range(0, len(matrizPopulacao)):
#        print(str(listaDistancias[i]))
        soma += listaDistancias[i]
        if soma >= roletaRand:
            return i
			
    return 0
    
#Laço principal até 10.000 interações
for interacoes in range(0, 10000):
   teste=interacoes
   
#Seleção por roleta
   pai1=randint(0, 9)
   pai2=randint(0, 9)
#   print(str(pai1))
#   print(str(pai2))
#   print(str(roleta()))
   '''
    
def roleta():
    matrizProbabilidade = [[1,1,21],
                           [2,22,35],
                           [3,36,48],
                           [4,49,59],
                           [5,60,69],
                           [6,70,77],
                           [7,78,85],
                           [8,86,92],
                           [9,93,97],
                           [10,98,100]]
    listaPais = []
    sorteados = random.sample(range(1,100),10)
    print(sorteados)
    #validar se nenhum apareceu mais de 5 vezes, se não
    #tem que sortear de novo
    sorteadosConvert = []
    '''parou aqui'''
    
    
    



'''gerar matriz 20x20 de numeros inteiros'''
criaMatrizPopulacao();

'''gerar matriz valorada de 20x21'''
criarMatrizDistancias();

'''gerar a matriz com o calculo sa distancias'''
criarListaDistancias();

'''Ordenar um array retornando apenas o index'''
ordenaMatrizes()

'''Remover metade da população'''
removerMetade()


roleta2()

'''Exibe resultado em modo grafio'''
exibeResultados()


#print(str(roleta()))

