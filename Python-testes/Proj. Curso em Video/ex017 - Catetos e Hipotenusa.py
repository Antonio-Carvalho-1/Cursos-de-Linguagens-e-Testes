import math


ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))
# h = ((ca**2)+(co**2))**(1/2) # um número elevado a 1/2 é = a sua raiz quadrada
# h = math.sqrt((ca**2)+(co**2))   # outra forma de fazer utilizando a biblioteca math
h = math.hypot(ca,co)
print('A hipotenusa é igual a: {}'.format(h))