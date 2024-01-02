#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

#Define as variáveis
num = 0
ant = 0
suc = 0

#Armazena o número digitado
num = int(input('Digite um número: '))

#Faz a conta para calcular o antecessor e o sucessor
ant = num - 1
suc = num + 1

#Mostra a mensagem para o usuário
print(f'Analisando o número {num}, seu antecessor é {ant} e seu sucessor é {suc} ')