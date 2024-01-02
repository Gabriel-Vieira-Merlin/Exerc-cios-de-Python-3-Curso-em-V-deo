# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

#Armazena o salário
salario = float(input('Forneça o valor do seu salário: R$ '))

#Armazena o valor do reajuste
reajuste = float(input('Digite a porcentagem do reajuste: '))

#Calculo do reajuste
salario_novo = salario + (reajuste * salario / 100)

print(f'Após o reajuste de {reajuste:.0f}%, o novo valor do salário é de R${salario_novo:.2f}.')