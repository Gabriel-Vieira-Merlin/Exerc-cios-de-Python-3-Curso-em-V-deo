#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

#Armazena o nome da cidade em uma variável
cidade = input('Digite o nome da cidade: ')

#Altera a variável para eliminar os espaços, deixar tudo em maiúsculo e pegar só as 5 primeiras letras
cidade = cidade.strip().upper()[:5]

#Printa a variável
print(cidade=='SANTO')