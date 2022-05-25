print('Inteligência Computacional 2022.1 - Rafael Schneidewind Vieira \n  Atividade 1 - Questão 4\n \n' )

# Uma empresa quer verificar se um empregado está qualificado para a aposentadoria ou não.
# Para estar em condições, um dos seguintes requisitos deve ser satisfeito:
#  Ter no mínimo 65 anos de idade.
#  Ter trabalhado no mínimo 30 anos.
#  Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos.
# Com base nas informações acima, faça um algoritmo que leia: o número do empregado
# (código), o ano de seu nascimento e o ano de seu ingresso na empresa. O programa deverá
# escrever a idade e o tempo de trabalho do empregado e a mensagem 'Requerer
# aposentadoria' ou 'Não requerer'.

import datetime 
hoje = datetime.date.today()
dataNasc = datetime.datetime.strptime(input('Insira a data de nascimento do funcionário(DD/MM/AAAA):'), '%d/%m/%Y').date()
dataEmpresa = datetime.datetime.strptime(input('Insira a data de ingresso do funcionário(DD/MM/AAAA):'), '%d/%m/%Y').date()

def calculateAge(data): 
    diasAno = 365.2425   
    calcIdade = int((datetime.date.today() - data).days / diasAno) 
    return calcIdade 

idade = calculateAge(dataNasc)
tempoServico = calculateAge(dataEmpresa)

if ((idade >= 65) or (tempoServico >= 30) or ((idade >= 60) and (tempoServico >= 25))) :
    print('O funcionário possui %i anos e %i anos de casa, Ele pode requerer a aposentadoria' %(idade, tempoServico) ) 

else:
    print('O funcionário possui %i anos e %i anos de casa, Ele não pode requerer a aposentadoria' %(idade,tempoServico) )