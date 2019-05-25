"""Funcao de aptdão (fitness) para o problema do caixeiro viajante - 
código em Matlab/Octave"""

function dist=cvfun(pop)

# Utiliza variaveis globais "x" e "y"
global x y
[Npop,Ncidade]=size(pop);
tour=[pop pop(:,1)]; # gera a matriz 20x21 da populacao onde a ultima coluna eh a copia da primeira coluna (o agente deve voltar a cidade inicial)

# distancia entre as cidades
for i=1:Ncidade
    for j=1:Ncidade
        dcidade(i,j)=sqrt((x(i)-x(j))^2+(y(i)-y(j))^2);
    end 
end 

# custo de cada cromossomo - a soma das distâncias para cada indivíduo
for i=1:Npop
    dist(i,1)=0;
    for j=1:Ncidade
        # Soma das distancias para cada cromossomo
        dist(i,1)=dist(i)+dcidade(tour(i,j),tour(i,j+1)); 
    end 
end 
end 