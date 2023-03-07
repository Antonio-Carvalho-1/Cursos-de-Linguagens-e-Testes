import math
#Biblioteca para funções matemáticas
import random
#Biblioteca para numeros aleatórios

#from math import sqrt
# Acima está a função que importária apenas a função sqrt

# import XXXXXX comando para importar uma biblioteca // EX: Import math
#from XXXXXX import XXXXXXX comando para importa somente um recurso de uma biblioteca em vez dela toda.

n1 = random.random() #gera um número aleatório
print(n1)
n2 = random.randint(1,100) #gera um número inteiro entre o intervalo digitado
print(n2)

num= int(input('Digite um número: '))
raiz = math.sqrt(num)
print('a raiz de {} é igual a {}'.format(num,raiz))
print('a raiz com 2 casa decimais é: {:.2f}'.format(raiz))
print('Com a função math.ceil a raiz será arredondada para cima. math.ceil = {}'.format(math.ceil(raiz)))
print('Com a função math.floor a raiz será arredondada para baixo. math.floor = {}'.format(math.floor(raiz)))

# math.ceil -> arredonda um numero para cima
# math.floor -> arredonda um numero para baixo


