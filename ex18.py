#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
#Importa as funções de seno cosseno e tangente da biblioteca teca
from math import sin, cos, tan

#Coleta o ângulo a ser analisado
ang = float(input('Digite o ângulo a ser analisado: '))

#Mostra o resultado ao usuário
print(f'O ângulo de {ang} tem o seno de {math.sin(math.radians(ang)):.2f}\nO ângulo de {ang} tem o cosseno de {math.cos(math.radians(ang)):.2f}'
      f'\nO ângulo de {ang} tem a tangente de {math.tan(math.radians(ang)):.2f}')