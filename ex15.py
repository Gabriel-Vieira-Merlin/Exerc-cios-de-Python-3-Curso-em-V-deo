#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

#Armazena os dias alugados
dias = float(input('Dias alugados: '))

#Armazena os Quilômetros rodados
km = float(input('Quilômetros rodados: '))

#Calcula o preço do aluguel
aluguel = (dias * 60) + (km * 0.15)

#Exibe o valor total
print(f'O preço do aluguel do carro é R${aluguel}.')
