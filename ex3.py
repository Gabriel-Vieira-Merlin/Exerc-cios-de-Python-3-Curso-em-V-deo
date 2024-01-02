#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

#Armazena o que foi digitado
texto = input('Digite algo: ')

#Informa que tipo é o texto
print(f"O tipo primitivo do que foi digitado é {type(texto)}")
#Informa se o texto tem espaços
print(f"O texto é composto somente de espaços? {texto.isspace()}")
#Informas se o texto é um número
print(f"É um número? {texto.isnumeric()}")
#Informa se o texto é alfabético
print(f"É alfabético? {texto.isalpha()}")
#Informa se o texto é alfanumérico
print(f"É alfanúmerico? {texto.isalnum()}")
#Informa se o texto é minúsculo
print(f"Está em minúsculo? {texto.islower()}")
#Informa se o texto é maiúsculo
print(f"Está em maiúsculo? {texto.isupper()}")
#Informa se o texto está captalizado
print(f"Está capitalizada? {texto.istitle()}")