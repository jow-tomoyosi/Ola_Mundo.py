d = int(input('Quantos dias alugados?'))
km = float(input('Quantos km foram rodados?'))

p = (d * 60) + (km * 0.15)

print('O valor que deve ser pago é de R${:.2f}'.format(p))
