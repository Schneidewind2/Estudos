from statistics import mean


print('Inteligência Computacional 2022.1 - Rafael Schneidewind Vieira \n  Atividade 1 - Questão 1\n \n' )

# Uma loja está levantando o valor total de todas as mercadorias em estoque.
# Escreva um algoritmo que permita a entrada das seguintes informações: a) o
# número total de mercadorias no estoque; b) o valor de cada mercadoria. Ao
# final imprimir o valor total em estoque e a média de valor das mercadorias.)

qtdMercadoria = int(input('Insira a quantidade de mercadorias no estoque: '))
listaValores = []

while qtdMercadoria <= 0:
	qtdMercadoria = int(input('Por favor, insira um valor maior que ZERO!: '))

for i in range(qtdMercadoria):
	valorMercadoria = float(input('Insira o valor da %dª mercadoria R$: ' %(i+1)))
	listaValores.append(valorMercadoria)

totalEstoque=sum(listaValores)

print('O valor total do estoque é de: R$ %.2f' %totalEstoque)

print('A média de valores do seu estoque é de: R$ %.2f' %mean(listaValores))
