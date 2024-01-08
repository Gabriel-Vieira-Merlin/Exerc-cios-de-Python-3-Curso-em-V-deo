#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
#Importa a função truncate da biblioteca math
from math import trunc

#Coleta o número a ser analisado
num = float(input('Digite um número: '))

#Mostra para o usuário o número e sua porção inteira
print(f'O valor digitado foi {num} e sua porção inteira é {math.trunc(num)}.')
