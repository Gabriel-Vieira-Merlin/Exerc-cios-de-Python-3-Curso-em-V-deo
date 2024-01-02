# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

#Armazena o preço
preco = float(input('Digite o preço do produto? R$ '))

#Armazena a variável do desconto
desconto = float(input('Qual é a porcentagem do desconto aplicado no produto? '))

#Realiza o cálculo para devolver o preço com desconto
precodesc = preco - (desconto * preco / 100)

#Mostra para o usuário o preço com desconto
print(f'O produto que antes custava R${preco:.2f}, agora tem {desconto:.0f}% de desconto e custa R${precodesc:.2f}. ')
