val = float(input('Qual o valor do produto? R$'))

des = val*0.05
vf = val-des

print('Com o desconta de %5 você pagará R${:.2f}'.format(vf))
