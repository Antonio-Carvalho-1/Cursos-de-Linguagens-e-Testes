a = float(input('digite a altura em m '))
b = float(input('digite a largura em m '))
area = a*b
litros = area//2
resto = area%2
if resto != 0:
    litros = litros+1

print('A area é {}m², e serão necessários {} litros de tinta'.format(area,litros))
