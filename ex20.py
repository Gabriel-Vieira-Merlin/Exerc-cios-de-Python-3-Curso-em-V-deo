#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
#Importa a função shuffle da biblioteca random
from random import shuffle

#Coleta o nome dos alunos
alunos = [input('Digite o nome do 1º aluno: '), input('Digite o nome do 2º aluno: '),
          input('Digite o nome do 3º aluno: '), input('Digite o nome do 4º aluno: ')]

#Aleatoriza a ordem da lista
random.shuffle(alunos)

#Mostra ao usuário a ordem
print(f'A ordem dos alunos que irão apresentar os trabalhos é {alunos}.')