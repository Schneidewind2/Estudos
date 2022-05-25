print('Inteligência Computacional 2022.1 - Rafael Schneidewind Vieira \n  Atividade 1 - Questão 3\n \n' )

# Escreva um algoritmo que permita a leitura dos nomes de 5 pessoas e armazene os nomes
# lidos em uma lista. Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer
# de pessoa e depois escrever a mensagem ACHEI, se o nome estiver entre os 5 nomes lidos
# anteriormente (guardados na lista), ou NÃO ACHEI caso contrário.

listaNomes = []

for i in range(5):
    nomes = str(input('Insira o nome da %dª pessoa: ' %(i+1)))
    listaNomes.append(nomes.upper())
buscaNomes = str(input('Insira o nome da pessoa a ser procurada na lista: '))
capNomes = buscaNomes.upper()

if capNomes in listaNomes:
    print('Achei')
else:
    print('Não achei')
