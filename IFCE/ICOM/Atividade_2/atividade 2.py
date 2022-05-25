# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 18:54:40 2022

@author: Rafael Schneidewind Vieira
"""
import numpy as np

print('QUESTÃO 1:\nA extensão do arquivo anexado à atividade é ".CSV".\n')
print('QUESTÃO 2:\nO separador de dados utilizado nos arquivos é ","(Vírgula).\n')

print('QUESTÃO 3:(Verificar código)\n')
irisData1 = np.genfromtxt('iris_data_1.csv', delimiter = ',')
irisData2 = np.genfromtxt('iris_data_2.csv', delimiter = ',')

print(f'QUESTÃO 4:\nA dimensão do array "irisData1 é: {irisData1.shape}\nA dimensão do array "irisData2 é: {irisData2.shape}\n')

print('QUESTÃO 5:(Verificar código)\n')
irisdata = np.vstack((irisData1, irisData2))

print(f'QUESTÃO 6:\nO resultado do empilhamento dos arrays anteriores resultou em um array {irisdata.shape}\nE está de acordo com o esperado\n')

print('QUESTÃO 7:(Verificar código)\n')
irisdata = irisdata[~np.isnan(irisdata).any(axis=1)]

print(f'QUESTÃO 8:\nApós a remoção das linhas contendo valores NaN, o array ficou com a dimensão {irisdata.shape}\nE está de acordo com o esperado.\n')

nodes, counts = np.unique(irisdata[:,5], return_counts=True)
print(f'QUESTÃO 9:\nExistem {len(nodes)} valores diferentes na última coluna.\nEles são {nodes} e se repetem {counts} respectivamente.\n')

print('QUESTÃO 10:(Verificar código)\n')
for i in range(3,-1,-1):
    irisdata[:,5][irisdata[:,5] == i] = (i+1)
    
caracteristicas = irisdata[:, :5]
classes = irisdata[:,5:6]

print(f'Questão 11\nA variável de características ficou com a dimensão {caracteristicas.shape}.\nE a variável de Classes ficou com a dimensão {classes.shape}.')

np.savetxt('file_irisdata.csv', irisdata, delimiter=';')
#np.savetxt('file_caracteristicas.txt', caracteristicas, delimiter = ';')
#np.savetxt('file_classes.txt', classes, delimiter = ';')