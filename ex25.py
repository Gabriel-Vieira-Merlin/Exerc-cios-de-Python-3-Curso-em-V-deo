#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

#Armazena o nome em uma variável
nome = input('Digite o nome: ')

#Alterando a variável
nome = nome.strip().upper()

#Verifica se tem Silva no nome e printa o resultado
print('SILVA' in nome)