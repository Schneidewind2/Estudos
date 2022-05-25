# -*- coding: utf-8 -*-
"""
Created on Tue May  3 18:37:36 2022

@author: Rafael Schneidewind Vieira
"""

import pandas as tobias

print('Questão 2:\nA extensão dos arquivos é CSV.\n')

print('Questão 3:\nOs arquivos contém informações de artistas, faixas, popularidade, playlistis que estão entre outras.\n')
      
alternative_df = tobias.read_csv('alternative_music_data.csv')
blues_df = tobias.read_csv("blues_music_data.csv")
hiphop_df = tobias.read_csv("hiphop_music_data.csv")

print(f'QUESTÃO 5:\nA base de dados "Alternative Music" possui a dimensão {alternative_df.shape}.\nA base de dados "Blues Music" possui a dimensão {blues_df.shape}.\n')
print(f'A base de dados "HipHop Music" possui a dimensão {hiphop_df.shape}.\n\n')

print(f'QUESTÃO 6:\nOs nomes das colunas são:\n{alternative_df.columns}\n\n')

print(f'QUESTÃO 7:\nOs tipos de dados de cada coluna são:\n{alternative_df.dtypes}\n\n')

print('QUESTÕES 8, 9 E 10: VERIFICAR CÓDIGO:\n\n')

alternative_df.loc[:,'Code'] = 1
blues_df.loc[:,'Code'] = 2
hiphop_df.loc[:,'Code'] = 3

print('QUESTÃO 11: VERIFICAR CÓDIGO\n\n')
mix_df = tobias.concat([alternative_df, blues_df, hiphop_df], ignore_index=True)

print(f'QUESTÕES 12 E 13:\nNão existem entradas com valores "NaN" no DataFrame.\nSua contagem segue abaixo:\n{mix_df.isnull().sum()}\n\n')

mix_nostring_df = mix_df.select_dtypes(exclude=['object'])
print(f'QUESTÃO 14:\nApós a remoção das colunas que continham\nstrings o Dataframe ficou com as dimensões {mix_nostring_df.shape}\ne restaram as seguintes colunas com seus tipos:\n{mix_nostring_df.dtypes}')

mix_nostring_df.to_csv('mix_nostring.csv')