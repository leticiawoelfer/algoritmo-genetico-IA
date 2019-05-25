import matplotlib.pyplot as plt
import random

def exibir(I):
    plt.imshow(I, 'RdYlGn')
    #plt.show(block=False)
    #plt.pause(0.5)
    #plt.clf()

def iniciar():
    linha = random.randint(1,4)
    coluna = random.randint(1,4)
    print('posicao INICIAL sorteada: ['+str(linha)+'],['+str(coluna)+']')
    aspirador = plt.scatter(coluna, linha, marker=point)

"""1 escolher randomicamente um numero de 4 a 13 (qtd min e max de
  quadrados sujos);
2 dois numeros randomicos de 1 a 4, que vão ser as posicoes;
3 verificar se ja tem sujeira na posicao, se nao tiver inserir a sujeira e 
  incrementar o contador.
Obs: contorno = 2(verde), limpo = 1(bege) e sujeira = 0(bordô)"""
def inserirSujeiras():
    qtdTotalSujeira = random.randint(4,13);
    #print("qtdTotalSujeira: " + str(qtdTotalSujeira))
    qtdSujo = 0;
    while qtdSujo < qtdTotalSujeira:
        linha = random.randint(1,4)
        coluna = random.randint(1,4)
        #print('posicao sorteada: ['+str(linha)+'],['+str(coluna)+']')
        if matriz[linha][coluna] == 1:
            matriz[linha][coluna] = 0
            #print('Colocou sujeira na posicao ['+str(linha)+'],['+str(coluna)+']')
            qtdSujo+=1;
            #print('quantidade sujos = '+str(qtdSujo))

#percepção é composta pela posição atual X e Y e se esta sujo ou limpo
def agenteReativoSimples(percepcao):
    exibir(matriz)
    
    ##teste chamando a função mover
    mover(linha, coluna, "DIREITA")

####Fazendo aspirador andar, ainda nao está sendo utilizado
def percorrerSala():
    i=1
    j=1
    for i in range(1, 5):
        linha2 = i
        i+=1
        for j in range(1, 5):
            coluna2 = j
            time.sleep(1)
            print('posicao atual: ['+str(linha2)+'],['+str(coluna2)+']')
            plt.scatter(linha2, coluna2, marker=point)
            j+=1


def mover(linha, coluna, direcao):
    if direcao == "ACIMA":
        if linha != 1: #na linha 1 não deve executar o comando 'ACIMA'
            plt.scatter(coluna, linha-1, marker=point1)
    elif direcao == "ABAIXO":
        if linha != 4: #na linha 4 não deve executar o comando 'ABAIXO'
            plt.scatter(coluna, linha+1, marker=point1)
    elif direcao == "ESQUERDA":
        if coluna != 1: #na coluna 1 não deve executar o comando 'ESQUERDA'
            plt.scatter(coluna-1, linha, marker=point1)
    elif direcao == "DIREITA":
        if coluna != 4: #na coluna 4 não deve executar o comando 'ESQUERDA'
            plt.scatter(coluna+1, linha, marker=point1)

def estaSujo(linha, coluna, direcao):
    if direcao == "ACIMA":
        if linha != 1: #na linha 1 não deve executar o comando 'ACIMA'
            return 2
        if matriz[linha-1][coluna] == 0:
            return 1 #está suja
        return 0 #está limpa
    elif direcao == "ABAIXO":
        if linha != 4: #na linha 4 não deve executar o comando 'ABAIXO'
            return 2
        if matriz[linha+1][coluna] == 0:
            return 1 #está suja
        return 0 #está limpa
    elif direcao == "ESQUERDA":
        if coluna != 1: #na coluna 1 não deve executar o comando 'ESQUERDA'
            return 2
        if matriz[linha][coluna-1] == 0:
            return 1 #está suja
        return 0
    elif direcao == "DIREITA":
        if coluna != 4: #na coluna 4 não deve executar o comando 'ESQUERDA'
            return 2
        if matriz[linha][coluna+1] == 0:
            return true #está suja
        return 0 #está limpa


    
#def funcaoMapear():
    #achar um ponto que esteja limpo para começar?? Não entendi essa função

#contorno = 2(verde), limpo = 1(bege) e sujeira = 0(bordô)
matriz = [[2,2,2,2,2,2],
          [2,1,1,1,1,2],
          [2,1,1,1,1,2],
          [2,1,1,1,1,2],
          [2,1,1,1,1,2],
          [2,2,2,2,2,2]]
point = "*" #aqui pode usar o "." tbm pra ficar menor, ou até "*"
point1 = "o" #aqui pode usar o "." tbm pra ficar menor, ou até "*"
qtdTotalSujeira = 0
aspirador = null;



#Chamada do programa
inserirSujeiras()
agenteReativoSimples(0)



