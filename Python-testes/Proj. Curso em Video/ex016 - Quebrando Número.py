import math

'''Tres aspas deixa tudo em comentário'''

# math.trunc() Retorna o número Inteiro

a = float(input('Digite um número: '))

print('O número digitado foi {}\n1: A sua porção inteira é: {}'.format(a,int(a)))
print('2: A sua porção inteira é: {:.0f}'.format(math.trunc(a)))
print('3: A sua porção inteira é: {:.0f}'.format(a//1))