from statistics import mean

print('Inteligência Computacional 2022.1 - Rafael Schneidewind Vieira \n  Atividade 1 - Questão 2\n \n' )

# Faça um algoritmo para ler e armazenar em um vetor a temperatura média de 6 dias do ano.
# Calcular e escrever: a) Menor temperatura b) Maior temperatura c) Temperatura média d)
# O número de dias em que a temperatura foi inferior a média.

tempDias = []
mediaBaixa = 0 

for i in range(6):
    temp = float(input('Insira a temperatura média do %dº dia no vetor: ' %(i+1)))
    tempDias.append(temp)
for j in range(len(tempDias)):
    if tempDias[j] < (mean(tempDias)):
        mediaBaixa += 1
  
print('A temperatura mínima ente os 6 dias é de: %.1fº' %(min(tempDias)))
print('A temperatura mínima ente os 6 dias é de: %.1fº' %(max(tempDias)))
print('A média de temperatura ente os 6 dias é de: %.1fº' %(mean(tempDias)))

print('A temperatura ficou abaixo da média durante %d dias.' %mediaBaixa)