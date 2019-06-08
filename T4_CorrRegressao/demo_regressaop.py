# -*- coding: utf-8 -*-
"""
@authors: Douglas, Joana e Leticia
"""
import matplotlib.pyplot as plt
import scipy.io as scipy
import numpy as np

def lerBaseDados():
    matrizData = []
    mat = scipy.loadmat('data_preg.mat')
    matrizData = mat['data']
    return matrizData
    
def geraGrafico(matrizData):
    plt.scatter(matrizData[:,0], matrizData[:,1])
    
#    plt.plot(x,resultados)
#    plt.title("Correlação:"+str(r)+"  B0:"+str(b0)+"  B1:"+str(b1))
    plt.figure()

#fazendo a função polyfit
def polyfit(matrizData):
    coefs1 = np.polyfit(matrizData[:,0], matrizData[:,1], 1)
    coefs1 = np.polyfit(matrizData[:,0], matrizData[:,1], 2)
    coefs3 = np.polyfit(matrizData[:,0], matrizData[:,1], 3)
    coefs8 = np.polyfit(matrizData[:,0], matrizData[:,1], 8)
    
    y1 = coefs1[1]+coefs1[0]*matrizData[:,0]
    y2 = coefs3[2]+coefs3[1]*matrizData[:,0]+coefs3[0]*matrizData[:,0]**2
    y3 = coefs3[3]+coefs3[2]*matrizData[:,0]+coefs3[1]*matrizData[:,0]**2+coefs3[0]*matrizData[:,0]**3
    y8 = coefs8[8]+coefs8[7]*matrizData[:,0]+coefs8[6]*matrizData[:,0]**2+coefs8[5]*matrizData[:,0]**3+coefs8[4]*matrizData[:,0]**4+coefs8[3]*matrizData[:,0]**5+coefs8[2]*matrizData[:,0]**6+coefs8[1]*matrizData[:,0]**7+coefs8[0]*matrizData[:,0]**8
    
    fig1 = plt.figure()                                                                                           
    ax1 = fig1.add_subplot(111)                                                                                   
    ax1.scatter(matrizData[:,0], matrizData[:,1])                                                                     
    ax1.plot(matrizData[:,0], y1,'r')
    ax1.plot(matrizData[:,0], y2,'g')
    ax1.plot(matrizData[:,0], y3,'b')   
    ax1.plot(matrizData[:,0], y8,'y')                                                              
    plt.show()
    
#calcular o erro quadratico medio
    
    

#geraGrafico(lerBaseDados())
polyfit((lerBaseDados()))


