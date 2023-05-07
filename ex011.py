lar = float(input('Digite a largura da parede:'))
al = float(input('Digite a altura da parede:'))

ar = lar*al
tin = ar/2

print('Sua parede tem a dimensão de {}X{} e sua área é de {:.3f}m².'.format(lar, al, ar))
print('Para pintar essa parede, você precisará de {:.3f}L de tinta.'.format(tin))
