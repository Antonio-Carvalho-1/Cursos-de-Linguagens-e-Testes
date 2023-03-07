a = int(input('Digite um número para ver sua tabuada:'))
print('A tabuada desse é:')
b=1
print('____________________')
while (b<=10):
    print('{} x {:2} = {}'.format(a,b,a*b)) # O (:2) define quantos zero a esquerda/espaçamentos eu vou querer
    b=b+1
print('____________________')
