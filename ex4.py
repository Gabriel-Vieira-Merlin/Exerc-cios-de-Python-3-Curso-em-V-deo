#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

#Armazena o número que será analisado
num = int(input('Digite um valor: '))

#Calula os sucessores e antecessores
antecessor = num - 1
sucessor = num + 1

#Retorna a informação para o usuário
print(f"O número {num} tem como antecessor o número {antecessor} e como sucessor o número {sucessor}")