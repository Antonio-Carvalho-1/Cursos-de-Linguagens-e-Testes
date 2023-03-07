d = float(input('Quantos dias alugados? '))
k = float(input('Quantos km rodados? '))
r = (d*60)+(k*0.15)
print('O total a pagar é de {:.2f}R$'.format(r))