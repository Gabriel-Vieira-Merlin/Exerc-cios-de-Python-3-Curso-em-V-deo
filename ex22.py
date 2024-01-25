#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo sem considerar espaços.
#Quantas letras tem o primeiro nome.

#Coleta o nome que será analisado
nome = input('Digite seu nome completo: ')

#Mostra para o usuário o
print(f'O nome com todas as letras maiúsculas fica {nome.upper()}\nO nome com todas as letras minúsculas fica {nome.lower()}\n'
      f'O nome possui {len(nome) - nome.count(" ")} letras\nO primeiro nome é {nome.split()[0]} e tem {len(nome.split()[0])} letras')
