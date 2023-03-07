a = float(input('Digite a largura da parede em m: '))
b = float(input('Digite a altura da parede em m: '))
c = a*b
print('Sua parede tem dimensão de {}m x {}m e sua área é de {}m²'.format(a,b,c))
print('Para pintar essa parede será necessário {}l de tinta'.format(c/2))