#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

#Armazena o valor que será convertido
valorbrl = float(input(f'Digite o valor em reais para ser covertido: '))

#Armazena a variável de cotação do Dólar
cotacao = 3.27

#Realiza a conversão
valordol = valorbrl / cotacao

#Exibe o valor convertido para o usuário
print(f'R${valorbrl} corresponde a U${valordol}')