# -*- coding: utf-8 -*-
"""
@authors: Douglas, Joana e Leticia
"""
import matplotlib.pyplot as plt
import math
import csv
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

def polyfit(matrizData):
    coefs = np.polynomial.polynomial.polyfit(matrizData[:,0], matrizData[:,1], 1)
    ffit = np.poly1d(coefs)
    x_new = np.linspace(matrizData[0,0], matrizData[-1,1], num=len(matrizData[:,0])*10)
    fig1 = plt.figure()                                                                                           
    ax1 = fig1.add_subplot(111)                                                                                   
    ax1.scatter(matrizData[:,0], matrizData[:,1])                                                                     
    ax1.plot(x_new, ffit(x_new),'r')                                                                     
    plt.show()

geraGrafico(lerBaseDados())
polyfit((lerBaseDados()))


