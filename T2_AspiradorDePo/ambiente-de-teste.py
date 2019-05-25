# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import matplotlib.pyplot as plt
import random
import time


def exibir(I):
    plt.imshow(I, 'gray')
    plt.show(block=False)
    plt.pause(0.1)
    plt.clf()  

####definindo ponto inicial do aspirador
point = "*"

linha = random.randint(1,4)
coluna = random.randint(1,4)

plt.scatter(linha, coluna, marker=point)


####definindo ponto inicial do aspirador


####Fazendo aspirador andar
point = "o"

i=1
j=1
for i in range(1, 5):
    linha2 = i
    i+=1
    for j in range(1, 5):
        coluna2 = j
        #time.sleep(1)
        print('posicao atual: ['+str(linha2)+'],['+str(coluna2)+']')
        plt.scatter(linha2, coluna2, marker=point)
        j+=1




####Fazendo aspirador andar




   
p1_1 = random.randint(0,1)
p1_2 = random.randint(0,1)
p1_3 = random.randint(0,1)
p1_4 = random.randint(0,1)
p2_1 = random.randint(0,1)
p2_2 = random.randint(0,1)
p2_3 = random.randint(0,1)
p2_4 = random.randint(0,1)
p3_1 = random.randint(0,1)
p3_2 = random.randint(0,1)
p3_3 = random.randint(0,1)
p3_4 = random.randint(0,1)
p4_1 = random.randint(0,1)
p4_2 = random.randint(0,1)
p4_3 = random.randint(0,1)
p4_4 = random.randint(0,1)
 
ambiente = [[1, 1, 1, 1, 1, 1],
        [1, (p1_1), (p1_2), (p1_3), (p1_4), 1],
        [1, (p2_1), (p2_2), (p2_3), (p2_4), 1],
        [1, (p3_1), (p3_2), (p3_3), (p3_4), 1],
        [1, (p4_1), (p4_2), (p4_3), (p4_4), 1],
        [1, 1, 1, 1, 1, 1]]    


exibir(ambiente)
    

