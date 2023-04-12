import random

n1 = input('Digite o nome do aluno 1:\n')
n2 = input('Digite o nome do aluno 2:\n')
n3 = input('Digite o nome do aluno 3:\n')
n4 = input('Digite o nome do aluno 4:\n')

lista = [n1, n2, n3, n4] #cria um vetor de strings com os nomes dos alunos -> Vetor Lista

escolhido = random.choice(lista) #Sorteia um elemento aleatório do vetor(lista) 

print('o aluno escolhido foi: {}'.format(escolhido))
