# -*- coding: utf-8 -*-
"""
@authors: Douglas, Joana e Leticia
"""
import matplotlib.pyplot as plt
import math
import csv


def lerArquivo():
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            row.insert(0, 1)
            X.append(row)
        

X = []
lerArquivo()
print(X)











