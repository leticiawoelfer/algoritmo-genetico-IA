# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:57:25 2019

@author: Douglas, Joana e Leticia
"""
import random


def criaMatrizPopulacao():
    #gerar uma matriz 20x20 de numero inteiro de 1 a 20
    for i in range(0, 20):
        linha = random.sample(range(1,21),20);
        matrizPopulacao.append(linha);
    #print(matriz);
    
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

    for linha in range(0, 20):
        total=0
        for coluna in range(0, 20):
            if coluna == 19:
                total=total+(matrizDistancias[matrizPopulacao[linha][coluna]-1][matrizPopulacao[linha][0]-1])             
            else:
                total=total+(matrizDistancias[matrizPopulacao[linha][coluna]-1][matrizPopulacao[linha][coluna+1]-1])
            

        listaDistancias.append(total)

            
#            print (str(matrizPopulacao[linha][coluna]-1) + ' ' + str(matrizPopulacao[linha][coluna+1]-1)) 
            

#        listaDistancias.append(10)
#            valor = round(((x[linha]-x[coluna])**2+(y[linha]-y[coluna])**2)**(1/2), 4)
            
#        dist(i,1)=dist(i)+dcidade(tour(i,j),tour(i,j+1)); 






#Gera grafico com os valores da função aptidão
#plt.xlabel('Indivíduos')
#plt.ylabel('Aptidão')
#plt.title('Aptidão dos indivíduos')
#plt.plot(matrizValores)        
#plt.show()
   
    
    
matrizPopulacao = [];
matrizDistancias = [];
listaDistancias = [];


'''gerar matriz 20x20 de numeros inteiros'''
criaMatrizPopulacao();
'''gerar matriz valorada de 20x21'''
criarMatrizDistancias();
'''gerar a matriz com o calculo sa distancias'''
criarListaDistancias();


