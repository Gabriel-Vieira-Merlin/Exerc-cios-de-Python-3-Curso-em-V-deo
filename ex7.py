#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

#Armazena a nota dos Bimestres
nota1 = float(input('Digite a nota do 1º Bimestre: '))
nota2 = float(input('Digite a nota do 2º Bimestre: '))
nota3 = float(input('Digite a nota do 3º Bimestre: '))
nota4 = float(input('Digite a nota do 4º Bimestre: '))

#Calcula a média
media = (nota1 + nota2 + nota3 + nota4) / 4

#Mostra a média
print(f'A média do aluno é {media}')