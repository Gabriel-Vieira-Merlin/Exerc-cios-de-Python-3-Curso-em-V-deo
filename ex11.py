#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

#Armazena a altura
altura = float(input('Forneça a altura desejada: '))

#Armazena a largura
largura = float(input('Forneça a largura desejada: '))

#Calcula a área
area = altura * largura

#Calcula a quantidade de tinta necessária
tinta = area / 2

#Exibe a tinta necessária
print(f'A parede possui uma área de {area}m2 e será necessário {tinta}L de tinta.')