#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

#Armazena o número que será analisado
num = int(input('Digite um número: '))

#Faz o cálculo do dobro
dobro = num * 2

#Faz o cálculo de triplo
triplo = num * 3

#Faz o cálculo da raíz quadrada
raiz = num **(1/2)

#Mostra o resultado ao usuário
print(f'O dobro de {num} é {dobro}.\n O triplo de {num} é {triplo}.\n A raíz quadrada de {num} é {raiz}.')