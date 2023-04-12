import random

n1 = input('Digite o nome do primeiro Aluno\n')
n2 = input('Digite o nome do segundo Aluno\n')
n3 = input('Digite o nome do terceiro Aluno\n')
n4 = input('Digite o nome do quarto Aluno\n')

lista = [n1, n2, n3, n4] #cria um vetor com os elementos n1 até n4

random.shuffle(lista) # embaralha(aleatoriamente) todos os elementos de um vetor

print('A ordem de aprensentação será')
print(lista) #reconhece como vetor e o printa
