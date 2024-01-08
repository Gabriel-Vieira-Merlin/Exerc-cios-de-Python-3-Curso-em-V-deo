# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.
import math
#Importa a função hypot da biblioteca math
from math import hypot

#Coleta os catetos opostos e adjacentes
co = float(input('Qual o valor do cateto oposto? '))
ca = float(input('Qual o valor do cateto adjascente? '))

#Mostra o resultado para o usuário
print(f'O resultado da hipotenusa é {math.hypot(co,ca):.2f}')