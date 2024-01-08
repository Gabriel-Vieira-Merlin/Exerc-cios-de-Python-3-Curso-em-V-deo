#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
#Importa a função randrange da biblioteca random
from random import choice

#Coleta os alunos
alunos = [input('Digite o nome do 1º aluno: '), input('Digite o nome do 2º aluno: '), input('Digite o nome do 3º aluno: '), input('Digite o nome do 4º aluno: ')]

#Sorteia e exibe o escolhido para o usuário
print(f'O aluno sorteado foi o(a) {random.choice(alunos)}!')
