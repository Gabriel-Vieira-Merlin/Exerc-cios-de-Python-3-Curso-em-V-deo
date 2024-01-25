#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

#Armazena a frase a ser analisada
frase = input('Digite uma frase: ')

#Altera a variável
frase = frase.strip().upper()

#Conta quantos "a" a frase possui
qtd_a = frase.count("A")

#Mostra a posição do primeiro "a"
primeiro_a = frase.find('A')

#Mostra posição do último "a"
ultimo_a = frase.rfind('A')

#Printa os resultados para o usuário
print(f'A letra "A" aparece {qtd_a}\nO primeiro "A" está na posição {primeiro_a}\nO último "A" está na posição {ultimo_a}')