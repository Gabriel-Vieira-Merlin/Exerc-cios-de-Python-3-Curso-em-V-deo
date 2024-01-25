#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

#Armazena o nome
nome = input('Digite o nome: ')

#Separa o nome em uma lista
nome = nome.split()

#Pega o primeiro e último nome
primeiro_nome = nome[0]
ultimo_nome = nome[-1]

#Printa o resultado para o usuário
print(f'O primeiro nome é {primeiro_nome} e o último é {ultimo_nome}')