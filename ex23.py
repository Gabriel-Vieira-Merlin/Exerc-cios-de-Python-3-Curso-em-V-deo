#Faça um programa que leia um número com 4 dígitos e mostre na tela cada um dos dígitos separados.

#Armazena o número em uma variável
num = input('Digite um número de 0 a 9999: ')

#Separa os digitos em variáveis
milhar = int(num[0])
centena = int(num[1])
dezena = int(num[2])
unidade = int(num[3])

#Printa os números separados
print(f'Milhar: {milhar*1000}\nCentena: {centena*100}\nDezena: {dezena*10}\nUnidade: {unidade}')